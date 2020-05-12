import json as _json
import datetime as _datetime

def parse_timestamp(dataset, time_format="%Y-%m-%dT%H:%M:%S.000Z"):
    for d in dataset:
        d["timestamp"] = _datetime.datetime.strptime(d["timestamp"], time_format)
    return dataset
def load_json(filename, time_format="%Y-%m-%dT%H:%M:%S.000Z"):
    dictionary = dict()
    with open(filename) as f:
        dictionary = _json.load(f)
    return parse_timestamp(dictionary, time_format)

def generate_config(dataset):
    start_idx = 0
    end_idx = len(dataset) - 1
    
    return { 
        "test_start": dataset[start_idx]["timestamp"],
        "test_end": dataset[end_idx]["timestamp"]
    }
