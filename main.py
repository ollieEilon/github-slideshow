import app_data.init_db
import bo.recipe

app_data.init_db.init_db()
my_recipe = bo.recipe.recipe()
my_recipe.name = "Burger"
my_recipe.method = "Fry me"
my_recipe.ingredients = "beef"
my_recipe.time = "10 minutes"
my_recipe.save_recipe()


