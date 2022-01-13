"""Unittest module for matatika_dataset_to_html"""

import unittest
import os
from pathlib import Path

from click.testing import CliRunner

from matatika_dataset_converter.cli.commands.root import convert


def clean_up_converted_test_files(test_files_path):
    """Cleans up converted html and markdown files in the test_files dir"""
    dir_list = os.listdir(test_files_path)
    for file in dir_list:
        file_path = test_files_path.joinpath(file)
        if os.path.isdir(file_path):
            clean_up_converted_test_files(file_path)
        else:
            if file.endswith(".html") or file.endswith(".md"):
                os.remove(file_path)


class TestDatasetConversion(unittest.TestCase):
    """Unit test class for matatika_dataset_to_html"""

    def setUp(self):

        self.runner = CliRunner()

        self.package_dir = Path(__file__).parent.absolute()
        self.test_files_path = self.chartjs_dataset = self.package_dir.joinpath(
            "test_files/"
        )
        self.chartjs_dataset = self.package_dir.joinpath(
            "test_files/meltano-top-10-jobs-by-runs.yml"
        )
        self.google_table_dataset = self.package_dir.joinpath(
            "test_files/meltano-most-recent-3-failing-jobs.yml"
        )
        self.export_dataset = self.package_dir.joinpath(
            "test_files/meltano-export-daily-jobs-by-job-id.yml"
        )
        self.chartjs_dataset_rawdata = self.package_dir.joinpath(
            "test_files/rawdata/meltano-top-10-jobs-by-runs.yml"
        )

    def tearDown(self):
        # clean_up_converted_test_files(self.test_files_path)
        pass

    def test_convert_chartjs_dataset(self):
        result = self.runner.invoke(
            convert,
            [
                str(self.test_files_path.joinpath("chartjs/")),
                str(self.test_files_path.joinpath("rawdata/")),
                str(self.test_files_path.joinpath("output/")),
            ],
        )

        self.assertIn("Converted", result.output)
        self.assertIs(result.exit_code, 0)
        self.assertTrue(
            self.test_files_path.joinpath(
                "output/Meltano_Top_10_Jobs_By_Runs.html"
            ).is_file()
        )
        self.assertTrue(
            self.test_files_path.joinpath(
                "output/Meltano_Top_10_Jobs_By_Runs.md"
            ).is_file()
        )

    def test_convert_google_table_dataset(self):
        result = self.runner.invoke(
            convert,
            [
                str(self.test_files_path.joinpath("google_table/")),
                str(self.test_files_path.joinpath("rawdata/")),
                str(self.test_files_path.joinpath("output/")),
            ],
        )

        self.assertIn("Converted", result.output)
        self.assertIs(result.exit_code, 0)
        self.assertTrue(
            self.test_files_path.joinpath(
                "output/Meltano_Most_Recent_3_Failing_Jobs.md"
            ).is_file()
        )

    def test_convert_export_dataset(self):
        result = self.runner.invoke(
            convert,
            [
                str(self.test_files_path.joinpath("export/")),
                str(self.test_files_path.joinpath("rawdata/")),
                str(self.test_files_path.joinpath("output/")),
            ],
        )

        self.assertIn("Did not convert", result.output)
        self.assertIs(result.exit_code, 0)

    def test_convert_all(self):
        result = self.runner.invoke(
            convert,
            [
                str(self.test_files_path),
                str(self.test_files_path.joinpath("rawdata/")),
                str(self.test_files_path.joinpath("output/")),
            ],
        )

        self.assertIn("Converted", result.output)
        self.assertIn("Did not convert", result.output)
        self.assertIs(result.exit_code, 0)
        self.assertTrue(
            self.test_files_path.joinpath(
                "output/Meltano_Most_Recent_3_Failing_Jobs.md"
            ).is_file()
        )
        self.assertTrue(
            self.test_files_path.joinpath(
                "output/Meltano_Top_10_Jobs_By_Runs.html"
            ).is_file()
        )
