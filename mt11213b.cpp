// typedef mersenne_twister_engine< uint32_t, 32, 351, 175, 19, 0xccab8ee7, 11, 0xffffffff, 7, 0x31b6ab00, 15, 0xffe50000, 17, 1812433253 > mt11213b;
#include <boost/random.hpp>
#include <iostream>

using namespace boost;
using namespace std;

int main()
{
    mt11213b generator(5489);
    long long n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << generator() << " ";
    }
    cout << "\n";
}
