import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 74, 80, r'pour $y=1$', 'resultat', 'm', weight='bold')
rows = [(58, 'sujet', r'$f$', r'$y^2-3y+2$', r'$1-3+2=0$'),
        (36, 'varie', r'$y\,g$', r'$y^2-y$', r'$1-1=0$'),
        (14, 'autre', r'$g$', r'$y-1$', r'$1-1=0$')]
for y, role, name, lab, res in rows:
    text(ax, 7, y + 6, name, role, 'l', weight='bold')
    box(ax, 14, y, 42, 12, role, label=lab, size='m')
    arrow(ax, (56, y + 6), (62, y + 6), 'fixe', lw=0.8)
    box(ax, 62, y, 24, 12, 'resultat', label=res, size='s')
arrow(ax, (35, 26), (35, 36), 'varie', lw=1.2)
text(ax, 38, 31, r'$\times\,y$', 'varie', 's', ha='left')
text(ax, 44, 6, r'1 annule $g$, donc 1 annule $y\,g$', 'resultat', 's')
save(fig, '70-029')
