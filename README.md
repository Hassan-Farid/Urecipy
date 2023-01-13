# Urecipy - Personal Recipe Notebook

Urecipy is a web application that allows users to view, add, and remove their personal recipes. Built using the [Streamlit](https://streamlit.io/) framework and python, it provides an easy-to-use interface for users to manage their recipe collection.

The application utilizes a SQLite database for storage and retrieval of recipes, and has the following features:
- View all recipes
- Add new recipes
- Remove existing recipes
- Text-to-speech audio for the ingredients and procedure of a recipe
- View and listen to the recipe's audio

## Getting Started

### Prerequisites

You will need to have python and pip installed on your machine. You can download the latest version of python [here](https://www.python.org/downloads/).

You will also need to install the following python packages:
- Streamlit
- gTTS
- PIL
- sqlite3

You can install these packages by running the following command:

> pip install streamlit gTTS PIL sqlite3

### Installing

Clone the repository to your local machine using the following command:

> git clone https://github.com/Hassan-Farid/Urecipy.git

Navigate to the project directory and run the following command to start the application:

> streamlit run main.py

## Built With
- [Streamlit](https://streamlit.io/) - The web framework used
- [gTTS](https://pypi.org/project/gTTS/) - Text-to-speech library
- [PIL](https://pypi.org/project/Pillow/) - Image processing library
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - Database library

## Author
- **Hassan Farid** - [Hassan-Farid](https://github.com/Hassan-Farid)
