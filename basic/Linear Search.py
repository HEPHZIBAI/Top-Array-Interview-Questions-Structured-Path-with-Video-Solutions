'''
https://www.codingninjas.com/studio/problems/linear-search_6922070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
'''



def linearSearch(n: int, num: int, arr: [int]) -> int:
    if num in arr:
        return(arr.index(num))
    else:
        return -1
    pass
