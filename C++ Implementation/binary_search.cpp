#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll b_search(vector<ll>v,ll value)
{
    ll r = v.size()-1;
    ll l = 0;
    while(r>=l)
    {
       ll mid = l+(r-l)/2;
        if(v[mid] ==  value)
        {
            return mid;
        }
        else if (v[mid] > value)
        {
            r = mid-1;
        }
        else
        {
            l = mid+1;
        }
    }
    return -1;
}

int main()
{
    vector<ll> v = {1,2,3,4,5,6,7,8,9};
    ll x = b_search(v,10);
    cout << x << endl;
    ll y = b_search(v,9);
    cout << y << endl;

}
