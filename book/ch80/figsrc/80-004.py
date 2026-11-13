import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
X=lambda i:24+(i-1)*2.1
rows=[(2,44,'sujet','30 ÷ 2 = 15'),(3,30,'autre','30 ÷ 3 = 10'),(5,16,'varie','30 ÷ 5 = 6')]
tot=0
for m,y,r,t in rows:
    text(ax,2,y,t,r,'s',ha='left')
    n=0
    for i in range(1,31):
        if i%m==0: disc(ax,X(i),y,0.9,r); n+=1
        else: disc(ax,X(i),y,0.35,'fixe')
    assert n==30//m
line(ax,[(X(1)-1,8),(X(30)+1,8)],'fixe',lw=0.5)
for v in (1,10,20,30): text(ax,X(v),4,str(v),'fixe','s')
text(ax,55,54,'multiples de 1 à 30','encre','s')
save(fig,'80-004')
