# Mini-Codes
This repository created for save mini codes that maybe we need

import csv
from tqdm import tqdm
import requests


def listDownloader ( fileDir , saveDir , name , type="mp4" ):

    # ====================================================
    with open( f'{fileDir}' , 'r') as read_obj:

        csv_reader = csv.reader(read_obj)

        list_of_csv = list(csv_reader)

        read_obj.close()

    links = []

    for i in list_of_csv :

        for j in i :

            links.append(j)

    # ====================================================

    for i in tqdm(range(len(links))):

        url = links[i]

        def download_file(url,filename):

            r = requests.get(url, stream=True)

            with open(filename, 'wb') as f:

                for chunk in r.iter_content(chunk_size=1024):

                    if chunk:

                        f.write(chunk)

            return filename

        download_file(url, f"{saveDir}/{name} ({i+1}).{type}" )
