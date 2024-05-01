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
    
    def getTeamEvents(self, team):
        response = requests.get(self.tbaEndpoint + f"/team/frc{team}/events/2024", headers=self.tbaHeaders).json()
        events = {}
        for event in response:
            events["2024" + event["event_code"]] = event["name"]
        return events
    
    def getEventsAmpLeverage(self, events):
        counter = 0
        for event in events:
            response = requests.get(self.tbaEndpoint + f"/event/{event}/matches??", headers=self.tbaHeaders).json()
            ampLeverage = []
            matchCounter = 1

            for match in response:
                if match["score_breakdown"] is not None:
                    speakerAmplifiedNotesBlue = match["score_breakdown"]["blue"]["teleopSpeakerNoteAmplifiedCount"]
                    ampNotesBlue = match["score_breakdown"]["blue"]["teleopAmpNoteCount"]
                    if ampNotesBlue > 0:
                        ampLeverage.append({"match": matchCounter, "porcentage": speakerAmplifiedNotesBlue / ((ampNotesBlue / 2) * 4)})
                if match["score_breakdown"] is not None:
                    speakerAmplifiedNotesRed = match["score_breakdown"]["red"]["teleopSpeakerNoteAmplifiedCount"]
                    ampNotesRed = match["score_breakdown"]["red"]["teleopAmpNoteCount"]
                    if ampNotesRed > 0:
                        ampLeverage.append({"match": matchCounter, "porcentage": speakerAmplifiedNotesRed / ((ampNotesRed / 2) * 4)})
                matchCounter += 1

            counter += 1
            
        total = 0
        for metric in ampLeverage:
            total += metric["porcentage"]
        
        leverage = str(total / len(ampLeverage) * 100)
        return leverage[:5] + "%"
    
    def getYearInfo(self, year):
        response = requests.get(self.tbaEndpoint + f"/events/{year}/keys", headers=self.tbaHeaders).json()
        events = len(response) - 8
        
        return {"events": events}

    def getYearActiveTeams(self, year): # TODO: fix complexity to use
        page = 1
        counter = 0
        while True:
            response = requests.get(self.tbaEndpoint + f"/teams/{year}/{page}", headers=self.tbaHeaders).json()
            counter += len(response)
            if len(response) == 0: break
            page += 1
            
        return counter

teste = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")
#print(teste.getYearInfo("2024"))
#print(teste.getYearActiveTeams("2023"))

# 2023: 3153
# 2024: 3291