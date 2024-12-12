import os
from pathlib import Path


import logging

logging.basicConfig(level=logging.INFO) ##logging information



##define project 

project_name= "cnnClassifier"


###list of files

list_of_files = [
    ".github/workflows/.gitkeep",          #.github/workflows/.gitkeep is to ensure that the workflows directory is included in your Git repository, even if it is initially empty. Git does not track empty directories, so this placeholder file ensures the directory is present in the repository structure. 
    f"src/{project_name}/__init__.py", ##constructor file -because this use local ,not python intrepreter
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
      f"src/{project_name}/constants/__init__.py",
      "config/config.yaml",
      "dvc.yaml",
      "params.yaml",
      "requirements.txt",
      "setup.py",
      "research/trails.ipynb", ###notebook experiment
   
]



for filepath in list_of_files:
    filepath = Path(filepath)  #PATH =-------- EVERY FILE SRC IN FORWARD SLASH '/ ' BUT WINDOWS ACTUAL USE BACKWARD SLASH'\'  SHOW SOME ERROR   ##FILE PATH TO WINDOWS PATH

    ##seperate folder and file name

    filedir , filename = os.path.split(filepath)

    #create directory

    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"create directory; {filedir}  for the file: {filename}") 




    ##after creating dirctory to also need to create files

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")


    else:
         logging.info(f"{filename} is already  exist!!!")       


         