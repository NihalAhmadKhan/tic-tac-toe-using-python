import random as r
m=[" "," "," "," "," "," "," "," "," "]
u=[]
com=[]
a=-1
l=[1,2,3,4,5,6,7,8,9]
win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def ingrid():
    print('''
          1 |  2 |  3
        ____|____|____
          4 |  5 |  6
        ____|____|____
          7 |  8 |  9
            |    |
        
THIS IS THE MAPPING OF THE NUMBERS WITH THE POSITION IN GRID......CHOOSE ACCORDINGLY
        ''')
def grid(a,b,c,d,e,f,g,h,i):
      s='''
      {} |  {} |  {}
    ____|____|____
      {} |  {} |  {}
    ____|____|____
      {} |  {} |  {}
        |    |
        '''
      s=s.format(a,b,c,d,e,f,g,h,i)
      print(s)
def move(c,xyz,ch):
      if c in l:
           xyz.append(c)
           xyz.sort()
           l.remove(c)
           m[c-1]=ch
           b=1
           return b
      else:
           print("MOVE NOT POSSIBLE PLEASE USE ANOTHER MOVE")
def playermove(ch):
      while True:
         c=int(input("ENTER YOUR MOVE FROM 1 TO 9 :"))
         ch3=move(c,u,ch)
         if ch3==1:
           break
def computermove(ch):
      cm=r.choice(l)
      com.append(cm)
      com.sort()
      m[cm-1]=ch
      print("COMPUTER CHOOSES ",cm)
      l.remove(cm)
def p1move(ch):
      while True:
         c=int(input("[PLAYER 1] ENTER YOUR MOVE FROM 1 TO 9 :"))
         ch3=move(c,u,ch)
         if ch3==1:
           break
def p2move(ch):
      while True:
         c=int(input("[PLAYER 2] ENTER YOUR MOVE FROM 1 TO 9 :"))
         ch3=move(c,com,ch)
         if ch3==1:
           break   
def Win(u):
      a=0
      for i in range(len(win)):
        if (len(u)>=len(win[0])) and (win[i][0] in u) and (win[i][1] in u) and (win[i][2] in u):
          a=1
      return a
ch=input('''************************ WELCOME TO TIC TAC TOE GAME ***************************
READY TO PLAY THE GAME?
1. YES
2. NO

ENTER YOUR CHOICE :''')
if ch=="1":
    while True:
      ch1=int(input('''
CHOOSE YOUR MODE
1. PLAYER VS COMPUTER
2. PLAYER VS PLAYER
    
ENTER YOUR CHOICE :'''))
      if ch1!=1 and ch1!=2:
        print("INVALID INPUT")
      else:
        break
    while True:
      ch2=int(input('''
CHOOSE YOUR SYMBOL
1. X
2. O
        
ENTER YOUR CHOICE :'''))
      if ch2!=1 and ch2!=2:
        print("INVALID INPUT")
      else:
        break  
    while True: 
      ingrid()
      m=[" "," "," "," "," "," "," "," "," "]
      l=[1,2,3,4,5,6,7,8,9]
      u.clear()
      com.clear()
      a=-1
      while True:
        if ch1==1 and ch2==1:
          i,j="X","O"
          playermove(i)
          ch4=Win(u)
          if ch4==1:
            grid(*m)
            a=1
            break
          if len(l)==0:
            break
          computermove(j)
          grid(*m)
          ch5=Win(com)
          if ch5==1:
            a=0
            break
        elif ch1==1 and ch2==2:
          j,i="X","O"
          computermove(j)
          grid(*m)
          ch5=Win(com)
          if ch5==1:
            a=0
            break
          if len(l)==0:
            break
          playermove(i)
          grid(*m)
          ch4=Win(u)
          if ch4==1:
            a=1
            break
        elif ch1==2 and ch2==1:
          i,j="X","O"
          p1move(i)
          grid(*m)
          ch4=Win(u)
          if ch4==1:
            a=2
            break
          if len(l)==0:
            break
          p2move(j)
          grid(*m)
          ch5=Win(com)
          if ch5==1:
            a=3
            break
        elif ch1==2 and ch2==2:
          j,i="X","O"
          p2move(j)
          grid(*m)
          ch5=Win(com)
          if ch5==1:
            a=3
            break
          if len(l)==0:
            break
          p1move(i)
          grid(*m)
          ch4=Win(u)
          if ch4==1:
            a=2
            break
      if a==1:
        print("YOU WON THE GAME")
      elif a==0:
        print("COMPUTER WON THE GAME")
      elif a==2:
        print("PLAYER 1 WON THE GAME")
      elif a==3:
        print("PLAYER 2 WON THE GAME")
      else:
        print("Game Draw")
      while True:
        ch6=int(input(
           '''
WANT TO PLAY AGAIN WITH SAME PREFERENCES?
1. YES
2. NO
         
ENTER YOUR CHOICE :'''
        ))
        if ch6==2 or ch6==1:
           break
        else:
           print("INVALID INPUT")
      if ch6==2:
       break
    print("\n\nTHANK YOU FOR PLAYING TIC TAC TOE")
else:
  print("\n\nTHANK YOU FOR PLAYING TIC TAC TOE")
