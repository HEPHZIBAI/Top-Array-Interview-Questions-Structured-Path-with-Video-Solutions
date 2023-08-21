'''
https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
'''


def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    b=[]
    x=max(a)
    y=min(a)
    while(x in a):
        a.remove(x)
    while(y in a):
        a.remove(y)
    b.append(max(a))
    b.append(min(a))
    return b
    pass
