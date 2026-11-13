import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
u=4
def bal(y,left,right,cx=44):
    line(ax,[(4,y),(84,y)],'fixe',lw=1.2); poly(ax,[(cx,y),(cx-5,y-8),(cx+5,y-8)],'fixe')
    x=8
    for l,r,n in left:
        box(ax,x,y,n*u,10,r,label=l,size='m'); x+=n*u
    x=50
    for l,r,n in right:
        box(ax,x,y,n*u,10,r,label=l,size='m'); x+=n*u
bal(74,[(r'$x$','sujet',4),('3','fixe',3)],[('7','fixe',7)])
text(ax,22,61,r'$x+3=7$','encre','l'); text(ax,64,61,r'avec 4 : $4+3=7$','resultat','m')
arrow(ax,(44,54),(44,42),'varie'); text(ax,48,48,'retirer 3 des deux côtés','varie','s',ha='left')
bal(26,[(r'$x$','sujet',4)],[('4','fixe',4)])
text(ax,22,13,r'$x=4$','encre','l'); text(ax,64,13,r'avec 4 : $4=4$','resultat','m')
save(fig,'16-047')
