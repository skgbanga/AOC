#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <numeric>
#include <unordered_set>
#include <deque>
#include <algorithm>

using namespace std;

struct Edge {
  string a;
  string b;
};


int main() {
  vector<Edge> edges;
  unordered_set<string> nodes;
  fstream stream ("input");
  string line;
  while (getline(stream, line)) {
    auto idx = line.find(')');
    auto a = line.substr(0, idx);
    auto b = line.substr(idx + 1);
    edges.emplace_back(Edge{a, b});
    nodes.emplace(a);
    nodes.emplace(b);
  }

  unordered_map<string, int> distance;
  for (const auto& n : nodes) {
    distance.try_emplace(n, numeric_limits<int>::max());
  }

  unordered_set<string> visited;
  deque<string> q;
  distance["YOU"] = 0;
  q.emplace_back("YOU");
  while (!q.empty()) {
    auto n = q.front();
    q.pop_front();
    visited.emplace(n);
    for (const auto& [a, b] : edges) {
      if ((a == n) || (b == n)) {
        auto other = (a == n) ? b : a;
        auto iter = visited.find(other);
        if (iter == visited.end()) {
          distance[other] = min(distance[other], distance[n] + 1);
          q.emplace_back(other);
        }
      }
    }
  }

  cout << distance["SAN"] - 2 << '\n';
}
