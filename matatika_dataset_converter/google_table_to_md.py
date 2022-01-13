"""Module for converting google table datasets to markdown"""
import json
import click
from mdutils import MdUtils

from matatika_dataset_converter.utils import clean_up_md_whitespace


def convert_google_table_dataset(dataset_dict, yaml_file_name, output_path):
    new_file_name = yaml_file_name.title().replace("-", "_")
    mdFile = MdUtils(file_name=str(output_path.joinpath(new_file_name)))
    try:
        description = dataset_dict["description"].split("#")
        description = description[0].strip()
    except:
        description = dataset_dict["description"]
    mdFile.write("## " + dataset_dict["title"])
    mdFile.new_paragraph()
    mdFile.write("### " + dataset_dict["questions"])
    mdFile.new_paragraph()
    mdFile.write(description)
    column_names = []
    my_dict = json.loads(dataset_dict["metadata"])
    for item in my_dict["related_table"]["columns"]:
        column_names.append(item["description"])
    mdFile.new_paragraph()
    mdFile.write("Columns displayed in dataset table:")
    mdFile.new_list(column_names)
    mdFile.write("\n")
    mdFile.write("---")
    mdFile.create_md_file()

    clean_up_md_whitespace(str(output_path.joinpath(new_file_name)))

    click.secho(f"Converted {yaml_file_name}", fg="green")
