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
		play(playlist)

	else :
		print "Error. No playlist name given"
		return

elif intent=="search":
	searchWolfram(command)

def play(playlist):


#function to take in search query text
def searchWolfram(query):

	#wolfram API app ID
	app_id = AX9HR8-JQYEK5WJL6

	#get response
	client = wolframalpha.Client(app_id)
	resp = client.query(query)

	if len(resp.pods) > 0:
    	ans = ""
    	pod = resp.pods[1]
    	if pod.text:
        	ans = pod.text
    	else:
        	ans = "No answer found"
 
   		print ans

