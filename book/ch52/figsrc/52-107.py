import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$M$ maximal $\Leftrightarrow$ $R/M$ corps','sujet','m')
rows=[(36,'(7) est maximal',r'$\mathbb{Z}/7\mathbb{Z}$ est un corps','3 × 5 = 15 = 1 (mod 7)','resultat'),(10,'(6) non maximal',r'$\mathbb{Z}/6\mathbb{Z}$ pas un corps','2 × 3 = 0 (mod 6)','limite')]
for y,a,b,ex,r in rows:
    box(ax,3,y,34,10,r,label=a,size='s')
    arrow(ax,(39,y+5),(47,y+5),'fixe',both=True)
    box(ax,49,y,36,10,r,label=b,size='s')
    text(ax,67,y-5,ex,r,'s')
save(fig,'52-107')
