# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:25:59 2018

@author: Ankita
"""

def printmov(fr,to):
    print('Move from ' + str(fr)+ ' to ' + str(to))
    
def Tower(n,fr,to,spare):
    if n==1:
        printmov(fr,to)
    else:
        Tower(n-1,fr,spare,to)
        Tower(1,fr,to,spare)
        Tower(n-1,spare,to,fr)
        
Tower(5,'In','Final','Aux')
    

