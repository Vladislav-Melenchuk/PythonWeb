import json
import os
from django.conf import settings

RECIPES_FILE = os.path.join(settings.BASE_DIR, 'recipes.json')


def load_recipes():
    if not os.path.exists(RECIPES_FILE):
        return []
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_recipes(recipes):
    with open(RECIPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)


def get_next_id(recipes):
    return max((r["id"] for r in recipes), default=0) + 1


def get_recipe_by_id(recipe_id):
    recipes = load_recipes()
    for r in recipes:
        if r["id"] == recipe_id:
            return r
    return None


def delete_recipe_by_id(recipe_id):
    recipes = load_recipes()
    recipes = [r for r in recipes if r["id"] != recipe_id]
    save_recipes(recipes)
