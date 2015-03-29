#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

void findPurpose(ifstream & ifile, string & intent, string & playlist);

int main (int argc, char* argv[]) 
{
	//parse the witOutput.txt file and make sure contents exist
	ifstream ifile(argv[1]);

	if (ifile.fail()) {
		cout << "Error parsing" << endl;
	}

	string intent, playlist;
	findIntent(ifile, intent, playlist);

	//only if intent is stop, leave the app
	if (intent == "stop") {
		cout << "Bye!" << endl;
		return 0;
	}

	//pass intent and playlist name to the mopidy function
	callMopidy(intent, playlist);

	return 0;

}

//function to look through the ifile, find the intent as well as the playlist and return it
void findPurpose(ifstream & ifile, string & intent, string & playlist)
{

}