import os

from fastapi import FastAPI

from app.service import DATASETS, dataset_summary


app = FastAPI(title="Pipeline Metrics API")


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "environment": os.getenv("APP_ENV", "local"),
        "product_name": os.getenv("PRODUCT_NAME", "pipeline-metrics-api"),
        "product_version": os.getenv("PRODUCT_VERSION", "unknown"),
    }


@app.get("/datasets")
def list_datasets() -> dict:
    return {"items": DATASETS}


@app.get("/summary")
def summary() -> dict:
    return dataset_summary()
