# @author Joshua Standiford, Daniel Kelly, Malik Jackson
# @description
# This file is the main file to be ran for the data analytics.
# Once the data is finished processing and running the web-interface
# will be called and the data will be loaded.

#Imports
import webbrowser, os.path
from WebLoader import open_url
from AddressParser import GeoCoords

#Gets all .csv files from data directory
def getDataFiles():
    files = []
    for file in os.listdir("../data"):
        if file.endswith(".csv"):
            files.append(file)
    return files

#
#
def main():
    url = "crime-data.dev"
    data_path = "../data/"
    path = "../web_interface/web/view/data/{{{DATAFILE NAME}}}"
    data_files = getDataFiles()

    #Select singular file for testing
    data_files = ['rape-csv.csv']
    state = "MD"
    target = 0

    #Date, Code, Address, Crime, Weapon, District, Neighborhood

    #Displays information within all the data files
    for data_file in data_files:
        file = open(data_path + data_file)
        index = 0
        for line in file:
            if index < target:
                index += 1
                continue
            #line below prints the date from the CSV
            data = line.split(',')
            try:
                GeoCoords(data[2] + " " + state)
            except:
                print("Died at :")
                print(index)
            index += 1

        file.close()

    #Check if file exists, if it does load web-interface for visualization
    if(os.path.exists(path)):
        open_url(url, 'chrome')
    #else:
        #raise BaseException('Cannot find produced DATA file')

if __name__ == "__main__":
    main()