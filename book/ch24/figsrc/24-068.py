import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
s=5
text(ax,4,79,'eau calme','fixe','s',ha='left')
box(ax,4,67,10*s,8,'sujet',label=r'$v = 10$')
text(ax,4,60,'descente : le courant s\'ajoute','varie','s',ha='left')
box(ax,4,48,10*s,8,'sujet',label=r'$v$'); box(ax,4+10*s,48,2*s,8,'varie',label=r'$c$')
text(ax,4+12*s+10,52,'12 km/h','sujet','m')
text(ax,4,41,'montée : le courant se retranche','varie','s',ha='left')
box(ax,4,29,8*s,8,'sujet',label=r'$v - c$'); box(ax,4+8*s,29,2*s,8,'varie',fill=False,dash=True,label=r'$c$')
text(ax,4+10*s+14,33,'8 km/h','sujet','m')
text(ax,4,19,'$c = 2$ km/h (flèche orange)','varie','s',ha='left')
box(ax,4,4,80,9,'resultat',label=r'$10 + 2 = 12$ ; $10 - 2 = 8$')
save(fig,'24-068')
