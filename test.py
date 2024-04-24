import requests

TbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
TbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
TbaHeaders = {"X-TBA-Auth-Key": TbaApiKey}

team = int(input("Team Number: "))
team = f"frc{team}"

response = requests.get(TbaApiEndpoint + f"/team/{team}/awards", headers=TbaHeaders).json()
