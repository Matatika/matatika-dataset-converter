"""Module for converting chartjs datasets into html files"""

import os
import json

import bios
import click
from matatika_dataset_converter.utils import clean_up_md_whitespace
from matatika import chartjs
from iplotter import ChartJSPlotter
from mdutils import MdUtils


def save_converted_chartjs_chart(
    plotter, my_dataset_chart, yaml_file_name, output_path
):
    yaml_file_name = yaml_file_name.title().replace("-", "_")
    plotter.save(
        **my_dataset_chart,
        filename=str(output_path.joinpath(yaml_file_name)),
        keep_html=True,
    )
    return yaml_file_name


def create_html_chart_include_string(file_name):
    include_string = r"{% include "
    include_string = include_string + f"{file_name}.html "
    include_string = include_string + r"%}"
    return include_string


def create_md_snippet(dataset_dict, file_name, output_dir_path):
    new_file_name = file_name.title().replace("-", "_")
    mdFile = MdUtils(file_name=str(output_dir_path.joinpath(new_file_name)))
    try:
        description = dataset_dict["description"].split("#")
        description = description[0].strip()
    except:
        description = dataset_dict["description"]
    mdFile.new_header(level=1, title=dataset_dict["questions"])
    mdFile.write(description)
    mdFile.new_paragraph()
    include_snippet_string = create_html_chart_include_string(file_name)
    mdFile.write(include_snippet_string)
    mdFile.create_md_file()

    clean_up_md_whitespace(str(output_dir_path.joinpath(new_file_name)))

    click.secho(f"Converted {file_name}", fg="green")


def convert_chartjs_dataset(
    dataset, dataset_dict, file_name, rawdata_path, output_path
):
    plotter = ChartJSPlotter()

    rawdata_file_list = os.listdir(rawdata_path)

    rawdata_file_list_trimmed = [os.path.splitext(fn)[0] for fn in rawdata_file_list]

    if file_name in rawdata_file_list_trimmed:
        imported_rawdata_file = bios.read(
            str(rawdata_path.joinpath(file_name + ".yml"))
        )
        my_dataset_chart = chartjs.to_chart(
            dataset,
            json.loads(imported_rawdata_file[file_name]),
        )
    else:
        try:
            my_dataset_chart = chartjs.to_chart(dataset, json.loads(dataset.raw_data))
        except:
            click.secho(f"No raw data found for dataset {file_name}", fg="red")
            return

    try:
        html_file_name = save_converted_chartjs_chart(
            plotter, my_dataset_chart, file_name, output_path
        )
        click.secho(f"Converted {file_name}")
    except:
        click.secho(f"Error converting {file_name}", fg="red")
        return

    create_md_snippet(dataset_dict, html_file_name, output_path)
