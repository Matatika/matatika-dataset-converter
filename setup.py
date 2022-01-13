from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="matatika-convert",
    version="0.1.0",
    description="A Matatika utility to convert datasets.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        convert=matatika_dataset_converter.cli.commands.root:convert
    """,
    license="MIT",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
