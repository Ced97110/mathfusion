import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,3,52,40,12,'fixe',label='le morceau de la base',size='s')
arrow(ax,(43.5,58),(57.5,58),'varie'); text(ax,50.5,62,'s’écrit','varie','s')
box(ax,58,52,26,12,'resultat',label=r'$P$',size='l')
for y,a,b in [(28,'30 % de 50 €','15 €'),(8,'20 % de 80 €','16 €')]:
    box(ax,3,y,34,12,'fixe',label=a); arrow(ax,(37.5,y+6),(49.5,y+6),'varie'); box(ax,50,y,34,12,'resultat',label=rf'$P$ = {b}')
save(fig,'09-089')
