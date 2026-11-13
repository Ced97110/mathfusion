import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,4,50,36,10,'sujet',label=r'$\mathrm{PGCD}(a,\ b)$')
arrow(ax,(41,55),(55,55),'varie'); text(ax,48,59,'écrit','varie','s')
box(ax,56,50,28,10,'resultat',label=r'$d$',size='l')
text(ax,44,43,'une lettre pour le PGCD','fixe','s')
for y,a,b,d in [(30,'12','18','6'),(10,'252','198','18')]:
    box(ax,4,y,36,10,'fixe',label=r'$a=%s,\ b=%s$'%(a,b))
    arrow(ax,(41,y+5),(55,y+5),'varie')
    box(ax,56,y,28,10,'resultat',label=r'$d=%s$'%d)
save(fig,'05-098')
