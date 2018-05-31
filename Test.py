import requests
import pandas
# facebook

token = "EAACEdEose0cBAK234Ap88lC50wHIcqBFQ9KwrrzWo78GKdHDJMPFRaYJZC34QVCKZAhkIWhpsjGIMVR09aGvqz4YduyARMZBd0pGuDY208GFsZBJZCjFtesm2reBZCmjpzqLZAIjYJgnX6A1qLWPhcjRWR8TmMbaZBotp9hzrZAHGhYDVBRqWJPaFZA1odau2LHFUyGEuSZA4FnkAZDZD"

url_string = "https://graph.facebook.com/67376508857/feed?fields=message,picture,full_picture,created_time&limit=100&access_token=" + token

request = requests.get(url_string)

json = request.json()

print(json)

data_frame = pandas.DataFrame(json['data'])

data_frame.to_excel("C:\\Users\\DanFang\\Desktop\\facebook.xlsx")