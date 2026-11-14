import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 14, 26, 44, 'sujet', fill=False); text(ax, 15, 62, r'$G$', 'sujet', 'm')
box(ax, 60, 14, 26, 44, 'autre', fill=False); text(ax, 73, 62, r"$G'$", 'autre', 'm')
for i in range(4):
    y = 50 - 10 * i
    disc(ax, 15, y, 4, 'sujet' if i == 3 else 'fixe', label=str(i), size='s')
    disc(ax, 73, y, 4, 'autre' if i == 3 else 'fixe', label=r'$r_%d$' % i, size='s')
arrow(ax, (19.5, 20), (68.5, 20), 'varie', lw=1.6); text(ax, 44, 24, r'$\eta$', 'varie', 'm')
text(ax, 44, 7, r'$\eta(3)=r_3$ : nom neuf de 3', 'resultat', 's')
save(fig, '45-030')
