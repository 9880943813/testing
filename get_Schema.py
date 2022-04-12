import requests
import json
import socket
import sys
import os

step_name = sys.argv[1]
project_name = sys.argv[2]
table_name = sys.argv[3]
print(step_name)
print(project_name)
print(table_name)
def fetch_data():
    url = "http://cesiumk8s-sjc.cisco.com/msvcs/polaris-svcs/generic_api"
    input = {
        "operation": "read",
        "options": "process_flow_get_project_metadata_by_step",
        "input": {
            "step_name": step_name,
            "project_name": project_name
            }
        }

    headers = {
        "csession": "6DB3E80F-8B57-49FA-9297-769F0FAE7ED2",
        "Content-type": "application/json"
        }
    response = requests.post(url, headers=headers, data=json.dumps(input))
    out = response.json()
    table = out['results'][1][0]['template_step_table_list']
    for i in range(len(table)):
         attributeslist = {}
         
         if table_name:
             if table[i]['table_name']==table_name:
                 for j in table[i]['attribute_list']:
                     attributeslist[j["attribute_name"]] = ""

                 json_object = json.dumps(attributeslist, indent = 4)
                 print "TABLE_NAME:",table[i]['table_name']
                 print "ATTRIBUTE_LIST:",json_object
             
         else:
             for j in table[i]['attribute_list']:
                 attributeslist[j["attribute_name"]] = ""
    
             json_object = json.dumps(attributeslist, indent = 4)
             print "TABLE_NAME:",table[i]['table_name']
             print "ATTRIBUTE_LIST:",json_object
       # print(table[i])
       # break
        #if table[i]['table_name']==table_name:
            #return table[i]
    #print(table)
        
    
fetch_data()
    
