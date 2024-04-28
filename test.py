import requests

tbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
tbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
tbaHeaders = {"X-TBA-Auth-Key": tbaApiKey}

response = requests.get(tbaApiEndpoint + f"/team/frc1156/matches/2024", headers=tbaHeaders).json()
print(response[0])

coreData = []

for match in response:
    coreData.append({
        "matchType": match["comp_level"],
        "red": match["alliances"]["red"]["team_keys"],
        "redScore": match["alliances"]["red"]["score"],
        "blue": match["alliances"]["blue"]["team_keys"],
        "blueScore": match["alliances"]["blue"]["score"],
        "winningAlliance": match["winning_alliance"],
        })
    
#print(coreData[8])