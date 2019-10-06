#include <iostream>

using namespace std;

int mdc(int a, int b){
    if (b == 0) return a;
    return mdc(b, a % b);
}

int main(){
  int n, res = 0;

  cin >> n;
  int b[n];

  for(int i = 0; i < n; i++)
    cin >> b[i];

  for(int i = 0; i < n; i++)
	continue

  cout << res << '\n';

  return 0;
}
