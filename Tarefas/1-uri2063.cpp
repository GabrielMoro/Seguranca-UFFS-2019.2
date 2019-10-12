#include <iostream>
#include <cstring>

#define MAX 112

using namespace std;

int gcd(int a, int b){
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

int lcm(int a, int b){
  return (a * b)/gcd(a, b);
}

int main(){
  int i, j, n, res = 1;
  int b[MAX], c[MAX], v[MAX];

  memset(c, 0, sizeof(c));
  memset(v, 0, sizeof(v));

  cin >> n;

  for(i = 0; i < n; i++){
    cin >> b[i];
    b[i]--;  
  }

  for(i = 0; i < n; i++){
    j = i;
    while(v[j] == 0){
      v[j]++;
      c[i]++;
      j = b[j];
    }
    if (c[i] == 0)
      continue;
    res = lcm(res, c[i]);
  }

  cout << res << endl;

  return 0;
}
