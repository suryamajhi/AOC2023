#include <bits/stdc++.h>
#include <fstream>
#define int long long

using namespace std;

// author: surya


signed main() {
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
			} 
		}
		string str(tmp.begin(), tmp.end());
		if(line[0] == 'T') {
			time.push_back(stol(str));
		} else distance.push_back(stol(str));
	}
	int count = 0;
	int record = time[0];
	for(int j = 1; j < record; j++) {
		int takenTime = (record - j) * j;
		if(takenTime > distance[0]) count++;
	}

	cout << count;
	return 0;
}