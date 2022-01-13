## matatika-dataset-converter

Converts a matatika dataset (yaml) file into a markdown file to be used in our [documentation](https://www.matatika.com/docs/).

Currently requires:
- `matatika`
- `matatika-iplotter`
- `bios`
- `mdutils`
- `click`

### Current Use



You can also use this script locally but invoking `make datasets` in any of our `analyze-{datasource-name}` directories. (There is a make file that uses this script, and there is `rawData` for the datasets to use when converted in each of the `analyze-{datasource-name}` repos.)

### How It Works

After pip installing this package you can use:

`convert <path_to_datasets> <path_to_rawdata> <path_to_output_dir>`

All arguments are required.

#### Running the script yourself

This script looks for all `.yml` or `.yaml` files in the target directory and loops through them.

It attempts to find an rawdata file in a `path_to_rawdata` target directory. (These rawdata directories are included in each of our `analyze-{datasource-name}` repos). If you are converting your own datasets to, you will need to provide the `rawData` yourself. 

Putting your `rawData` within the dataset will be the easiest way to achieve this, for more information about our dataset files check out our [dataset documentaion](https://www.matatika.com/docs/data-visualisation/dataset-yaml) or you can see examples datasets with raw data in our [examples repository](https://github.com/Matatika/matatika-examples/tree/master/example_datasets). You can also checkout out any of the `rawdata` file in the top levels of our `analyze-{datasource-name}` repos.

The script will then add the `rawData` to the loaded `.yml` or `.yaml` (or default back to using the `rawData` included in the dataset file), then convert that loaded dataset file into a Matatika dataset object.

The script will then take the newly created dataset object and convert into a `.md` snuppet file containing the any relevent converted charts.  

The output `.md` file will be place in the following location: `./output/{dataset_filename}.md`

#### `make datasets`

By invoking this script through the `Makefile` in any of our `analyze-{datasouce-name}` repositories, the `rawData` you need to have a snippet including a chart file that displays something is already included. 

In each of the `analyze-{datasource-name}` repos there is a `rawdata` directory that is used for this, and the output `.html` files will be placed by deafult inside `bundle/analyze/datasets/output/`, then used in their respective markdown snippet file.
