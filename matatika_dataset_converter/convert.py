"""Module to handle over running of dataset conversions"""


import bios
import click

from pathlib import Path

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

from matatika_dataset_converter.export_to_md import convert_export_dataset
from matatika_dataset_converter.google_table_to_md import convert_google_table_dataset
from matatika_dataset_converter.chartjs_to_html import convert_chartjs_dataset

plotter = ChartJSPlotter()


def convert_all(dataset_dir_path, rawdata_dir_path, output_dir_path):

    if not output_dir_path.exists():
        output_dir_path.mkdir(parents=True)

    for file in dataset_dir_path.iterdir():
        if file.name.endswith(".yaml") or file.name.endswith(".yml"):

            yaml_dict = bios.read(str(file.absolute()))

            new_dataset = Dataset.from_dict(yaml_dict)

            yaml_file_name = Path(file).stem

            # my_dataset_chart = None

            dataset_dict = new_dataset.to_dict()

            visualisation = dataset_dict.get("visualisation")

            if not visualisation:
                click.secho(f"Did not convert {yaml_file_name}", fg="red")
                continue
            elif "google" or "html-table" in visualisation:
                convert_google_table_dataset(
                    dataset_dict, yaml_file_name, output_dir_path
                )
            elif "chartjs" in visualisation:
                convert_chartjs_dataset(
                    new_dataset,
                    dataset_dict,
                    yaml_file_name,
                    rawdata_dir_path,
                    output_dir_path,
                )
