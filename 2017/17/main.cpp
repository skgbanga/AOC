#include <vector>
#include <iostream>

using namespace std;

struct Node {
  int value;
  Node* next;
};

int main() {
  int N = 50'000'001;
  std::vector<Node> pool;
  pool.resize(N);

  int idx = 0;

  int R = 386;
  Node head;
  head.value = 0;
  head.next = &head;

  Node* current = &head;
  for (int i = 1; i < N; ++i) {
    for (int r = 0; r < R; ++r) {
      current = current->next;
    }
    Node* n = &pool[idx++];
    n->value = i;
    n->next = current->next;
    current->next = n;

    current = n;
  }

  cout << current->next->value << '\n';

  for (int i = 1; i < N; ++i) {
    if (current->value == 0) {
      cout << current->next->value << '\n';
      break;
    } else {
      current = current->next;
    }
  }
}
