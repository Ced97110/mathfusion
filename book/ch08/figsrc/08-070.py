import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
bw=18; g=4; x0=2; y=26; h=12
specs=[('sujet','reste 1'),('varie',r'$\times$10 : 10'),('fixe',r'10 = 3$\times$3 + 1'),('resultat','chiffre 3')]
for i,(r,l) in enumerate(specs):
    x=x0+i*(bw+g); box(ax,x,y,bw,h,r,label=l,size='s')
    if i<3: arrow(ax,(x+bw+0.3,y+h/2),(x+bw+g-0.3,y+h/2),'fixe')
xa=x0+bw/2; xb=x0+3*(bw+g)+bw/2
line(ax,[(xb,y-0.3),(xb,y-8),(xa+1.5,y-8)],'sujet',lw=1.1)
arrow(ax,(xa,y-8),(xa,y-0.3),'sujet',lw=1.1)
text(ax,(xa+xb)/2,y-12,'le reste revient','sujet','s')
text(ax,44,y+h+6,'un tour : le même calcul','encre','s')
text(ax,xb,y-4.5,'reste 1','sujet','s')
save(fig,'08-070')
