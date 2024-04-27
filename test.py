import requests

TbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
TbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
TbaHeaders = {"X-TBA-Auth-Key": TbaApiKey}

response = requests.get(TbaApiEndpoint + f"/team/frc1156/events/2024", headers=TbaHeaders).json()
#print(response[0])

for i in response:
    print(i["name"])