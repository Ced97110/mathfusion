import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax,44,64,'une vérification : un angle à la fois','fixe','s')
f=numberline(ax,8,76,50,0,120,step=20,arrow_right=False,size='s')
for a in (35,60):
    disc(ax,f(a),50,2.6,'varie'); text(ax,f(a),57,f'{a}°','varie','s')
text(ax,44,36,'une identité : tous les angles d’un coup','resultat','s')
f=numberline(ax,8,76,24,0,120,step=20,arrow_right=False,size='s')
box(ax,8,21.5,68,5,'resultat',fill=True)
text(ax,44,10,'(les angles où les deux côtés ont un sens)','fixe','s')
save(fig,'31-010')
