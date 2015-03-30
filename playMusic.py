import requests
import sys
import wolframalpha from wolframalpha

#parse all the data from the wit json output
response = requests.get(sys.argv[1])
data = response.json()

#data is in dictionary so easy access is possible
#need to extract intent and playlist name

command = data["_text"]
intent = data["intent"]

#if intent is play (music)
if intent=="play":
#assuming the second word in the command is the name of the playlist
	if len(command) > 2:
		playlist = command[1]

	else :
		print "Error. No playlist name given"
		return

elif intent=="search":
	searchWolfram(command)

def searchWolfram(query):

	app_id = AX9HR8-JQYEK5WJL6

	client = wolframalpha.Client(app_id)

	resp = client.query(query)

	if len(resp.pods) > 0:
    	texts = ""
    	pod = resp.pods[1]
    	if pod.text:
        	texts = pod.text
    	else:
        	texts = "I have no answer for that"
 
   		print texts
	else:
    	print "Unkown search command"
