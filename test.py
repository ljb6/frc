import requests

TbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
TbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
TbaHeaders = {"X-TBA-Auth-Key": TbaApiKey}

response = requests.get(TbaApiEndpoint + f"/team/frc1156/matches/2024", headers=TbaHeaders).json()
#print(response[0])

coreData = []

for match in response:
    coreData.append({
        "matchType": match["comp_level"],
        "red": match["alliances"]["red"]["team_keys"],
        "blue": match["alliances"]["blue"]["team_keys"],
        "winningAlliance": match["winning_alliance"],
        })
    
print(coreData[8])