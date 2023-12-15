#include <bits/stdc++.h>
#include <fstream>
#define int long long

using namespace std;

// author: surya


signed main() {
	// ios::sync_with_stdio(false);
	// cin.tie(0);

	fstream inputFile;

	inputFile.open("1.txt", ios::in);

	string line;
	int result = 0;
	vector<vector<char>> matrix;

	while(getline(inputFile, line)) {
		vector<char> x;
		for(int i = 0; i < line.length(); i++) {
			x.push_back(line[i]);
		}
		matrix.push_back(x);

	}
	int x = matrix.size();
	int y = matrix[0].size();
	std::cout.flush();


	vector<vector<bool>> boolMatrix(x, vector<bool>(y, false));
	
	for(int i = 0; i < x; i++) {

		for(int j = 0; j < y; j++) {
			char ch = matrix[i][j];
			if(!isdigit(ch)) {
				continue;
			}
			if(j < y - 1 && !isdigit(matrix[i][j + 1]) && matrix[i][j+1] != '.') {
				boolMatrix[i][j] = true;
			}
			if(j > 0 && !isdigit(matrix[i][j - 1]) && matrix[i][j - 1] != '.') {
				boolMatrix[i][j] = true;
			}
			if(i < x - 1 && !isdigit(matrix[i + 1][j]) && matrix[i + 1][j] != '.') {
				boolMatrix[i][j] = true;
			}
			if(i > 0 && !isdigit(matrix[i - 1][j]) && matrix[i - 1][j] != '.') {
								boolMatrix[i][j] = true;
			}
			if(i < x - 1 && j < y - 1 && !isdigit(matrix[i + 1][j + 1]) && matrix[i + 1][j + 1] != '.' ){
								boolMatrix[i][j] = true;
			}
			if(i < x - 1 && j > 0 && !isdigit(matrix[i + 1][j - 1]) && matrix[i + 1][j - 1] != '.') {
								boolMatrix[i][j] = true;
			}
			if(i > 0 && j < y - 1 && !isdigit(matrix[i - 1][j + 1]) && matrix[i - 1][j + 1] != '.') {
				boolMatrix[i][j] = true;

			}
			if(i > 0 && j > 0 && !isdigit(matrix[i - 1][j - 1]) && matrix[i - 1][j - 1] != '.') {
				boolMatrix[i][j] = true;
			}
		}
	}

	for(int i = 0; i < x; i++) {
		vector<char> num;
		bool connected = false;
		for(int j = 0; j < y; j++) {
			char ch = matrix[i][j];
			if(isdigit(ch)) {
				num.push_back(ch);
				if(boolMatrix[i][j]) {
					connected = true;
				}
				if(j == y - 1) {
					if(connected) {
						string str(num.begin(), num.end());
					result += stoi(str);
					}
				}
			} else {
				if(connected) {
					string str(num.begin(), num.end());
					result += stoi(str);
					// cout << stoi(str) << endl;
				}
				connected = false;
				num.clear();
			}

		}
	}
	cout << result;
	return 0;
}