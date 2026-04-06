from statistics import mean


DATASETS = [
    {"name": "orders", "records": 12450, "fresh_hours": 2, "quality_score": 0.98},
    {"name": "customers", "records": 4200, "fresh_hours": 1, "quality_score": 0.99},
    {"name": "inventory", "records": 860, "fresh_hours": 9, "quality_score": 0.93},
]


def dataset_summary() -> dict:
    stale_threshold_hours = 6
    stale = [item for item in DATASETS if item["fresh_hours"] > stale_threshold_hours]
    return {
        "total_datasets": len(DATASETS),
        "total_records": sum(item["records"] for item in DATASETS),
        "stale_datasets": len(stale),
        "average_quality_score": round(mean(item["quality_score"] for item in DATASETS), 3),
    }
