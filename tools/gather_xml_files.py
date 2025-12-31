# I am soooo lazy that Imma automate gathering xml files :pppp
from pathlib import Path
import shutil

xml_files = Path("../assets")
output_path = Path("../training_yolo/xml_unformatted/")

files = [
    file for file in xml_files.iterdir() if file.is_file() and file.suffix == ".xml"
]  # Goes through everything in the subdirectory and if it is a file, adds it to da list


# print(files)

for file in files:
    dest_file = output_path / file.name
    shutil.copy2(file, dest_file)
