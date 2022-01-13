"""CLI entrypoint 'matatika_convert' command"""

import click

from matatika_dataset_converter.utils import make_dir_path_absolute
from matatika_dataset_converter.convert import convert_all


@click.command()
@click.argument(
    "dataset_dir_path",
    default=None,
)
@click.argument(
    "rawdata_dir_path",
    default=None,
)
@click.argument("output_dir_path", default=None)
def convert(dataset_dir_path, rawdata_dir_path, output_dir_path):
    """CLI entrypoint and base command"""

    dataset_dir_path = make_dir_path_absolute(dataset_dir_path)
    rawdata_dir_path = make_dir_path_absolute(rawdata_dir_path)
    output_dir_path = make_dir_path_absolute(output_dir_path)
    convert_all(dataset_dir_path, rawdata_dir_path, output_dir_path)
