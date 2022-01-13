## matatika-dataset-to-html

Converts a matatika dataset (yaml) file into a html chart.

Currently requires:
- `matatika`
- `matatika-iplotter`
- `bios`

### Current Use

This script is used in out dataset pipelines to create `html` files containing interative versions of our dataset charts.

You can also use this script locally but invoking `make datasets` in any of our `analyze-{datasource-name}` directories. (There is a make file that uses this script, and there is `rawData` for the datasets to use when converted in each of the `analyze-{datasource-name}` repos.)

### How It Works

invoke the script by using the following:

`python matatika_dataset_to_html.py --d <path_to_datasets> --r <path_to_rawdata>`

`<path_to_datasets>` is always required
`<path_to_rawdata>` is optional, but your datasets need rawdata either from an external path or inside the dataset for the html conversion to display anything.

If you do not supply rawdata either inside the dataset or in another directory you specify inline, you will get a message printed out that the selected dataset has no rawdata and nothing will be converted. This means if there are some datasets to convert with rawdata and others without, it will print a message about some datasets not having any rawdata, but still convert those that do.

#### Running the script yourself

This script looks for all `.yml` or `.yaml` files in the target directory and loops through them.

It attempts to find an rawdata file in a `path_to_rawdata` target directory. (These rawdata directories are included in each of our `analyze-{datasource-name}` repos). If you are converting your own datasets to `.html` files, you will need to provide the `rawData` yourself. 

Putting your `rawData` within the dataset will be the easiest way to achieve this, for more information about our dataset files check out our [dataset documentaion](https://www.matatika.com/docs/data-visualisation/dataset-yaml) or you can see examples datasets with raw data in our [examples repository](https://github.com/Matatika/matatika-examples/tree/master/example_datasets). You can also checkout out any of the `rawdata` file in the top levels of our `analyze-{datasource-name}` repos.

The script will then add the `rawData` to the loaded `.yml` or `.yaml` (or default back to using the `rawData` included in the dataset file), then convert that loaded dataset file into a Matatika dataset object.

The script will then take the newly created dataset object and convert into a `.html` file containing the chart with the datasets filename. 

The output `.html` file will be place in the following location: `./html_charts/{dataset_filename}.html`

#### `make datasets`

By invoking this script through the `Makefile` in any of our `analyze-{datasouce-name}` repositories, the `rawData` you need to have a `.html` chart file that displays something is already included. 

In each of the `analyze-{datasource-name}` repos there is a `rawdata` directory that is used for this, and the output `.html` files will be placed by deafult inside `bundle/analyze/datasets/html_charts/`.
