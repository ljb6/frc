import requests

class TbaRequests():
    def __init__(self, apiKey):
        self.tbaEndpoint = "https://www.thebluealliance.com/api/v3"
        self.tbaHeaders = {"X-TBA-Auth-Key": apiKey}

    def getTeamBasicInfo(self, team):
        response = requests.get(self.tbaEndpoint + f"/team/frc{team}", headers=self.tbaHeaders).json()
        return {
            "nickname": response["nickname"],
            "teamNumber": response["team_number"],
            "rookieYear": response["rookie_year"],
            "country": response["country"],
            "key": response["key"]
            }
    
    def getAmpLeverageForEvents(self, events):
        response = requests.get(self.tbaEndpoint + f"/events/event??", headers=self.tbaHeaders).json()


teste = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")
