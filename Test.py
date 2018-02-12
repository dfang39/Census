import requests



token = "EAACEdEose0cBAPlEKJIhkM1bQxQDyHULJSlKzTZA3DMD0CiogZBmD8YDqrZBSVAOaVhById42EtQQRykdV1w1T6hSZBZBOCosVlZB4hYceytYcZCC5dMXnfInrzoZAMHZCANs00pXMbu1v9ZBbT6kTYEZC2zejb0ka9QqhaeEZC7F64ZCTpTW18ZAZAUi2VSXojiiakDqVVWDPjtQfWvAZDZD"

url_string = "https://graph.facebook.com/67376508857/feed?fields=message,picture,full_picture&access_token=" + token

request = requests.get(url_string)

json = request.json()

print(json)