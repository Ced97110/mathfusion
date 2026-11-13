import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
def bar(y,n,role,fill=True,x0=26,dash=False):
    for j in range(n): box(ax,x0+9*j,y,9,7,role,fill=fill,lw=0.6,r=0.5,dash=dash)
text(ax,44,77,r'$m=2$ et $n=3$','encre','m',weight='bold')
text(ax,23,65.5,r'$mn=6$','sujet','m',ha='right'); bar(62,6,'sujet')
text(ax,23,55.5,'PPCM = 6','resultat','m',ha='right'); bar(52,6,'resultat')
text(ax,44,44,r'PGCD = 1 : $\cong\mathbb{Z}/6$','resultat','m')
line(ax,[(4,39),(84,39)],'fixe',lw=0.5)
text(ax,44,33,r'$m=2$ et $n=2$','encre','m',weight='bold')
text(ax,23,25.5,r'$mn=4$','sujet','m',ha='right'); bar(22,4,'sujet')
text(ax,23,15.5,'PPCM = 2','limite','m',ha='right'); bar(12,2,'limite'); bar(12,2,'fixe',fill=False,x0=26+18,dash=True)
text(ax,44,5,r'PGCD = 2 : pas $\cong\mathbb{Z}/4$','limite','m')
save(fig,'45-192')
