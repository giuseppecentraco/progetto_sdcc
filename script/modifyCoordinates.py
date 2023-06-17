
import numpy as np
import random
import json
import os

import points as points
from shapely.geometry import Polygon, Point

def randomPointGenerator (poly):

    min_x, min_y, max_x, max_y = poly.bounds

    flag = True
    point = Point([0,0])

    while flag:
        point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if point.within(poly):
            flag = False

    return point


def pointToDictionary(point):

    geo_point = {
        "lat": point.x,
        "lon": point.y
    }

    return geo_point

def get():

	poly = Polygon([(48.15166836057548, -124.58903083449438),
                    (48.65216753389164, -95.25936768004513),
                    (45.23353305229313, -89.50253174254513),
                    (41.39867609503304, -83.30624268004513),
                    (44.7362220690925, -70.21053955504513),
                    (30.880317812873436, -81.64807662791249),
                    (26.311212460510912, -80.12504589057635 ),
                    (25.163254748225288, -80.56449901557635 ),
                    (30.782162613334748, -83.68605587893336 ),
                    (30.360896401726905, -104.12206586729037),
                    (32.4609814623837, -108.91210492979037  ),
                    (33.12592490726583, -116.99804242979037 ),
                    (39.357545183181486, -123.67772992979037)])

	p = randomPointGenerator(poly)
	return pointToDictionary(p)


def updateCoordinates(file, file_path, destination_path):

    source_file = open(file_path, 'r')  # viene aperto il file con il permesso di lettura
    lines = source_file.readlines()  # restituisce una lista contenente le linee del file
    destination_file = open(destination_path + "/[formattato]" + file, 'w') # file creato vuoto

    for i in range(len(lines)):
        j=json.loads(lines[i][:-1])
        j["coordinates"] = get()
        tmp=json.dumps(j)
        destination_file.write(tmp)
        destination_file.write(",\n")


def main():

    folder_source = input("Inserisci il path della cartella con i json dei quali modificare le coordinate: ")
    folder_destination = input("Inserisci il path della cartella in cui memorizzare i file modificati: ")

    file_list = os.listdir(folder_source)

    for file in file_list:
        file_path = folder_source + "/" + file
        updateCoordinates(file, file_path, folder_destination)
        print("Coordinate " + file + " modificate")


main()