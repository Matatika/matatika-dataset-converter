"""Module for converting export datasets into markdown"""
import click
from mdutils import MdUtils


def convert_export_dataset(dataset_dict, yaml_file_name, output_dir_path):
    new_file_name = yaml_file_name.title().replace("-", "_")
    mdFile = MdUtils(file_name=str(output_dir_path.joinpath(new_file_name)))
    try:
        description = dataset_dict["description"].split("#")
        description = description[0].strip()
    except:
        description = dataset_dict["description"]
    index = description.find("![Export]")
    description_part_one = description[:index]
    description_part_two = description[
        description.find("List of columns in this export") :
    ]
    mdFile.new_header(level=1, title=dataset_dict["questions"])
    mdFile.write(description_part_one)
    mdFile.new_paragraph()
    mdFile.write(description_part_two)
    mdFile.create_md_file()

    click.secho(f"Converted {yaml_file_name}", fg="green")
