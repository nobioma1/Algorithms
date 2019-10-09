#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch_count = 0
    while True:
        for i in recipe.keys():
            if i in ingredients:
                if ingredients[i] < recipe[i]:
                    return batch_count
                else:
                    ingredients[i] = ingredients[i] - recipe[i]
            else:
                return batch_count
        batch_count += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
