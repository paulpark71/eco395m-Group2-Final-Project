import json
import requests
from .calculate_hour import calculate_hour


def detail(id, key):
    """
    Input: Google Map place_id and key
    Output: detailed data by each places
    """
    params = {
        "key": key,
        "place_id": id,
        "language": "en",
    }
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    res = requests.get(url, params=params)
    get_detail = json.loads(res.text)

    dd_temp = {
        "place_id": id,
        "weekday": get_detail["result"]["current_opening_hours"]["weekday_text"],
        "Total Business Hour": calculate_hour(
            get_detail["result"]["current_opening_hours"]["weekday_text"]
        ),
    }
    return dd_temp
