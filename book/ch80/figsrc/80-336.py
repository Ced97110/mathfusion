import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'parties finies de $\mathbb{N}$', 'sujet', 'm')
f = numberline(ax, 30, 74, 12, 0, 9)
rows = ((56, r'$\{2, 5\}$', 'sujet', (2, 5)), (46, r'$\{7\}$', 'autre', (7,)), (36, 'réunion', 'resultat', (2, 5, 7)), (26, r'$\{5\}$', 'sujet', (5,)))
for y, lab, role, vals in rows:
    text(ax, 2, y, lab, role, 'm', ha='left')
    for v in vals: disc(ax, f(v), y, 2.2, role)
for v in (2, 5, 7): ax.plot([f(v), f(v)], [13, 56], color=COL['fixe'], lw=0.5, ls=':', zorder=1)
text(ax, 2, 18, r'sous $\{2,5\}$', 'fixe', 's', ha='left')
save(fig, '80-336')
