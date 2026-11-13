import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,18,60,'condition','fixe','s')
text(ax,48,60,r'$d=6$','resultat','m',weight='bold')
text(ax,74,60,r'$d=3$','autre','m',weight='bold')
tags=[r'$d>0$',r'$d\mid a$ et $d\mid b$',r"tout $d'$ : $d'\mid d$"]
good=[r'$6>0$',r'$6\mid 12$ et $6\mid 18$',r'$1,2,3\mid 6$']
bad=[r'$3>0$',r'$3\mid 12$ et $3\mid 18$',r'$6\nmid 3$']
for i in range(3):
    y=44-i*15
    box(ax,2,y,32,11,'fixe',label=tags[i],size='s')
    box(ax,36,y,24,11,'resultat',label=good[i],size='s')
    box(ax,62,y,24,11,'resultat' if i<2 else 'limite',label=bad[i],size='s')
save(fig,'05-106')
