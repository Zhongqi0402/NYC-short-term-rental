# Build ML Pipeline for Short-Term Rental Prices in NYC
This is for a property management company renting rooms and properties for short periods of 
time on various rental platforms. I estimate the typical price for a given property based 
on the price of similar properties. My company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

# Path to WB and Github
Path to W&B: https://wandb.ai/matt_04/nyc_airbnb?workspace=user-matt_04  
Path to Github: https://github.com/Zhongqi0402/NYC-short-term-rental
## Table of contents

* [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
* [Data cleaning](#data-cleaning)
* [Data testing](#data-testing)
* [Data splitting](#data-splitting)
* [Train Random Forest](#train-random-forest)
* [Optimize hyperparameters](#optimize-hyperparameters)
* [Select the best model](#select-the-best-model)
* [Test](#test)
* [Visualize the pipeline](#visualize-the-pipeline)
* [Release the pipeline](#release-the-pipeline)
* [Train the model on a new data sample](#train-the-model-on-a-new-data-sample)

### Running the entire pipeline or just a selection of steps
In order to run the pipeline
```bash
>  mlflow run .
```
This will run the entire pipeline.

It is useful to be able to run one step at the time. Say you want to run only
the ``download`` step. The `main.py` is written so that the steps are defined at the top of the file, in the 
``_steps`` list, and can be selected by using the `steps` parameter on the command line:

```bash
> mlflow run . -P steps=download
```
If you want to run the ``download`` and the ``basic_cleaning`` steps, you can similarly do:
```bash
> mlflow run . -P steps=download,basic_cleaning
```
You can override any other parameter in the configuration file using the Hydra syntax, by
providing it as a ``hydra_options`` parameter. For example, say that we want to set the parameter
modeling -> random_forest -> n_estimators to 10 and etl->min_price to 50:

```bash
> mlflow run . \
  -P steps=download,basic_cleaning \
  -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"
```


## Overview

### Exploratory Data Analysis (EDA)

## Data cleaning

### Data testing

### Data splitting

### Train Random Forest

### Optimize hyperparameters

### Select the best model using W&B

### Test

### Train the model on a new data sample

## License

[License](LICENSE.txt)
