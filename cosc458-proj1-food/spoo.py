import json
import random
import requests

class Recipe:
    def __init__(self, title, servings, link, image, ingredients):
        self.title = title
        self.servings = servings # or prep_time
        self.link = link
        self.image = image
        self.ingredients = ingredients
        
    def __str__(self):
        return "title: " + self.title +'\n' + "servings: " + self.servings + "\n" + "link: " +  self.link + "\n" "image: "\
        + self.image  + "ingredients: " + self.ingredients

def get_recipe_instructions(api_key, id):
    url = "https://api.spoonacular.com/recipes/" + str(id) + "/information?apiKey=" + api_key
    ingredients = []
    
    response = requests.get(url)
    json_body = response.json()
    
    for x in json_body["extendedIngredients"]:
        ingredients.append(x["original"])
        
    return ingredients
    
def get_recipe_link(api_key, id):
    url = "https://api.spoonacular.com/recipes/" + str(id) + "/information?apiKey=" + api_key
    
    response = requests.get(url)
    json_body = response.json()
    return json_body["sourceUrl"]
    
def get_recipe_data():
    # api_key = os.getenv('spoo_token') - This is for Heroku
    api_key = "7726f86057b44e718f733c24ce29b7df"
    url = "https://api.spoonacular.com/recipes/search?apiKey=" + api_key + "&query=sweet+potato&number=20"

    response = requests.get(url)
    json_body = response.json()
 
    print("hi")
    print(json.dumps(json_body, indent=2))
    
    # Find the how many items (songs containing text or songs from an artist)
    size = json_body['totalResults']
    print("size" + str(size))
    
    # Choose a random number for our indices
    index = random.randint(1 ,15)
    
    # Retrieve our information
    id = json_body["results"][index]["id"]
    title = json_body['results'][index]['title']
    servings = json_body["results"][index]['servings']
    recipe_uri = json_body["baseUri"]
    recipe_file = json_body["results"][index]["image"]
    image = recipe_uri + recipe_file
    print("Image:" + image)
    link = get_recipe_link(api_key, id)
    ingredients = get_recipe_instructions(api_key, id)
    # artist_image = json_body['response']['hits'][index]['result']['primary_artist']['image_url']
    
    recipe_data = Recipe(title, servings, link, image, ingredients)
    
    return recipe_data