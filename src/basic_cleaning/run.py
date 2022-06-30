#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    logger.info("Downloading the dataset from W&B")
    local_path = run.use_artifact(args.input_artifact).file()
    
    logger.info("Reading the dataset")
    df = pd.read_csv(local_path)
    
    logger.info("Cleaning the data")
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()
    # Convert last_review to datetime
    df['last_review'] = pd.to_datetime(df['last_review'])
    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()
    
    logger.info("Saving cleaned dataset")
    df.to_csv("clean_sample.csv", index=False)
    
    logger.info("Initialize output artifact")
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    
    logger.info("Adding file to artifact and logging artifact to run")
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)
    
    run.finish()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type= str,
        help= "Fully-qualified name for the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name for output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="type of output artifact",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="description of output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="maximum price",
        required=True
    )


    args = parser.parse_args()

    go(args)
