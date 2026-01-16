# This will convert the texture ATLAS xml files to readable YOLO format textures labels

import xml.etree.ElementTree as etree
from pathlib import Path

iteration = 0  # Iteration is a count of how many sprites have been processed

print(
    "So uh yeah put all the files you want to convert in a subdirectory called 'xml_unformatted'"
)
xml_files = Path("training_yolo/xml_unformatted/")
files = [
    file
    for file in sorted(
        xml_files.iterdir()
    )  # Currently glorping to whoever made sorted() :3
    if file.is_file() and file.suffix == ".xml"
]  # Goes through everything in the subdirectory and if it is a file, adds it to da list


def write_data(data_to_write, file_path: Path):
    for sprite in data_to_write:
        with file_path.open("a") as f:  # DON'T OUTPUT IN PROCESS
            f.write(sprite)


def process_files(xml_file: Path, iteration):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    print(root)
    sprite_classes: list[str] = []

    # Sorry for poor naming, this just takes a string that COULD be none and tells the interpreter/linter that it is not None and converts it to int
    def str_to_int(
        input,
    ):  # This is to make sure that we don't fetch and invalid data from the ATLAS
        value = input

        if value is None:
            raise ValueError(
                "Uhm... hey dummy, you formatted your xml file wrong and it's missing a few attributes"
            )
        return int(value)

    text_atlas = root
    if text_atlas is not None:
        IMG_W = str_to_int(text_atlas.get("width"))
        IMG_H = str_to_int(text_atlas.get("height"))
    else:
        raise ValueError("Yo, the xml file doesn't have a TextureAtlas header")

    output_path = (Path("training_yolo/labels/train") / xml_file.stem).with_suffix(
        ".txt"
    )
    # labels/gui_2x (not labels/gui_2x.xml)
    output_path.touch()

    # This is where we actually process our sprite
    for sprite in root.findall("sprite"):  # It only found one sprite for some reason...
        name = sprite.get("n")
        # Truly disgusting to look at
        x = str_to_int(sprite.get("x"))
        y = str_to_int(sprite.get("y"))
        w = str_to_int(sprite.get("w"))
        h = str_to_int(sprite.get("h"))
        ox: str | None = sprite.get("oX")
        oy: str | None = sprite.get("oY")
        oW: str | None = sprite.get("oW")
        oH: str | None = sprite.get("oH")

        cen_x = (
            x + int(ox) + (w / 2) if ox is not None and oy is not None else x + w / 2
        )
        cen_y = (
            y + int(oy) + (h / 2) if ox is not None and oy is not None else y + h / 2
        )

        sprite_class = f"{iteration} {cen_x / IMG_W:.6f} {cen_y / IMG_H:.6f} {w / IMG_W:.6f} {h / IMG_H:.6f}"  # This is the YOLO verified class
        sprite_classes.append(sprite_class + "\n")

        iteration += 1
    print(sprite_classes)
    return iteration, sprite_classes, output_path


for file in files:
    iteration, sprite, file_to_write_to = process_files(file, iteration)
    write_data(sprite, file_to_write_to)
