#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = 0
    if len(recipe) != len(ingredients):
        return batches
    else:
        for key in recipe:
            if batches > ingredients[key] // recipe[key] and batches != 0:
                batches = ingredients[key] // recipe[key]
            elif batches == 0:
                batches = ingredients[key] // recipe[key]
            else:
                pass
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    recipe = {'milk': 2, 'sugar': 40, 'butter': 20}
    ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
