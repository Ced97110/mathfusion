import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
for y,a,b,t in [(46,18,34,'calcul 1 : 18 puis 34'),(34,34,18,'calcul 2 : 34 puis 18')]:
    box(ax,8,y,a,6,'fixe',label=str(a))
    box(ax,8+a,y,b,6,'fixe',label=str(b))
    text(ax,8,y+9,t,'encre','s',ha='left')
line(ax,[(60,22),(60,54)],'resultat',dash=True)
text(ax,63,48,'même résultat','resultat','s',ha='left')
box(ax,8,12,52,10,'resultat',label='52',size='l',lw=2.2)
text(ax,8,26,'le résultat seul, détaché du calcul','resultat','s',ha='left')
text(ax,63,19.5,'nom du résultat :','resultat','s',ha='left')
text(ax,63,14.5,'la somme','resultat','m',weight='bold',ha='left')
save(fig,'02-012')
