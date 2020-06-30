import json,time,logging,os,unittest,tempfile,requests
from flask import Flask,make_response

# pip install -i http://szcinstall.paic.com.cn:30000/pypi/simple --trusted-host szcinstall.paic.com.cn --user XXX
url = "http://httpbin.org/post?a=1"
r = requests.post(url=url)
print(r.text)