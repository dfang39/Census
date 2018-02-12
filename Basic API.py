import requests
import os
import openpyxl
import pandas
import Variables

api_key = "0bfe5578f2f3e0f6a2752d4b08bcf6f428db83a5"


variables = ''
variable_array = Variables.poverty_level_by_age

for i in range(0, len(variable_array)):
    variables += "," + str(variable_array[i])

url_string = 'https://api.census.gov/data/2016/acs/acs5?get=NAME' + variables + '&for=zip%20code%20tabulation%20area:*&key=' + api_key
print(url_string)

request = requests.get(url_string)

json = request.json()

data_frame = pandas.DataFrame(json)

data_frame.to_excel("C:\\Users\\DanFang\\Desktop\\ziptestpovertyage.xlsx")