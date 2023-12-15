#include <bits/stdc++.h>
#include <fstream>

using namespace std;

// author: surya


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	fstream inputFile;
	inputFile.open("1.txt", ios::in);
	string line;

	vector<int> time;
	vector<int> distance;

	while(getline(inputFile, line)) {
		bool num = false;
		vector<char> tmp;
		for(int i = 0; i < line.length(); i++) {
			if(isdigit(line[i])) {
				num = true;
				tmp.push_back(line[i]);
			} else {
				if(num) {
					string str(tmp.begin(), tmp.end());
					if(!str.empty()) {
						if(line[0] == 'T') {
							time.push_back(stoi(str));
						} else distance.push_back(stoi(str));
						tmp.clear();
					}
					
				}
			}
		}
		string str(tmp.begin(), tmp.end());
		if(line[0] == 'T') {
			time.push_back(stoi(str));
		} else distance.push_back(stoi(str));
	}
	int result = 1;
	for(int i = 0; i < time.size(); i++) {
		int count = 0;
		int record = time[i];
		for(int j = 1; j < record; j++) {
			int takenTime = (record - j) * j;
			if(takenTime > distance[i]) count++;
		}
		cout << count << ' ';
		result *= count;
	}

	cout << endl << result;
	return 0;
	
	
}