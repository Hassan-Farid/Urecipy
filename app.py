import streamlit as st
from db_ops import DBOps
import http
from utils import *
from gtts import gTTS
from PIL import Image

def main():
    #Setting up application settings
    st.set_page_config(page_title="Urecipy - Your Personal Recipe Notebook")
    
    #Setting up database for application
    db = DBOps()
    db.create_table()
    
    #Loading the HTML templates
    about_temp = open("./templates/home.html", 'r').read()
    recipe_temp = open("./templates/recipe.html", 'r').read()
    
    #Setting up the logo header
    st.image(Image.open('logo.png'), width=256)
    
    #Setting up the menu selection
    menu = ["Home", "View Recipes", "Add/Remove Recipes"]
    choice = st.sidebar.selectbox("Menu", menu)

    #Selection of Home Page
    if choice == "Home":
        st.markdown(about_temp, unsafe_allow_html=True)

    #Selection of Recpies Page
    elif choice == "View Recipes":
        all_recipes = db.view_all_recipes()
        if all_recipes:
            all_recipes = [recipe[0] for recipe in all_recipes]
            postlist = st.sidebar.selectbox("Recipes", all_recipes)
            postrecipe = db.get_recipe(postlist)
            title, ingredients, procedure, postdate = postrecipe[0]
            st.markdown(recipe_temp.format(title, ingredients, procedure, postdate), unsafe_allow_html=True)
            recipe_audio = open('./audios/{}.mp4'.format(title), mode='rb').read()
            st.audio(recipe_audio, format='audio/mpeg')
            
    #Selection of Creating/Removing Recipes Page
    elif choice == "Add/Remove Recipes":
        ops_menu = st.sidebar.selectbox("Add/Remove", ["Add Recipe", "Remove Recipe"])
        if ops_menu == "Add Recipe":
            st.subheader("Add a recipe")
            recipe_title = st.text_input("Enter Recipe Name: ", max_chars=50)
            recipe_url = st.text_input("Enter Recipe URL (without http/https): ")
            connected = http.client.HTTPConnection(recipe_url)
            if st.button("Add"):
                all_recipes = [recipe[0] for recipe in db.view_all_recipes()]
                if recipe_title not in all_recipes:
                    audio_text = get_text_from_audio(recipe_url, recipe_title)
                    recipe_ingredients, recipe_procedure = get_recipe_completion(audio_text=audio_text)
                    ingredients = get_ingredients(recipe_ingredients)
                    procedure = get_procedure(recipe_procedure)
                    db.add_recipe(recipe_title, ingredients, procedure)
                    recipe_audio_text = "Ingredients: {} \n Procedure: {}".format(ingredients, procedure)
                    recipe_audio = gTTS(recipe_audio_text, lang="en", slow=False)
                    recipe_audio.save("./audios/{}.mp4".format(recipe_title))
                else:
                    print("Recipe already in list!")
        elif ops_menu == "Remove Recipe":
            st.subheader("Remove a recipe")
            recipe_title = st.text_input("Enter Recipe Name: ", max_chars=50)
            if st.button("Remove"):
                all_recipes = db.view_all_recipes()
                if all_recipes:
                    all_recipes = [recipe[0] for recipe in all_recipes]
                    if recipe_title in all_recipes:
                        db.remove_recipe(recipe_title)
                        os.remove("./audios/{}.mp4".format(recipe_title))
                else:
                    print("No recipes in the list!")
                    
if __name__ == '__main__':
    main()
