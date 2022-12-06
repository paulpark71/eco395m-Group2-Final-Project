import pandas as pd
import os

from .functions.get_information_map import get_information_map
from .functions.detail import detail

query = "gym near Travis County, TX"
key = "AIzaSyCebdSDtlBnNy38SGG2G8lXD1VNycLP5aQ"
BASE_DIR = "artifacts"


"""
    1. Get Information from Google MAP API
"""
df = pd.DataFrame(
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
df.set_index("place_id")

df = get_information_map(query, key)

os.makedirs(os.path.join(BASE_DIR, "store"), exist_ok=True)
ID_CSV_PATH = os.path.join(BASE_DIR, "store", "result_place_id.csv")
os.makedirs(BASE_DIR, exist_ok=True)
with open(
    ID_CSV_PATH, mode="w", newline="", encoding="shift-jis", errors="ignore"
) as f:
    df.to_csv(f, index=False)

"""
    2. Get Each Detailed Information from Google API
"""
dd = pd.DataFrame({"place_id": [], "weekday": [], "Total Business Hour": []})
dd.set_index("place_id", inplace=True)

for e in df["place_id"]:
    dd_temp = detail(e, key)
    dd = dd.append(dd_temp, ignore_index=True)

Detail_CSV_PATH = os.path.join(BASE_DIR, "store", "result_detail.csv")
with open(
    Detail_CSV_PATH, mode="w", newline="", encoding="shift-jis", errors="ignore"
) as f:
    dd.to_csv(f, index=False)

"""
    3. Integration between 1.2. output files
"""

ID_CSV_PATH = os.path.join(BASE_DIR, "store", "result_place_id.csv")
Integrated_CSV_PATH = os.path.join(BASE_DIR, "store", "basic.csv")

id_data = pd.read_csv(ID_CSV_PATH, index_col="place_id")
detail_data = pd.read_csv(Detail_CSV_PATH, index_col="place_id")
integrated_data = id_data.join([detail_data])

integrated_data.to_csv(Integrated_CSV_PATH, header=True)
