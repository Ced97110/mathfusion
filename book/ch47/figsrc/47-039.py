import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,16,44,18,13,'sujet',label='g',size='l'); box(ax,36,44,18,13,'fixe',label='h',size='l')
text(ax,70,50.5,'gh : g à gauche','sujet','s',ha='center') if False else None
arrow(ax,(14,50.5),(3,50.5),'varie')
text(ax,62,52,'g écrit à gauche','varie','s',ha='left')
text(ax,62,47,'de chaque h','varie','s',ha='left')
box(ax,16,10,18,13,'sujet',label='r',size='l'); box(ax,36,10,18,13,'fixe',label='s',size='l')
arrow(ax,(25,43),(25,24),'fixe'); arrow(ax,(45,43),(45,24),'fixe')
text(ax,62,20,'g = r','sujet','s',ha='left'); text(ax,62,13,'h = s','fixe','s',ha='left')
text(ax,35,4,'on écrit rs : classe à gauche','resultat','s') if False else None
save(fig,'47-039')
