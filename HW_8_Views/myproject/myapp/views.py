import json
from django.http import (
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotFound,
)
from django.core.cache import cache
from .data_storage import data_dict

from django.http import HttpResponse

def restricted_area(request):
    return HttpResponse("This is restricted area")


def get_item(request, item_id):
    key = f"item_{item_id}"
    cached = cache.get(key)
    if cached:
        return JsonResponse({"source": "cache", "result": cached})

    processed = {"id": item_id, "value": item_id * 2}
    cache.set(key, processed, timeout=60)
    return JsonResponse({"source": "processed", "result": processed})


def normalize_user_data(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")
    try:
        data = json.loads(request.body)
    except:
        return HttpResponseBadRequest("Invalid JSON")

    if "name" not in data or "age" not in data:
        return HttpResponseBadRequest("Missing fields")

    name = str(data["name"]).strip().capitalize()
    try:
        age = int(data["age"])
    except:
        return HttpResponseBadRequest("Age must be number")

    return JsonResponse({"name": name, "age": age})


def detect_device(request):
    ua = request.META.get("HTTP_USER_AGENT", "").lower()
    if any(x in ua for x in ["iphone", "android", "mobile", "ipad"]):
        return HttpResponseRedirect("/mobile-page/")
    return HttpResponse("Добро пожаловать на сайт!")


def get_data_by_key(request, key):
    if key in data_dict:
        return JsonResponse({key: data_dict[key]})
    return HttpResponseNotFound("Not found")


def update_data(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")
    try:
        new_data = json.loads(request.body)
    except:
        return HttpResponseBadRequest("Invalid JSON")

    if not isinstance(new_data, dict):
        return HttpResponseBadRequest("JSON must be object")

    data_dict.update(new_data)
    return JsonResponse({"status": "updated", "data": data_dict})
