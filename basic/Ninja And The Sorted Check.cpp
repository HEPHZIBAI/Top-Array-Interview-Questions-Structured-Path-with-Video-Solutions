/*
https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
*/



int isSorted(int n, vector<int> a) 
{
    // Write your code here.
    int f=1;
    for(int i=0;i<n-1;i++)
    {
        if(a[i]>a[i+1])
        {
            f=0;
            break;
        }
    }
    return f;
}
