#include <bits/stdc++.h>
#include <fstream>
using namespace std;

// author: surya


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	fstream inputFile;

	inputFile.open("2.txt", ios::in);

	map<string, int> mp;
	mp["one"] = 3;
	mp["two"] = 3;
	mp["three"] = 5;
	mp["four"] = 4;
	mp["five"] = 4;
	mp["six"] = 3;
	mp["seven"] = 5;
	mp["eight"] = 5;
	mp["nine"] = 4;

	map<string, int> valueMp;
	valueMp["one"] = 1;
	valueMp["two"] = 2;
	valueMp["three"] = 3;
	valueMp["four"] = 4;
	valueMp["five"] = 5;
	valueMp["six"] = 6;
	valueMp["seven"] = 7;
	valueMp["eight"] = 8;
	valueMp["nine"] = 9;


	string name;
	int result = 0;
	while(getline(inputFile, name)) {
		int first;
		int second;
		for(int i = 0; i < name.length(); i++) {
			if(isdigit(name[i])) {
				first = name[i] - 48;
				break;
			}
			bool found = false;
			for(const auto &p: mp) {
				if(i + 1 >= p.second) {
					string tmp = name.substr(i - p.second + 1, p.second);
					if(tmp == p.first) {
						first = valueMp[tmp];
						found = true;
						break;
					}
				}	
			}
			if(found) break;
		}
		// cout << first;
		for(int i = name.length() -1 ; i >= 0; i--) {
			if(isdigit(name[i])) {
				second = name[i] - 48;
				break;
			}
			bool found = false;
			for(const auto &p: mp) {
				if(name.length() - i >= p.second) {
					string tmp = name.substr(i, p.second);
					if(tmp == p.first) {
						second = valueMp[tmp];
						found = true;
						break;
					}
				}	
			}
			if(found) break;
		}
		// cout << second << endl;
		result += first * 10 + second;
	}
	cout << result;
	return 0;
}