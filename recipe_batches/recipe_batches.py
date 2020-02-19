#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Initialize a variable to hold number of batches so far
    batch_count = 0

    # Keep the Loop running and exit on a return statement
    while True:
        # Loop through the keys in the recipe dictionary
        for i in recipe.keys():
            # Check if the current key in recipe is also in the ingredients dictionary
            if i in ingredients:
                # Check if the value of the current ingredients is less than the value of the current recipe
                if ingredients[i] < recipe[i]:
                    # End the loop and return the current batch_count
                    return batch_count
                else:
                    # Remove the amount of the recipe from the current ingredients
                    ingredients[i] -= recipe[i]
            else:
                # Return the batch count if the current recipe is not in ingredients
                return batch_count
        # After the cycle for each item less the amount of recipe, increment the batch count by 1
        batch_count += 1

# A little more efficent solution 
def recipe_batches_e(recipe, ingredients):
    # define a variable to hold the number of batches
    # we have to loop through and subtract recipe from ingredient
    # check if the recipe and ingredients have same properties
    batches = 0

    # if the recipe and the ingredients don't match, end the loop
    if (ingredients.keys() != recipe.keys()):
        return batches

    # keep the subtraction loop running till we can subtract anymore
    while True:
        # for each ingredient remove the amount of ingredient consumed
        for item in ingredients:
            # quantity of ingredient has to be greater than the recipe
            if (ingredients[item] >= recipe[item]):
                ingredients[item] = ingredients[item] - recipe[item]
            else:
                return batches

        batches += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
