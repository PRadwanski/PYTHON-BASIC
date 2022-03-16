import json, xml, os
import xml.etree.ElementTree as ET
from numpy import mean


'''
Code to create XML file.

'''


# Function to get all attributes
def wrap_up(temp, wind):
    temp_mean = round(mean(temp),2)
    wind_mean = round(mean(wind),2)
    temp_min = min(temp)
    wind_min = min(wind)
    temp_max = max(temp)
    wind_max = max(wind)

    dict_to_dump = {'temp_mean':str(temp_mean), "wind_mean":str(wind_mean),
                     "temp_min":str(temp_min), "wind_min":str(wind_min),
                    "temp_max":str(temp_max), "wind_max":str(wind_max)}

    return dict_to_dump


def summary(spain_temp, spain_wind):
    mean_temp = round(mean(spain_temp))
    mean_wind = round(mean(spain_wind))

    return {"mean_temp":str(mean_temp), "mean_wind":str(mean_wind)}


# Assign variables for iteration through folders.
# folders contains list of all cities
# base_path will be used as an interator with .format() method
# json path points to file where data will be saved
folders = os.listdir("tasks_5/cities")
base_path = "/Users/pradwanski/Desktop/Python/tasks_5/cities/{}/2021_09_25.json"
xml_path = "/Users/pradwanski/Desktop/Python/tasks_5/xml_file.xml"
spain_temp = []
spain_wind = []
# Set etree root for xml file
# Add subelement cities. Later during iteration it will create new subelements in the run.
root = ET.Element('weather')
root.set('county','Spain')
root.set('date', "2021-09-25")
element1 = ET.SubElement(root,"cities")


# First "for" loop to go collect data from each folder.
# if statement used to skip hidden files in folder.
for city in folders:
    if city[0] == ".":
        continue

    with open(base_path.format(city), "r") as f:
        data = json.load(f)
        f.close()
    
    # This part of code will iterate through the data from json file -
    # and append temp, wind speed values into 2 lists.
    temp = []
    wind = []
    for i in range(0,23):
        temp.append(data['hourly'][i]['temp'])
        wind.append(data['hourly'][i]['wind_speed'])

        # Also append to global variables for global mean
        spain_temp.append(data['hourly'][i]['temp'])
        spain_wind.append(data['hourly'][i]['wind_speed'])
        

    # Earlier predefined functions to grab 'temp' and 'wind' lists and arange it into
    # Dictionary with mean, min, max values
    # Then add SubElement with City
    numbers = wrap_up(temp, wind)
    ET.SubElement(element1, city.replace(' ','-'), numbers)

    
# Add summary
summary_dict = summary(spain_temp, spain_wind)
ET.SubElement(root, "summary", summary_dict)

b_xml = ET.tostring(root)
b_xml

# Dump the data into a json file.
with open(xml_path, "wb") as f:
    f.write(b_xml)
    f.close()
    
    
    
    
'''

Code to create JSON file

'''



# Function to get all attributes
def wrap_up(temp, wind):
    temp_mean = round(mean(temp),2)
    wind_mean = round(mean(wind),2)
    temp_min = min(temp)
    wind_min = min(wind)
    temp_max = max(temp)
    wind_max = max(wind)

    return temp_mean, wind_mean, temp_min, wind_min, temp_max, wind_max


# Function just for json test file
# This creates a dict from a given numbers and town name
def dic_to_json(numbers, town):

    my_dict = {"mean_temp":numbers[0], "mean_wind_speed":numbers[1], "min_temp":numbers[2],
        "min_wind_speed":numbers[3], "max_temp":numbers[4], "max_wind_speed":numbers[5]}

    return {town:my_dict}





# Assign variables for iteration through folders.
# folders contains list of all cities
# base_path will be used as an interator with .format() method
# json path points to file where data will be saved
folders = os.listdir("tasks_5/cities")
base_path = "/Users/pradwanski/Desktop/Python/tasks_5/cities/{}/2021_09_25.json"
json_path = "/Users/pradwanski/Desktop/Python/tasks_5/json_file.json"


for folder in folders:
    if folder[0] != ".":
        with open(base_path.format(folder), "r") as f:
            data = json.load(f)
            f.close()

    # This part of code will iterate through the data from json file -
    # and append temp, wind speed values into 2 lists.
    temp = []
    wind = []
    for i in range(0,23):
        temp.append(data['hourly'][i]['temp'])
        wind.append(data['hourly'][i]['wind_speed'])

    # Earlier predefined functions to grab 'temp' and 'wind' lists and arange it into
    # Dictionary with mean, min, max values
    numbers = wrap_up(temp, wind)
    to_dump = dic_to_json(numbers, folder)
    
    # Dump the data into a json file.
    with open(json_path, "a") as f:
        json.dump(to_dump,f)
        f.close()


