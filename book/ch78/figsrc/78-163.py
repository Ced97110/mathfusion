import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,71,'15 éléments non nuls','sujet','m')
text(ax,44,66.5,'un paquet = 3 éléments','fixe','s')
s=6.5;gx=3.5;gy=1.5;x0=(88-(5*s+4*gx))/2
for c in range(5):
    x=x0+c*(s+gx)
    box(ax,x-1,36.5,s+2,3*s+2*gy+3,'fixe',fill=False,dash=True,r=0.5)
    for r in range(3):
        box(ax,x,38+r*(s+gy),s,s,'sujet',r=0.4,label=None) if False else poly(ax,[(x,38+r*(s+gy)),(x+s,38+r*(s+gy)),(x+s,38+r*(s+gy)+s),(x,38+r*(s+gy)+s)],'sujet')
xe=x0+5*s+4*gx
brace(ax,x0,xe,34,'resultat',label=r'5 paquets $=15\div3$')
box(ax,10,7,68,10,'limite',label=r'8 éléments : $15\div7$')
text(ax,44,2.8,'pas un nombre entier','limite','s')
save(fig,'78-163')
