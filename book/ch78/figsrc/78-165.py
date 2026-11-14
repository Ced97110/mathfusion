import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,54,r'$3 = 1 + 3m$ : essayer chaque $m$','sujet','m')
c=6.0;x0=18;y0=38
for k,(m,y) in enumerate(((0,38),(1,26),(2,14))):
    text(ax,10,y+c/2,rf'$m={m}$','encre','s')
    n=1+3*m
    for i in range(n):
        role='fixe' if i<1 else 'varie'
        poly(ax,[(x0+i*c,y),(x0+i*c+c,y),(x0+i*c+c,y+c),(x0+i*c,y+c)],role)
    text(ax,x0+n*c+3,y+c/2,rf'${n}$','limite','s',ha='left')
xt=x0+3*c
line(ax,[(xt,10),(xt,46)],'resultat',lw=1.2,dash=True)
text(ax,xt,48.5,r'but : $3$','resultat','s')
text(ax,44,6,'1 case du centre, 3 par classe','fixe','s')
save(fig,'78-165')
