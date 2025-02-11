import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format = '[%(asctime)s] : %(message)s:'
)

project_name = 'CNNClassifier'

file_list = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/config/configuration.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
]

for file in file_list:
    filepath = Path(file)
    filedir, filename = filepath.parent, filepath.name

    if not filedir.is_dir():
        filedir.mkdir(parents = True, exist_ok=True)
        logging.info(f"Directory {filedir.name} is created")
    else:
        logging.info(f"Directory {filedir.name} already exist")
    
    if not filepath.exists():
        filepath.touch()
        logging.info(f"File {filepath.name} is created")
    else:
        logging.info(f"File {filepath.name} already exist")