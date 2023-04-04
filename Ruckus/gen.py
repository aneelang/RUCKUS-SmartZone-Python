import requests
import warnings
import json

warnings.simplefilter('ignore')

# Get authentication token
def getToken(host, username, password):
    url = "https://" + host + ":8443" + "/wsg/api/public/v11_1/serviceTicket"
    body = {'username': username,'password': password} 
    r = requests.post(url, json = body, verify=False)
    # token = r.json()['serviceTicket']
    if r.status_code == 200:
        token = r.json()['serviceTicket']
        # print(r.json())
    else:
        token=""
        print(r.json(), r.status_code)
    return token

# token = getToken("52.60.240.145", "Hadi", "Genwave99!")
# print(token)


def getAPList(host, serviceTicket):
    url = "https://" + host + ":8443" + "/wsg/api/public/v11_1/aps?serviceTicket="+serviceTicket
    body={}
    r = requests.get(url, json=body, verify=False)
    APList = []
    if r.status_code == 200:
        APList = r.json()['list']
        APList = json.dumps(APList, indent=3)
    else:
        print(r.status_code)
    return APList

# print(APList)

# def apDoc(host, serviceTicket, apMac):
#     url = "https://" + host + ":8443" + f"/wsg/api/public/v11_1/aps/{apMac}/supportLog?serviceTicket=" + serviceTicket
#     body={}
#     file = requests.get(url, json=body, verify=False)
#     if file.status_code == 200:
#         open('facebook.txt', 'wb').write(file.content)
#     else:
#         print(file.status_code)

def queryAllAPs(host, serviceTicket):
    url = "https://" + host + ":8443"+"/wsg/api/public/v11_1/query/ap?serviceTicket="+serviceTicket
    body = {
        "filters": [

        ],
        "extraFilters": [

        ],
        "extraNotFilters": [

        ],
        "options": {
            "auth_includeNa": True,
            "auth_includeLocalDb": True,
            "auth_includeGuest": True,
            "auth_includeAdGlobal": True,
            "auth_type": "",
            "auth_realmType": "ALL",
            "acct_type": "",
            "auth_testableOnly": True,
            "acct_testableOnly": True,
            "acct_includeNa": True,
            "forwarding_type": "",
            "includeSharedResources": True,
            "INCLUDE_RBAC_METADATA": True,
            "TENANT_ID": "",
            "inMap": True,
            "globalFilterId": "",
            "auth_hostedAaaSupportedEnabled": True,
            "auth_plmnIdentifierEnabled": True,
            "includeUsers": True,
            "includeUserClickNode": True
        },
        "extraTimeRange": {
            "start": 0,
            "end": 0,
            "interval": 0,
            "field": "insertionTime"
        },
        "fullTextSearch": {
            "type": "AND",
            "value": "",
            "fields": [
            ""
            ]
        },
        "attributes": [
        ],
        "sortInfo": {
            "sortColumn": "",
            "dir": "ASC"
        },
        "page": 1,
        "limit": 1,
        "expandDomains": True,
        "criteria": "none",
        "query": "none"
    }

    APList = []
    APList = requests.post(url, json=body, verify=False)
    APList = json.dumps(APList.json(), indent=5)
    print(APList['list'])



def main():

    print("Getting token")
    token = getToken("52.60.240.145", "Hadi", "Genwave99!")
    # APList = []
    # APList = getAPList("52.60.240.145", token)
    # apMac = '0C:F4:D5:2F:98:00'
    # url = f"https://52.60.240.145:8443/wsg/api/public/v11_1/aps/" + apMac +"?serviceTicket="+token
    # body = {}
    # r = requests.get(url, json=body, verify=False)

    # if r.status_code == 200:
    #     message = r.json()
    #     message = json.dumps(message, indent=2)
    #     print(message)
    # else:
    #     print(r.status_code)
    # # print("Getting AP Support log")
    # # apDoc("52.60.240.145", token, apMac)
    # print(APList)
    queryAllAPs("52.60.240.145", token)


if __name__=="__main__":
    main()