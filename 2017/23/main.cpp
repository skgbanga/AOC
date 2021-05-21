#include <iostream>

using namespace std;

int main() {
  int b = 84;
  int c = b;
  b *= 100;
  b += 100'000;
  c = b;
  c += 17000;

  int g = 0;
  int h = 0;
  do {
    int f = 1;
    int d = 2;
    do {
      int e = 2;
      do {
        g = d;
        g *= e;
        g -= b;
        if (g == 0) {
          f = 0;
        }
        e += 1;
      } while (e != b);
      d += 1;
    } while (d != b);

    if (f == 0) {
      h += 1;
      cout << "Incremented h for b " << b << endl;
    }

    b += 17;
  } while (b != c);

  cout << h << '\n';
}
