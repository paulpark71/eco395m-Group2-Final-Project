import pandas as pd
import requests
import json
import time

"""
    Input: query and the key of Google Map API
    Output: dataset
"""


def get_information_map(query, key):
    df_temp = pd.DataFrame(
        {
            "name": [],
            "address": [],
            "lat": [],
            "lng": [],
            "place_id": [],
            "rating": [],
            "rating_total": [],
        }
    )
    get_next_token = ""
    print("Set up... Please wait for 300 seconds")
    for search_num in range(3):

        if search_num == 0:
            params = {
                "query": query,
                "key": key,
                "language": "en",
            }

        else:
            params = {
                "query": query,
                "key": key,
                "language": "en",
                "pagetoken": get_next_token,
            }
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        res = requests.get(url, params=params)
        get_place = json.loads(res.text)
        if search_num == 2:
            get_next_token = ""
        else:
            get_next_token = get_place["next_page_token"]

        for e in range(len(get_place["results"])):
            df_temp = df_temp.append(
                {
                    "place_id": get_place["results"][e]["place_id"],
                    "name": get_place["results"][e]["name"],
                    "address": get_place["results"][e]["formatted_address"],
                    "lat": get_place["results"][e]["geometry"]["location"]["lat"],
                    "lng": get_place["results"][e]["geometry"]["location"]["lng"],
                    "rating": get_place["results"][e]["rating"],
                    "rating_total": get_place["results"][e]["user_ratings_total"],
                },
                ignore_index=True,
            )

        for i in range(100):
            print(f" \r\033[K#{i+1+100*(search_num)}/{(3*100)}", end="")
            time.sleep(0.1)
    df_temp["zipcode"] = df_temp["address"].str.extract(r"(\d{5})")
    return df_temp
