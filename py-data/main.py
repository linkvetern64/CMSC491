# @author Joshua Standiford, Daniel Kelly, Malik Jackson
# @description
# This file is the main file to be ran for the data analytics.
# Once the data is finished processing and running the web-interface
# will be called and the data will be loaded.

#Imports
import webbrowser, os.path
from WebLoader import open_url
from AddressParser import GeoCoords

def main():
    url = "crime-data.dev"
    data_path = "../data/"
    data_files = ["rape-csv.csv", "homicide-csv.csv", "larceny-csv.csv"]
    path = "../web_interface/web/view/data/{{{DATAFILE NAME}}}"

    #Testing LatLong function
    #GeoCoords("561 Light St Baltimore MD")

    for data_file in data_files:
        file = open(data_path + data_file)
        for line in file:
            print("")
            #line below prints the date from the CSV
            #print(line.split(',')[0])

        file.close()

    #Check if file exists, if it does load web-interface for visualization
    if(os.path.exists(path)):
        open_url(url, 'chrome')

if __name__ == "__main__":
    main()