'''
Name: Colin Bui, Mahaly Marcelin
email: buici@mail.uc.edu, marcelml@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Anything else that's relevant: 
Created on November 16
'''

import json, requests

#API: 6GdzhIKPz8qS2dkdPkZMxwhgl6fziXxQ7g6jfbEu
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=6GdzhIKPz8qS2dkdPkZMxwhgl6fziXxQ7g6jfbEu')

json_string = response.content

parsed_json = json.loads(json_string) 

#prints python dictionary    
print(parsed_json)

date = (parsed_json['date'])
explanation = (parsed_json['explanation'])

#shows date & explanation of Picture of the day
print(date)
print(explanation)
