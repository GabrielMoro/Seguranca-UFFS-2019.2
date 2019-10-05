#include <stdio.h>

typedef long long ll;

ll gcdExtended(ll a, ll b, ll *x, ll *y){
    if (a == 0){
        *x = 0, *y = 1;
        return b;
    }

    ll x1, y1;
    ll gcd = gcdExtended(b % a, a, &x1, &y1);

    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

ll modInverse(int a, int m){
    ll x, y;
    ll g = gcdExtended(a, m, &x, &y);
    if (g != 1)
        return 0;
    else{
        ll res = (x % m + m) % m;
        return res;
    }
}

ll modExp(ll x, ll y, ll p){
    ll res = 1;
    x = x % p; 

    while (y > 0){
        if (y & 1)
            res = (res * x) % p;

        y = y >> 1;
        x = (x * x) % p;
    }
    return res;
}

ll phi(ll n){
    ll result = n, i;
    for (i = 2; i * i <= n; i++){
        if (n % i == 0){
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}

int main(void){
    int n, e, c;
    ll phiN;

    scanf("%d %d %d", &n, &e, &c);

    phiN = phi(n);
    ll d = modInverse(e, phiN);
    ll m = modExp(c, d, n);

    printf("%lld\n", m);

    return 0;
}
