from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import RecipeForm
from .models import (
    load_recipes, save_recipes,
    get_next_id, get_recipe_by_id,
    delete_recipe_by_id
)


def recipe_list(request):
    recipes = load_recipes()
    return render(request, 'recipes/list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        raise Http404("Рецепт не знайдено")
    return render(request, 'recipes/detail.html', {'recipe': recipe})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipes = load_recipes()
            new_id = get_next_id(recipes)
            data = form.cleaned_data

            recipe = {
                "id": new_id,
                "title": data["title"],
                "description": data["description"],
                "ingredients": data["ingredients"].splitlines(), 
                "instructions": data["instructions"],
            }
            recipes.append(recipe)
            save_recipes(recipes)
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    return render(request, 'recipes/form.html', {'form': form, 'mode': 'add'})


def edit_recipe(request, recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        raise Http404("Рецепт не знайдено")

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipes = load_recipes()
            data = form.cleaned_data
            for r in recipes:
                if r["id"] == recipe_id:
                    r["title"] = data["title"]
                    r["description"] = data["description"]
                    r["ingredients"] = data["ingredients"].splitlines()
                    r["instructions"] = data["instructions"]
                    break
            save_recipes(recipes)
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        initial = {
            "title": recipe["title"],
            "description": recipe["description"],
            "ingredients": "\n".join(recipe["ingredients"]),
            "instructions": recipe["instructions"],
        }
        form = RecipeForm(initial=initial)

    return render(request, 'recipes/form.html', {'form': form, 'mode': 'edit', 'recipe_id': recipe_id})


def delete_recipe(request, recipe_id):
    delete_recipe_by_id(recipe_id)
    return redirect('recipe_list')
