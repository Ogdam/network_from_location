import pyproj
import requests
import pandas as pd

API_GOUV = "https://api-adresse.data.gouv.fr/search/"
data_csv = pd.read_csv('2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv', sep=';')
operators = {
    20801 : 'Orange', 
    20810 : 'SFR', 
    20815 : 'Free', 
    20820 : 'Bouygue'
}

def lamber93_to_gps(x, y):
	lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
	wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
	long, lat = pyproj.transform(lambert, wgs84, x, y)
	return long, lat

def get_legal_projection_coordinates(address :str) -> tuple:
    r = requests.get(API_GOUV, params={
        "q" : address,
        "limit" : 1
    })
    if r.status_code != 200 :
        return None
    json_data = r.json()
    return json_data['features'][0]['properties']['x'], json_data['features'][0]['properties']['y']

def search_all_nearest_network(x: int, y: int) -> pd.DataFrame :
    results = data_csv[(data_csv.y.isin(range(y-1000, y+1000)) & data_csv.x.isin(range(x-1000, x+1000)))]
    return results

def format_network_response(data : pd.DataFrame) -> dict:
    response = {}
    data = data.groupby(by=["Operateur"])
    for name, group in data :
        network = {"2G": False, "3G": False, "4G": False}
        for _, row in group.iterrows(): 
            for key in network.keys():
                network[key] = True if row[key] == 1.0 else  network[key]
        response[operators[name[0]]] = network
    return response