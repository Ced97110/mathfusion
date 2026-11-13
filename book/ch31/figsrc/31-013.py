import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
O=(34,31); R=26
A=(O[0]+R,O[1]); B=(O[0],O[1]+R)
disc(ax,*O,R,'fixe',fill=False,lw=0.7)
line(ax,[(O[0]-R-3,O[1]),(O[0]+R+9,O[1])],'fixe',lw=0.5); line(ax,[(O[0],O[1]-R-3),(O[0],O[1]+R+6)],'fixe',lw=0.5)
line(ax,[O,B],'sujet',lw=2.0); line(ax,[O,A],'fixe',lw=2.0)
disc(ax,*B,1.6,'sujet'); disc(ax,*A,1.4,'fixe'); disc(ax,*O,0.9,'encre')
disc(ax,O[0],O[1]-R,1.4,'fixe',fill=False)
text(ax,O[0]+3,O[1]-R-1,'sans lettre','fixe','s',ha='left')
text(ax,B[0]+4,B[1]+2,'B','sujet','l',weight='bold')
text(ax,A[0]+3.5,A[1]-3,'A','fixe','m')
text(ax,O[0]-2.5,O[1]-3,'O','encre','s')
text(ax,O[0]+3,O[1]+R/2,'1','sujet','m',ha='left')
text(ax,O[0]+R/2,O[1]+3,'1','fixe','m')
save(fig,'31-013')
