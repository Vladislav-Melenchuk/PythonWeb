from django.http import HttpResponseForbidden
from django.core.cache import cache
import time

class RateLimitMiddleware:
    RATE_LIMIT_PATH = "/restricted-area/"
    MAX_REQUESTS = 5
    INTERVAL = 60

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(self.RATE_LIMIT_PATH):
            ip = request.META.get("REMOTE_ADDR")
            key = f"rl_{ip}"

            data = cache.get(key, {"count": 0, "start": time.time()})

            if time.time() - data["start"] > self.INTERVAL:
                data = {"count": 0, "start": time.time()}

            data["count"] += 1
            cache.set(key, data, timeout=self.INTERVAL)

            if data["count"] > self.MAX_REQUESTS:
                return HttpResponseForbidden("Rate limit exceeded")

        return self.get_response(request)
