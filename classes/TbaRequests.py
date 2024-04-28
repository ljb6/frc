import requests

class TbaRequests():
    def __init__(self, apiKey):
        self.tbaEndpoint = "https://www.thebluealliance.com/api/v3"
        self.tbaHeaders = {"X-TBA-Auth-Key": apiKey}

    def getTeamEvents(self, team):
        response = requests.get(self.tbaEndpoint + f"/team/frc{team}", headers=self.tbaHeaders).json()
        print(response)

teste = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")

teste.getTeamEvents("1156")