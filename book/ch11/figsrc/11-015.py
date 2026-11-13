import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cm = 6.0; po = 2.54 * cm
box(ax, 6, 44, 4 * po, 6, 'sujet', r=0.3, label='le même ruban', size='s')
box(ax, 6 + 0, 28, po, 6, 'autre', r=0.3)
text(ax, 6 + po + 3, 31, 'unité : po', 'autre', 's', ha='left')
text(ax, 62, 31, 'on compte 4', 'autre', 'm')
box(ax, 6, 14, cm, 6, 'varie', r=0.3)
text(ax, 6 + cm + 3, 17, 'unité : cm', 'varie', 's', ha='left')
text(ax, 62, 17, 'on compte 10,16', 'varie', 'm')
text(ax, 44, 5, 'le po est 2,54 fois plus long', 'resultat', 's')
save(fig, '11-015')
