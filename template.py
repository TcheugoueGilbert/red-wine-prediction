import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "winequality"



list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]



for filepath in list_of_files:
    filepath = Path(filepath)       # Convert to Path object for better path handling

    filedir, filename = os.path.split(filepath)    # Split into directory and filename

    if filedir !="":  # Check if directory is not empty
        os.makedirs(filedir, exist_ok=True) # Create directory if it doesn't exist  
        logging.info(f"Creating directory; {filedir} for the file: {filename}")   

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):   # Check if file does not exist or is empty
        with open(filepath, "w") as f:   # Open file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}")  


    else:
        logging.info(f"{filename} is already exists") 