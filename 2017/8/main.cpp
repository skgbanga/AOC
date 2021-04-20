#include <iostream>
#include <functional>

using namespace std;

std::function<int(int, int)> foo(int c) {
  auto add = [] (auto a, auto b) { return a + b; };
  auto sub = [] (auto a, auto b) { return a - b; };
  if (c > 42) {
    return add;
  } else {
    return sub;
  }
}

int main() {
  cout << foo(100)(10, 20) << '\n';
}
