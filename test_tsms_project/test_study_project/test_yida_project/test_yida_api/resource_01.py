import requests,time,json

url = 'http://139.159.147.3:9981/resource/resource/projectStage/add'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJ5aWRhIiwibW9iaWxlIjoiMTg1NzU2OTc0ODIiLCJ1c2VyaWQiOjQwLCJtYW5hZ2VyTm8iOiIxNTIyNjEyODYyMjY0OTEwIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIl0sImNsaWVudF9pZCI6InlkX2Nsb3VkIiwiaGVhZCI6Imh0dHBzOi8vb3NzLnlpZGF5dW50dS5jb20vMTUyMjYxMjg2MjI2NDkxMC8yMDE5MTExOS8xNTc0MTMzMzQ1MjUzNC9pbWFnZTAuanBnIiwibWFuYWdlclR5cGUiOjEsInJlYWxOYW1lIjoi5Lq_6L6-5Lit5Zu9IiwiYXVkIjpbInByb3BlcnR5LWFwaSIsImF1dGhvcml6ZS1zZXJ2ZXIiLCJ5ZF93ZWIiLCJvcGVyYXRpb24tYXBpIiwieWRfc2hvcCIsInNtYXJ0cGFydHkiXSwiY29tcGFueUlkIjoyLCJzY29wZSI6WyJhIl0sImxvZ2luTmFtZSI6InlpZGEiLCJleHAiOjE1ODg2MjM2MzcsImp0aSI6IjNlYjM1YjM0LWJkMWEtNGM4OS1hOWYwLWI2ZmM0MGY5ZjIxNCJ9.oRU6PLafb8dg-8n7hB34sJdfeSkVDZmH8YdSPlWK74HPLBG0LLBccyEPyg8RLcge6cbeF-GWiTRc5HkVwe5OciDTIvov607MP0VLDY4w0MoO2MS5OAmXfntuZiLwIIvUFBxqAn644eSIfCtA1RmsfRwN7EzSltcgU91fYwTH_iNxckJ3XxmgjL35T9yK-kAh32V5BNgfQdazMKxXSb39Ac8Lb4-RKY0a2Cmjc9whZsBQk1B0yBduOcm5hHBWTMkoK1Plo-3gwIWRFSyRsgshH2rWFpJ4_DxgwpTMs75h-53B2K-jldZa_8ct5cFUiqcQ2Bdr79ILENZ87ZIajrdCGQ",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
data ={
    "projectStage": 520,
    "projectStageName": "易达云图",
    "planArchitectureArea": 123232131,
    "capacityRate": 213213213,
    "projectId": 83213214
}

response = requests.get(url,headers=headers,data=parms)
print(response.status_code)
a = response.json()
print(a)