#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int n, m;

// author: surya

int twoDToOneD(int row, int col) {
	return row * m + col;
}

vector<int> oneDToTwoD(int a) {
	return vector<int> { a / m, a%m };
}

bool isInside(vector<int>& longestPoints, int xp, int yp) {

	int cnt = 0;
	for(int i = 1; i < longestPoints.size(); i++) {
		int e1 = longestPoints[i - 1];
		int e2 = longestPoints[i - 2];
		double x1 = e1 / m;
		double y1 = e1 % m;
		double x2 = e2 / m;
		double y2 = e2 % m;

		if(((yp < y1) != (yp < y2)) && (xp < x1 + ((yp - y1)/(y2 - y1)) * (x2 - x1))) {
			cnt++;
		}
	}
	return cnt%2 == 1;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	fstream inputFile;

	inputFile.open("input.txt", ios::in);

	string line;
	vector<vector<char>> matrix;

	while(getline(inputFile, line)) {
		vector<char> lineV;
		for (int i = 0; i < line.length(); i++) {
			lineV.push_back(line[i]);
		}
		matrix.push_back(lineV);
	}
	n = matrix.size();
	m = matrix[0].size();
	int start[2];
	for(int i = 0; i < matrix.size(); i++) {
		for(int j = 0; j < matrix[i].size(); j++) {
			if(matrix[i][j] == 'S') {
				start[0] = i;
				start[1] = j;
			}
		}
	}

	// BFS
	queue<int> que;
	vector<vector<bool>> visited(n, vector<bool>(m, false));
	vector<vector<int>> distance(n, vector<int>(m, 0));


	visited[start[0]][start[1]] = true;
	distance[start[0]][start[1]] = 0;
	que.push(twoDToOneD(start[0], start[1]));
	vector<int> loops;
	int result = 0;
	vector<vector<int>> pointVector(n * m, vector<int>(0, {}));
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			int oneD = twoDToOneD(i, j);
			pointVector[oneD].push_back(oneD);
		}
	}

	vector<int> longestPoints;

	// for(int i = 0; i < pointVector.size(); i++) {
	// 	for(int j = 0; j < pointVector[i].size(); j++) {
	// 		cout << i << ' ' << j << ' ' << pointVector[i][j] << ' ';
	// 	}
	// 	cout << endl;
	// }

	while(!que.empty()) {
		int s = que.front(); que.pop();
		vector<int> dir = oneDToTwoD(s);
		// cout << dir[0] << ' ' << dir[1];
		char ch = matrix[dir[0]][dir[1]];
		if(ch == '.')
			continue;
		if(ch == 'S') {
			vector<int> p {dir[0] - 1, dir[1]};
			visited[p[0]][p[1]] = true;

			if(matrix[p[0]][p[1]] == '|' ||
				matrix[p[0]][p[1]] == 'F' ||
				matrix[p[0]][p[1]] == '7'
				) {
				pointVector[twoDToOneD(p[0], p[1])].push_back(twoDToOneD(dir[0], dir[1]));
				distance[p[0]][p[1]] = distance[dir[0]][dir[1]] + 1;
				que.push(twoDToOneD(p[0], p[1]));
			}

			vector<int> q {dir[0], dir[1] - 1};

			visited[q[0]][q[1]] = true;

			if(matrix[q[0]][q[1]] == '-' ||
				matrix[q[0]][q[1]] == 'F' ||
				matrix[q[0]][q[1]] == 'L'
				) {
				pointVector[twoDToOneD(q[0], q[1])].push_back(twoDToOneD(dir[0], dir[1]));
				distance[q[0]][q[1]] = distance[dir[0]][dir[1]] + 1;
				que.push(twoDToOneD(q[0], q[1]));
			}



			vector<int> r {dir[0], dir[1] + 1};
			visited[r[0]][r[1]] = true;

			if(matrix[r[0]][r[1]] == '-' ||
				matrix[r[0]][r[1]] == 'J' ||
				matrix[r[0]][r[1]] == '7'
				) {
				pointVector[twoDToOneD(r[0], r[1])].push_back(twoDToOneD(dir[0], dir[1]));
				distance[r[0]][r[1]] = distance[dir[0]][dir[1]] + 1;
				que.push(twoDToOneD(r[0], r[1]));
			}



			vector<int> s {dir[0] + 1, dir[1]};

			visited[s[0]][s[1]] = true;

			if(matrix[s[0]][s[1]] == '|' ||
				matrix[s[0]][s[1]] == 'J' ||
				matrix[s[0]][s[1]] == 'L'
				) {
				pointVector[twoDToOneD(s[0], s[1])].push_back(twoDToOneD(dir[0], dir[1]));
				distance[s[0]][s[1]] = distance[dir[0]][dir[1]] + 1;
				que.push(twoDToOneD(s[0], s[1]));
			}

		}
		if(ch == '|') {
			vector<vector<int>> aim;
			vector<int> q {dir[0] + 1, dir[1]};
			vector<int> r {dir[0] - 1, dir[1]};
			aim.push_back(q);
			aim.push_back(r);
			for(vector<int> u: aim) {
				int x = pointVector[twoDToOneD(dir[0], dir[1])].rbegin()[1];
				int prevI = x / m;
				int prevJ = x % m;
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m || (u[0] == prevI && u[1] == prevJ)) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}
					continue;
				}
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '|' ||
					matrix[u[0]][u[1]] == '7' ||
					matrix[u[0]][u[1]] == 'F' ||
					matrix[u[0]][u[1]] == 'J' ||
					matrix[u[0]][u[1]] == 'L'
					) {

					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}

					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}
			}
		}

		if(ch == '-') {
			vector<vector<int>> aim;
			vector<int> q {dir[0], dir[1] - 1};
			vector<int> r {dir[0], dir[1] + 1};
			aim.push_back(q);
			aim.push_back(r);

			for(vector<int> u: aim) {
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}
					continue;
				}				
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '-' ||
					matrix[u[0]][u[1]] == '7' ||
					matrix[u[0]][u[1]] == 'F' ||
					matrix[u[0]][u[1]] == 'J' ||
					matrix[u[0]][u[1]] == 'L'
					) {
					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}
					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}
			}
		}

		if(ch == 'L') {
			vector<vector<int>> aim;
			vector<int> p {dir[0] - 1, dir[1]};
			vector<int> r {dir[0], dir[1] + 1};
			aim.push_back(p);
			aim.push_back(r);

			for(vector<int> u: aim) {
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}
					continue;
				}
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '-' ||
					matrix[u[0]][u[1]] == '|' ||
					matrix[u[0]][u[1]] == 'F' ||
					matrix[u[0]][u[1]] == '7' ||
					matrix[u[0]][u[1]] == 'J' 
					) {
					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}
					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}	
			}
		}

		if(ch == 'J') {
			vector<vector<int>> aim;
			vector<int> p {dir[0] - 1, dir[1]};
			vector<int> q {dir[0], dir[1] - 1};
			aim.push_back(p);
			aim.push_back(q);

			for(vector<int> u: aim) {
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}
					continue;
				}
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '-' ||
					matrix[u[0]][u[1]] == '|' ||
					matrix[u[0]][u[1]] == 'F' ||
					matrix[u[0]][u[1]] == '7' ||
					matrix[u[0]][u[1]] == 'L' 
					) {
					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}
					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}
				
			}
		}

		if(ch == '7') {
			vector<vector<int>> aim;
			vector<int> q {dir[0], dir[1] - 1};
			vector<int> s {dir[0] + 1, dir[1]};
			aim.push_back(q);
			aim.push_back(s);

			for(vector<int> u: aim) {
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}
					continue;
				}				
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '-' ||
					matrix[u[0]][u[1]] == '|' ||
					matrix[u[0]][u[1]] == 'F' ||
					matrix[u[0]][u[1]] == 'J' ||
					matrix[u[0]][u[1]] == 'L' 
					) {
					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}
					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}
				
			}
		}

		if(ch == 'F') {
			vector<vector<int>> aim;
			vector<int> r {dir[0], dir[1] + 1};
			vector<int> s {dir[0] + 1, dir[1]};
			
			aim.push_back(r);
			aim.push_back(s);

			for(vector<int> u: aim) {
				if(u[0] < 0 || u[0] >= n || u[1] < 0 || u[1] >= m) continue;
				if(visited[u[0]][u[1]] && distance[u[0]][u[1]] != 0) {
					if((distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1) >= result) {
						result = distance[dir[0]][dir[1]] + distance[u[0]][u[1]] + 1;
						longestPoints.clear();
						for(int i = pointVector[twoDToOneD(dir[0], dir[1])].size() - 1; i >= 0; i--) {
							longestPoints.push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
						}
						for(int i =0 ; i < pointVector[twoDToOneD(u[0], u[1])].size();i++) {
							longestPoints.push_back(pointVector[twoDToOneD(u[0], u[1])][i]);
						}
					}

					continue;
				}		
				visited[u[0]][u[1]] = true;
				if(matrix[u[0]][u[1]] == '-' ||
					matrix[u[0]][u[1]] == '|' ||
					matrix[u[0]][u[1]] == '7' ||
					matrix[u[0]][u[1]] == 'J' ||
					matrix[u[0]][u[1]] == 'L' 
					) {
					for(int i = 0; i < pointVector[twoDToOneD(dir[0], dir[1])].size(); i++) {
						pointVector[twoDToOneD(u[0], u[1])].push_back(pointVector[twoDToOneD(dir[0], dir[1])][i]);
					}
					distance[u[0]][u[1]] = distance[dir[0]][dir[1]] + 1;
					que.push(twoDToOneD(u[0], u[1]));
				}
			}
		}
	}

	// for(int i = 0; i < pointVector.size(); i++) {
	// 	for(int j = 0; j < pointVector[i].size(); j++) {
	// 		cout << pointVector[i][j] << ' ';
	// 	}
	// 	cout << endl;
	// }

	// for(int i = 0; i < longestPoints.size(); i++) {
	// 	cout << longestPoints[i] << ' ';
	// }
	int count = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			int one = twoDToOneD(i, j);
			if(!std::count(longestPoints.begin(), longestPoints.end(), one)) {
				if(isInside(longestPoints, i, j)) {
					count++;
				}
			}
		}
	}
	cout << endl;
	cout << count << endl;
	cout << result / 2 << endl;

	// for(int i = 0; i < distance.size(); i++) {
	// 	for(int j = 0; j < distance[i].size(); j++) {
	// 		cout << distance[i][j] << ' ';
	// 	}
	// 	cout << endl;
	// }
	// cout << result / 2;
	return 0;
}