import requests

url = "http://127.0.0.1:5000/predict"

data = {
  "hours_studied":5,
  "attendance":80,
  "previous_score":70,
  "extra_classes":1,	
  "age":18,
  "gender":0,
  "parent_education_Bachelor":1,
  "parent_education_College":0,
  "parent_education_Highschool":0,
  "parent_education_Masters":0

}

response = requests.post(url,json=data)


print("status code:",response.status_code)
print("predictions:",response.text)

