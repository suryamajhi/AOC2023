#include <bits/stdc++.h>
#include <fstream>
using namespace std;

// author: surya


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	fstream inputFile;

	inputFile.open("1.txt", ios::in);

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
		}
		for(int i = name.length() -1 ; i >= 0; i--) {
			if(isdigit(name[i])) {
				second = name[i] - 48;
				break;
			}
		}
		result += first * 10 + second;
	}
	cout << result;
	return 0;
}