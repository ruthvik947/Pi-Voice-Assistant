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

	//pass intent and playlist name to the mopidy function

}

//function to look through the ifile, find the intent as well as the playlist and return it
void findPurpose(ifstream & ifile, string & intent, string & playlist)
{

}