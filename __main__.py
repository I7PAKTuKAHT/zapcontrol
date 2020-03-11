from datetime import datetime
import json
import sys, string, io, os
import requests

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

from suds.client import Client
# Create proxy from WSDL
url = 'http://bcvm559:50013?wsdl'
client = Client(url)

# Call unprotected webmethod with complex output
result = client.service.GetProcessList()
print(result)

# Access output data
print('PID:', result[0][0].pid)

# Call unprotected webmethod with complex output on another instance
client.set_options(location='http://bcvm559:50013?wsdl')
result = client.service.GetProcessList()
print('Status:') 
prGreen(result[0][0].dispstatus)
print('Status:') 
prGreen(result[0][1].dispstatus)
print('Status:') 
prGreen(result[0][2].dispstatus)
#prGreen(result)

# Provide user and password for protected webmethod
#client2 = Client(url, username='soladm', password='')
#result = client2.service.ParameterValue('rdisp/myname')
#print('rdisp/myname:', result)
