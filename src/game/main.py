# -*- coding: utf-8 -*-

import os
import sys 
from game import ASSETS_DIR
from game import gegner 
from game import items 
from game import spieler 
import pandas as pd 
import pygame 

def create_gamefield() : 
    """ Gamefield 
        1111111111111
        1000000000001
        1000000000001
        1000000000001
        1111111111111
    """
    gamefield = {"row0" :  [], "row1" : [], "row2" : [], "row3" : [], "row4" : []}
    for x in range(5) :
        for y in range(13): 
            if x == 0 : 
                gamefield["row0"].append(1)
            elif x == 4: 
                gamefield["row4"].append(1)
            elif x != 4 or x !=0  : 
                gamefield[f"row{x}"].append(0)
                
    for key, value in gamefield.items():
        value[0] = 1 
        value[12] = 1 
        
    df = pd.DataFrame()
    df = df.from_dict(gamefield, orient='columns')
    
    return gamefield, df 


if __name__ == "__main__":
    print("Text adventure")

    x = None 
    y = None 
    gamer_positon = [x, y]
    
    gamefield_dict, gamefield_dataframe = create_gamefield()
    
    

    
                