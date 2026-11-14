import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,66,r'$\sin^2 A=(\sin A)^2$','sujet','l')
s=40; x0=8; y0=8
box(ax,x0,y0,s,s,'fixe',fill=False,dash=True,r=0.01)
box(ax,x0,y0,0.6*s,0.6*s,'sujet',label=r'$0{,}36$',r=0.01)
text(ax,x0+s,y0-3,'1','fixe','s',ha='center')
text(ax,x0+0.3*s,y0-3,'0,6','sujet','s')
text(ax,x0-3.5,y0+0.3*s,'0,6','sujet','s')
text(ax,68,40,r'$\sin A=0{,}6$','sujet','m')
text(ax,68,31,r'$0{,}6\times0{,}6$','varie','m')
text(ax,68,22,'= 0,36','resultat','m')
save(fig,'26-039')
