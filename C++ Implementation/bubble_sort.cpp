#include<bits/stdc++.h>

using namespace std;


void bubble_sort(vector<int>&v){

    for(int i=0; i<v.size()-1; i++)
    {
        bool swp = false;
        for (int j=0; j<v.size()-i-1; j++)
        {
            if(v[j]>v[j+1])
            {
                swap(v[j],v[j+1]);
                swp = true;
            }

        }
        if (swp == false){
            break;
        }

    }

}

int main()
{
    vector<int> v = {1,2,3,4,5,6,7,8,9};
    sort(v.begin(),v.end(),greater<int>());
    for(int i=0; i<v.size(); i++)
    {
        cout << v[i] << endl;
    }
    bubble_sort(v);
    for(int i=0; i<v.size(); i++)
    {
        cout << v[i] << endl;
    }


}
