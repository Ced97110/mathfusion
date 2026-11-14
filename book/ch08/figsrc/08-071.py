import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
box(ax,14,46,60,7,'limite',fill=False,dash=True,label="chiffres d'avant : non relus",size='s')
rows=[(26,'reste 1',r'10 = 3$\times$3 + 1','chiffre 3, reste 1'),(8,'reste 2',r'20 = 3$\times$6 + 2','chiffre 6, reste 2')]
for y,a,b,c in rows:
    box(ax,2,y,18,10,'sujet',label=a,size='s'); arrow(ax,(20.3,y+5),(24,y+5),'fixe')
    box(ax,24,y,30,10,'fixe',label=b,size='s'); arrow(ax,(54.3,y+5),(58,y+5),'fixe')
    box(ax,58,y,28,10,'resultat',label=c,size='s')
text(ax,44,41,'seul le reste compte','encre','s')
save(fig,'08-071')
