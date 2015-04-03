import requests
import sys
import wolframalpha from wolframalpha
import mpd

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
		#create MPD wrapper object
		playControl = MPDO() 
		playControl.control(playlist)

	else :
		print "Error. No playlist name given"
		return

elif intent=="search":
	searchWolfram(command)
	
def control(playlist):
	self.play(playlist[0])

#function to take in search query text
def searchWolfram(query):

	#wolfram API app ID
	app_id = AX9HR8-JQYEK5WJL6

	#get response
	client = wolframalpha.Client(app_id)
	resp = client.query(query)

	ans = ""
	#pods[0] is the title of the returned list of results
	pod = resp.pods[1]
	#if there's a response
	if pod.text:
    	ans = pod.text
	else:
    	ans = "No answer found"
 
   	print ans

class MPDO(object):
    def __init__(self):
    	#we will need server and port names/numbers to connect to local MPD client
        self.server = "localhost"
        self.port = 6600

        #prepare client
        self.client = mpd.MPDClient()
        self.client.timeout = None
        self.client.idletimeout = None
        self.client.connect(self.server, self.port)

        #load playlists
        self.playlists = [x["playlist"] for x in self.client.listplaylists()]

        #define function that takes in playlist name and plays
    def play(self, playlist_name):
    	#empty current play queue
        self.client.clear()
        #load new playlist and then play - these are mpdclient commands
        self.client.load(playlist_name)
        self.client.play()



