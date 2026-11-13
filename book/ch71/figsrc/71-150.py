import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(60)
text(ax,4,55,'base orthogonale pour $B$','encre','m',ha='left')
o=(22,30); d=14
arrow(ax,o,(o[0]+d,o[1]+d),'sujet'); arrow(ax,o,(o[0]+d,o[1]-d),'autre')
text(ax,o[0]+d+3,o[1]+d+2,r'$u_1$','sujet','m'); text(ax,o[0]+d+3,o[1]-d-2,r'$u_2$','autre','m')
k=3.5*math.sqrt(0.5)
line(ax,[(o[0]+k,o[1]+k),(o[0]+2*k,o[1]),(o[0]+k,o[1]-k)],'fixe')
text(ax,o[0]+8,o[1],r'$B(u_1,u_2)=0$','resultat','s',ha='left')
text(ax,70,50,'matrice de $B$','encre','m')
box(ax,57,32,13,12,'sujet',label='2'); box(ax,71,32,13,12,'resultat',label='0')
box(ax,57,18,13,12,'resultat',label='0'); box(ax,71,18,13,12,'sujet',label='2')
text(ax,70,12,r'diag$(2,\,2)$','encre','m')
save(fig,'71-150')
