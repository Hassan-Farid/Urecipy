# Urecipy - Personal Recipe Notebook

Urecipy is a web application that allows users to view, add, and remove their personal recipes. Built using the [Streamlit](https://streamlit.io/) framework and python, it provides an easy-to-use interface for users to manage their recipe collection.

The application utilizes a SQLite database for storage and retrieval of recipes, and has the following features:
- View all recipes
- Add new recipes
- Remove existing recipes
- Text-to-speech audio for the ingredients and procedure of a recipe
- View and listen to the recipe's audio

graph TB
    subgraph "Legend"
        L1[Frontend Component]:::frontend
        L2[Application Component]:::application
        L3[(Database)]:::database
        L4[Storage Component]:::storage
        L5[External Service]:::external
    end

    subgraph "Frontend Layer"
        Browser["Web Browser"]:::frontend
        Templates["Templates"]:::frontend
        HomeTemplate["home.html"]:::frontend
        RecipeTemplate["recipe.html"]:::frontend
    end

    subgraph "Application Layer"
        Flask["Flask App"]:::application
        DBOps["Database Operations"]:::application
        Utils["Utility Functions"]:::application
    end

    subgraph "Storage Layer"
        DB[(SQLite Database)]:::database
        AudioStorage["Audio Storage"]:::storage
    end

    subgraph "External Services"
        gTTS["Google TTS API"]:::external
    end

    Browser --> Templates
    Templates --> HomeTemplate
    Templates --> RecipeTemplate
    HomeTemplate --> Flask
    RecipeTemplate --> Flask
    Flask --> DBOps
    Flask --> Utils
    DBOps --> DB
    Utils --> AudioStorage
    Utils --> gTTS
    gTTS --> AudioStorage

    classDef frontend fill:#3498db,stroke:#2980b9,color:white
    classDef application fill:#2ecc71,stroke:#27ae60,color:white
    classDef database fill:#f1c40f,stroke:#f39c12,color:black
    classDef storage fill:#9b59b6,stroke:#8e44ad,color:white
    classDef external fill:#e67e22,stroke:#d35400,color:white

    click Templates "https://github.com/Hassan-Farid/Urecipy/tree/master/templates"
    click HomeTemplate "https://github.com/Hassan-Farid/Urecipy/blob/master/templates/home.html"
    click RecipeTemplate "https://github.com/Hassan-Farid/Urecipy/blob/master/templates/recipe.html"
    click Flask "https://github.com/Hassan-Farid/Urecipy/blob/master/app.py"
    click DBOps "https://github.com/Hassan-Farid/Urecipy/blob/master/db_ops.py"
    click Utils "https://github.com/Hassan-Farid/Urecipy/blob/master/utils.py"
    click DB "https://github.com/Hassan-Farid/Urecipy/blob/master/data.db"
    click AudioStorage "https://github.com/Hassan-Farid/Urecipy/tree/master/audios"

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

