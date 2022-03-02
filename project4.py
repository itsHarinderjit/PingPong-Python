from graphics import *
import random
import math

speed=30

l=random.randrange(1,19,1)
b=math.sqrt(20**2-l**2)
g=random.choice([1,-1])
h=random.choice([1,-1])
b=b*g
l=l*h

screen=GraphWin("Screen",1600,800)      
screen.setBackground("black")

player=Rectangle(Point(600,710),Point(720,730))
player.setFill("white")
player.draw(screen)

comp=Rectangle(Point(600,20),Point(720,40))
comp.setFill("white")
comp.draw(screen)

ball=Circle(Point(660,375),10)
ball.setFill("white")
ball.draw(screen)

mainrec=Rectangle(Point(10,10),Point(1310,740))
mainrec.setOutline("white")
mainrec.setWidth(5)
mainrec.draw(screen)

rec=Rectangle(Point(1320,10),Point(1535,740))
rec.setOutline("white")
rec.setWidth(5)
rec.draw(screen)

line1=Line(Point(1320,55),Point(1535,55))
line1.setOutline("white")
line1.setWidth(5)
line1.draw(screen)

line2=Line(Point(1320,65),Point(1535,65))
line2.setOutline("white")
line2.setWidth(5)
line2.draw(screen)

t=Text(Point(1425,30),"Ping Pong")
t.setTextColor("white")
t.setSize(25)
t.setFace('courier')
t.setTextColor('white')
t.setStyle('bold')
t.draw(screen)

def print_result(flag):
    if(flag==1):
        res=Text(Point(650,350),'You Won')
        res.setTextColor("white")
        res.setSize(50)
        res.setFace('courier')
        res.setTextColor('white')
        res.setStyle('bold')
        res.draw(screen)
    else:
        res=Text(Point(650,350),'You Lose')
        res.setTextColor("white")
        res.setSize(50)
        res.setFace('courier')
        res.setTextColor('white')
        res.setStyle('bold')
        res.draw(screen)

def ball_move(x,y):
    ball.move(l*0.025*x,b*0.025*y)
    

def player_move(key):
    P1=player.getP1()
    P2=player.getP2()
    if key==None:
        return
    if ((P1.getX() < 60 and key=='Left') or (P2.getX() >1260 and key=='Right')):
        return
    if key=='Left':
        player.move(-speed,0)
    if key=='Right':
        player.move(speed,0)
    
def comp_move():
    pos=ball.getCenter()
    c1=comp.getP1()
    c2=comp.getP2()
    X=(40-pos.getY())/(b/l)+pos.getX()
    center=(c1.getX()+c2.getX())/2
    if c1.getX()<20 :
        comp.move(2,0)
    if c2.getX()>1300 :
        comp.move(-2,0)
    if X == center:
        return
    if X < center:
        comp.move(-0.5,0)
    if X > center:
        comp.move(0.5,0)
    
def main():
    global l,b
    x=1.0001
    y=1.0001
    flag=0
    screen.getKey()
    while True:
        ball_move(x,y)
        key=screen.checkKey()
        player_move(key)
        comp_move()
        pos=ball.getCenter()
        P1=player.getP1()
        P2=player.getP2()
        c1=comp.getP1()
        c2=comp.getP2()
        player_center=(P1.getX()+P2.getX())/2
        comp_center=(c1.getX()+c2.getX())/2
        if pos.getX()<20 or pos.getX()>1300 :
            l=-l
        if pos.getY()>700 :
            if player_center-20 <= pos.getX() <= player_center+20:
                b=-b
            elif player_center-40 <= pos.getX() <= player_center+40:
                if b>19 :
                    b=-b+1
                b=-b-1
                l=math.sqrt(20**2-b**2)
            elif player_center-70 <= pos.getX() <= player_center+70 :
                if b>18 :
                    b=-b+2
                b=-b-2
                l=math.sqrt(20**2-b**2)
            else:
                break
        elif  pos.getY()<50 :
            b=-b
            if pos.getX() > c1.getX() and pos.getX() < c2.getX():
                continue
            else:
                flag=1
                break
        x+=0.00001
        y+=0.00001

    print_result(flag)
    screen.getKey()               
    screen.close()
    #main end

if __name__ == '__main__' :
    main()
