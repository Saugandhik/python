# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:52:55 2020

@author: saugandhik
"""

def displayBoard(gameList):
    for i in range(0,3):
        op_str=''
        for j in range(0,3):
            op_str=op_str+gameList[i][j]+" | "
        print(op_str)

def checkrow(gameList,pos):#pos =[row,col]
    if len(set(gameList[pos[0]]))==1 and set(gameList[pos[0]])!={'#'}:
        return True
    else:
        return False

def checkcol(gameList,pos):
    gameList_t=list(zip(*gameList))
    if len(set(gameList_t[pos[1]]))==1 and set(gameList_t[pos[1]])!={'#'}:
        return True
    else:
        return False
    
def checkdiag(gameList,pos):
    if pos==[1,1]:
        n_ls1=set([gameList[0][0],gameList[1][1],gameList[2][2]])
        n_ls2=set([gameList[0][2],gameList[1][1],gameList[2][0]])
        
        if(len(n_ls1)==1 and n_ls1!={'#'}):
            return True
        elif(len(n_ls2)==1 and n_ls2!={'#'}):
            return True
        else:
            return False
    else:
        if pos[0]==pos[1]:
            n_ls1=set([gameList[0][0],gameList[1][1],gameList[2][2]])
            if(len(n_ls1)==1 and n_ls1!={'#'}):
                return True
            else:
                return False
        else:
            n_ls2=set([gameList[0][2],gameList[1][1],gameList[2][0]])
            if(len(n_ls2)==1 and n_ls2!={'#'}):
                return True
            else:
                return False

        
def gameCheck(gameList,newPosition):#pos =[row,col]
        if(checkrow(gameList,newPosition)):
            return True
        elif(checkcol(gameList,newPosition)):
            return True
        elif(checkdiag(gameList,newPosition)):
            return True
        else:
            return False

def demoBoard():
    print("Please input the cell number where u want to put ur O/X")
    cnt=0
    for i in range(0,3):
        op_str=''
        for j in range(0,3):
            op_str=op_str+str(cnt)+" | "
            cnt+=1
        print(op_str)
        
def gameListMod(gameList,newPosition,p):
    gameList[newPosition[0]][newPosition[1]]=p
    return gameList

def getposition(ti):
    pos_2d=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    return pos_2d[ti]
    
        
def gameRunner():
    while True:
        gameList=[['#','#','#'],
                  ['#','#','#'],
                  ['#','#','#']]
        print("Starting TIC TAC")
        player1=input("Please entr 'O' or 'X': ")
        print(f'Player1 = {player1}')
        if(player1=='O'):
            player2='X'
        else:
            player2='O'
        print(f'Player2 = {player2}')
        x=1
        used_ti=[]
        for i in range(0,9):
            demoBoard()
            print(used_ti)
            print(f'Player {abs(x)}\'s Turn : ')
            while True:
                ti=int(input('Input the Cell number : '))
                if ti not in used_ti:
                    used_ti.append(ti)
                    break
                else:
                    print("Already used input. Please try again")
            
            newPosition=getposition(ti)
            if abs(x)==1:
                gameList=gameListMod(gameList,newPosition,player1)
            else:
                gameList=gameListMod(gameList,newPosition,player2)
            displayBoard(gameList)
            if(gameCheck(gameList,newPosition)):
                print(f'Player {abs(x)} WINS')
                break
            x=~x #complement of x
        if(input("ENTER E to Exit : ")=='E'):
            break
        else:
            print("lets Play again")
            #break
            
gameRunner()
    
