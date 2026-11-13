import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
# départ
box(ax, 4, 86, 80, 14, 'fixe')
text(ax, 44, 96, r'départ : $f=qg+r=q_1g+r_1$', 'fixe', 's')
text(ax, 44, 90, r'deux écritures de la division', 'fixe', 's')
arrow(ax, (44, 86), (44, 78), 'varie')
# étape qui porte la preuve
box(ax, 4, 34, 80, 44, 'varie', lw=1.6)
text(ax, 44, 73, r'étape : soustraire les deux écritures', 'varie', 's')
box(ax, 8, 58, 33, 11, 'sujet', label=r'$(q-q_1)\,g$', size='m')
text(ax, 44.5, 63.5, '=', 'varie', 'l')
box(ax, 48, 58, 33, 11, 'autre', label=r'$r_1-r$', size='m')
# degrés : axe commun, repère m
xm = 52
line(ax, [(xm, 38), (xm, 55)], 'fixe', dash=True, lw=0.9)
text(ax, xm, 56.5, r'$m$', 'fixe', 's')
arrow(ax, (10, 49), (76, 49), 'sujet', lw=2.0)
text(ax, 78, 49, r'$\geq m$', 'sujet', 's', ha='left')
arrow(ax, (10, 42), (44, 42), 'autre', lw=2.0)
text(ax, 46, 42, r'$<m$', 'autre', 's', ha='left')
arrow(ax, (44, 34), (44, 26), 'varie')
# arrivée
box(ax, 4, 4, 80, 22, 'resultat')
text(ax, 44, 20, 'égaux seulement si les deux sont nuls', 'resultat', 's')
text(ax, 44, 11, r'donc $q=q_1$ et $r=r_1$', 'resultat', 'm')
save(fig, '54-159')
