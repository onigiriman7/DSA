#include <bits/stdc++.h>
using namespace std;
struct minmax
{
    int min;
    int max;
};
struct minmax maxmin(int arr[], int n)//n = length of array
{
    int max = arr[0];
    int min = arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>max) max =arr[i];
        if(arr[i]<min) min = arr[i];
    }
    struct minmax result;
    result.max = max;
    result.min = min;
    return result;
}