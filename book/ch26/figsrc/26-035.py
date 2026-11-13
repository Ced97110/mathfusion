import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=1.6; x0=6
box(ax,x0,44,30*u,9,'sujet',label='échelle : 30 m')
box(ax,x0,30,36*u,9,'limite',label='hauteur lue : 36 m')
box(ax,x0,16,26*u,9,'resultat',label='hauteur juste : 26 m')
line(ax,[(x0+30*u,12),(x0+30*u,56)],'fixe',dash=True)
text(ax,x0+30*u,60,'limite : 30 m','fixe','s')
text(ax,44,5,r'$36\div30=1{,}2>1$ : erreur','limite','m')
save(fig,'26-035')
