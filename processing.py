import json
import logging
import math
import time

results = []

def append_records(filename, points):
    results.append({
        "filename": filename,
        "dateProcessed": str(math.floor(time.time() * 1000)),
        "points": points
    })

def get_records():
    return results

def process_output(data, format_type):
    if format_type == "json":
        json_data = {
            "items": []
        }
        
        for d in data:
            logging.debug(d)
            points = d["points"].split('\n')
            
            item_data = {
                "filename": d["filename"],
                "dateProcessed": d["dateProcessed"],
                "points": []
            }

            for p in points:
                item_data["points"].append(p)
            
            json_data["items"].append(item_data)
        
        return json.dumps(json_data)
    
    elif format_type == "text":
        output = ""

        for d in data:
            output += "> " + d["filename"] + "\n\n"
            output += d["points"] + "\n\n\n"

        return output