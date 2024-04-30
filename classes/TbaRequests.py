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
