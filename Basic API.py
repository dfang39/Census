import requests
import os
import openpyxl
import pandas
import Variables

api_key = "0bfe5578f2f3e0f6a2752d4b08bcf6f428db83a5"
zip = ''

variables = ''
variable_array = Variables.children_per_household #Variables.combination

for i in range(0, len(variable_array)):
    variables += "," + str(variable_array[i])

url_string = 'https://api.census.gov/data/2016/acs/acs5?get=NAME' + variables + '&for=county:013&in=state:02&key=' + api_key
print(url_string)

request = requests.get(url_string)

json = request.json()
print(json[1])

# class Area(object):
#     def __init__(self,
#                  name = "",
#                  total_pop = 0,
#                  total_poverty = 0,
#                  poverty_percent = 0,
#                  total_family = 0,
#                  total_family_poverty = 0,
#                  total_single_father = 0,
#                  total_single_mother = 0,
#                  family_poverty_percent = 0,
#                  single_parent_percent = 0,
#                  total_households = 0,
#                  total_public_assist = 0,
#                  public_assist_percent = 0):
#         self.name = name
#         self.total_pop = total_pop
#         self.total_poverty = total_poverty
#         self.poverty_percent = poverty_percent
#         self.total_family = total_family
#         self.total_family_poverty = total_family_poverty
#         self.total_single_father = total_single_father
#         self.total_single_mother = total_single_mother
#         self.family_poverty_percent = family_poverty_percent
#         self.single_parent_percent = single_parent_percent
#         self.total_households = total_households
#         self.total_public_assist = total_public_assist
#         self.public_assist_percent = public_assist_percent
#
# area_objects = []
#
# for i in range(1, len(json)):
#     area_objects.append(Area(name=json[i][0],
#                              total_pop=int(json[i][1]),
#                              total_poverty=int(json[i][2]),
#                              total_family=int(json[i][3]),
#                              total_family_poverty =int(json[i][4]),
#                              total_single_father=int(json[i][5]),
#                              total_single_mother=int(json[i][6]),
#                              total_households=int(json[i][7]),
#                              total_public_assist=int(json[i][8])))
#
#
# for object in area_objects:
#     object.poverty_percent = object.total_poverty/object.total_pop*100
#     object.family_poverty_percent = object.total_family_poverty/object.total_family*100
#     object.single_parent_percent = (object.total_single_father + object.total_single_mother)/object.total_family * 100
#     object.public_assist_percent = object.total_public_assist/object.total_households*100
#     print(object.poverty_percent)

# data_frame = pandas.DataFrame(json)

# data_frame.to_excel("C:\\Users\\DanFang\\Desktop\\ziptestpovertyage.xlsx")