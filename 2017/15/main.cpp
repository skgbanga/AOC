#include <iostream>
using namespace std;


class Gen {
  public:
    Gen(int64_t start, int64_t mult, int mod) : start_(start), mult_(mult), mod_(mod) {  }

    int64_t next() {
      int64_t p;
      do {
        p = (start_ * mult_) % 2147483647;
        start_ = p;
      } while (p % mod_ != 0);
      return p;
    }

   private:
    int64_t start_;
    int64_t mult_;
    int64_t mod_;
};

int main() {
  auto g1 = Gen(512, 16807, 4);
  auto g2 = Gen(191, 48271, 8);

  auto s = 0;
  auto cnt = 0;
  while (cnt < 5'000'000) {
    uint16_t a1 = g1.next();
    uint16_t a2 = g2.next();
    if (a1 == a2) {
      s += 1;
    }
    cnt += 1;
  }
  cout << s << '\n';
}
