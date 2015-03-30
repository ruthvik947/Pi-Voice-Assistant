import requests
import sys
import wolframalpha

#parse all the data from the wit json output
response = requests.get(sys.argv[1])
data = response.json()

#data is in dictionary so easy access is possible
#need to extract intent and playlist name

command = data["_text"]
intent = data["intent"]

#assuming the second word in the command is the name of the playlist
if len(command) > 2:
	playlist = command[1]

else :
	print "Error. No playlist name given"
	return



