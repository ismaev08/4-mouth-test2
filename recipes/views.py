from django.shortcuts import render, redirect
from .models import Recipe, Ingredient, Collection
from .forms import RecipeForm, IngredientForm, CollectionForm

# Список рецептов
def recipe_list(request):
    query = request.GET.get('q', '')
    recipes = Recipe.objects.filter(title__icontains=query)
    return render(request, 'recipe_list.html', {'recipes': recipes})

# Детали рецепта
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    total_calories = sum(ingredient.calories * ingredient.quantity for ingredient in ingredients)
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients, 'total_calories': total_calories})

# Добавление нового рецепта
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

# Добавление ингредиента
def add_ingredient(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', pk=recipe.id)
    else:
        form = IngredientForm()
    return render(request, 'add_ingredient.html', {'form': form, 'recipe': recipe})

# Удаление рецепта
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('recipe_list')

# Редактирование ингредиента
def edit_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=ingredient.recipe.id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'edit_ingredient.html', {'form': form})

# Детали коллекции
def collection_detail(request, pk):
    collection = Collection.objects.get(pk=pk)
    return render(request, 'collection_detail.html', {'collection': collection})
