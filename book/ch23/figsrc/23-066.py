import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,16,74,'nombre sous la racine','encre','s')
text(ax,62,74,'solutions','encre','s')
rows=[(r'$D=136>0$',2,'deux solutions','resultat'),(r'$D=0$',1,'une solution','resultat'),(r'$D=-16<0$',0,'aucune solution','resultat')]
for i,(d,n,c,r) in enumerate(rows):
    y=58-i*14
    box(ax,2,y,30,10,'sujet',True,d)
    arrow(ax,(33,y+5),(40,y+5),'fixe')
    for k in range(n): disc(ax,46+k*7,y+5,2.2,'resultat')
    text(ax,60 if n==2 else (53 if n==1 else 44),y+5,c,'resultat','s',ha='left')
box(ax,2,12,30,10,'limite',True,r'$a=0,\ D=16$')
arrow(ax,(33,17),(40,17),'limite')
text(ax,42,17,'annonce 2, mais 1 seule','limite','s',ha='left')
text(ax,44,5,r'valable seulement si $a\neq0$','encre','s')
save(fig,'23-066')
