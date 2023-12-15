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
			if(ch != '*') {
				continue;
			}
			int first = -1;
			int second = -1;
			if(j < y - 1 && isdigit(matrix[i][j + 1]) && !boolMatrix[i][j + 1]) {
				int curX = i;
				int curY = j + 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j + 2;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}

			}
			if(j > 0 && isdigit(matrix[i][j - 1]) && !boolMatrix[i][j - 1]) {
				int curX = i;
				int curY = j - 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}
			}
			if(i < x - 1 && isdigit(matrix[i + 1][j]) && !boolMatrix[i + 1][j]) {
				int curX = i + 1;
				int curY = j;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j + 1;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}

			}
			if(i > 0 && isdigit(matrix[i - 1][j]) && !boolMatrix[i - 1][j]) {
				int curX = i - 1;
				int curY = j;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j + 1;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}			
			}
			if(i < x - 1 && j < y - 1 && isdigit(matrix[i + 1][j + 1]) && !boolMatrix[i + 1][j + 1] ){
				int curX = i + 1;
				int curY = j + 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j + 2;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}
			}
			if(i < x - 1 && j > 0 && isdigit(matrix[i + 1][j - 1]) && !boolMatrix[i + 1][j - 1]) {
				int curX = i + 1;
				int curY = j - 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}

			}
			if(i > 0 && j < y - 1 && isdigit(matrix[i - 1][j + 1]) && !boolMatrix[i - 1][j + 1]) {
				int curX = i - 1;
				int curY = j + 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j + 2;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}
			}
			if(i > 0 && j > 0 && isdigit(matrix[i - 1][j - 1]) && !boolMatrix[i - 1][j - 1]) {
				int curX = i - 1;
				int curY = j - 1;
				vector<char> tmp;
				while(curY >= 0 && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.insert(tmp.begin(), matrix[curX][curY]);
					curY = curY - 1;
				}
				curY = j;
				while(curY < y && isdigit(matrix[curX][curY])) {
					boolMatrix[curX][curY] = true;
					tmp.push_back(matrix[curX][curY]);
					curY = curY + 1;
				}
				string str(tmp.begin(), tmp.end());
				if(first == -1) {
					first = stoi(str);
				} else {
					result += first * stoi(str);
				}
			}
		}
	}

	cout << result;
	return 0;
}