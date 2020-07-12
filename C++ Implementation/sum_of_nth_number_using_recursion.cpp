#include<bits/stdc++.h>

using namespace std;

int fact(int n)
{
    if (n==0)
        return 0;
    else
    return n+fact(n-1);
}

int main()
{
    int n = 5;
    cout << n*(n+1)/2 << endl;
    cout << fact(n) << endl;
}
