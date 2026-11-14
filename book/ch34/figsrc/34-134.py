import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 3, 52, 38, 18, 'sujet', label=r'$\frac{\sqrt{6}+\sqrt{2}}{4}$', size='l')
box(ax, 47, 52, 38, 18, 'autre', label=r'$\frac{\sqrt{2+\sqrt{3}}}{2}$', size='l')
for x, role in ((22, 'sujet'), (66, 'autre')):
    arrow(ax, (x, 51.5), (x, 36), 'varie')
    text(ax, x + 2, 43.5, 'au carré', 'varie', 's', ha='left')
box(ax, 3, 18, 38, 17, 'sujet', label=r'$\frac{2+\sqrt{3}}{4}$', size='l')
box(ax, 47, 18, 38, 17, 'autre', label=r'$\frac{2+\sqrt{3}}{4}$', size='l')
text(ax, 44, 26.5, '=', 'resultat', 'xl', weight='bold')
box(ax, 14, 2, 60, 11, 'resultat', label='positifs : nombres égaux', size='s')
arrow(ax, (44, 17.5), (44, 13.5), 'resultat')
save(fig, '34-134')
