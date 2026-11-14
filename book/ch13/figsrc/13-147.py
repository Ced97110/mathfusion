import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 22, 70, 'entiers relatifs', 'sujet', 'm'); text(ax, 66, 70, 'fractions', 'autre', 'm')
box(ax, 4, 50, 36, 10, 'sujet', label=r'$(3,5)\sim(10,12)$', size='s')
box(ax, 48, 50, 36, 10, 'autre', label=r'$(1,2)\sim(2,4)$', size='s')
for x, r, t in [(22, 'sujet', 'en croix'), (66, 'autre', 'en croix')]:
    arrow(ax, (x, 49), (x, 38), r); text(ax, x + 2, 43.5, t, r, 's', ha='left')
box(ax, 4, 26, 36, 11, 'sujet', label=r'$3+12=5+10$', size='s')
box(ax, 48, 26, 36, 11, 'autre', label=r'$1\times4=2\times2$', size='s')
text(ax, 22, 20, 'sommes égales', 'varie', 's'); text(ax, 66, 20, 'produits égaux', 'varie', 's')
text(ax, 44, 8, 'même procédé, autre opération', 'varie', 's')
save(fig, '13-147')
