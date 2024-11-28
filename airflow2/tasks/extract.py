import pandas as pd

def from_csv(**kwargs):
    file_path = kwargs["params"]["file_path"]
    df = pd.read_csv(file_path)
    output_path = "data/extracted_data.csv" 
    df.to_csv(output_path, index=False)

def from_json(**kwargs):
    file_path = kwargs["params"]["file_path"]
    df = pd.read_json(file_path)
    output_path = "data/extracted_data.csv"
    df.to_csv(output_path, index=False)

def choose_extraction(**kwargs):
    extract_type = kwargs["params"].get("extract_type")
    if extract_type == "csv":
        return "extract_from_csv"
    elif extract_type == "json":
        return "extract_from_json"
    else:
        raise ValueError("Jenis extract_type tidak valid!")