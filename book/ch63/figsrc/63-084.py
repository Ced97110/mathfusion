import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 19, 76, r'$[E:F]$ : degré', 'autre', 'm')
text(ax, 67, 76, r'$|G|$ : éléments de $G$', 'sujet', 'm')
text(ax, 44, 67, r'$G=\{1,\sigma\}$, $F=\mathrm{Inv}\,G=\mathbb{Q}$', 'fixe', 's')
for k, lab in enumerate([r'$1$', r'$\sqrt{2}$']):
    box(ax, 6 + k * 14, 44, 12, 14, 'autre', label=lab, size='s')
for k, lab in enumerate([r'$1$', r'$\sigma$']):
    box(ax, 54 + k * 14, 44, 12, 14, 'sujet', label=lab, size='s')
text(ax, 44, 51, r'$\leq$', 'resultat', 'l')
text(ax, 44, 31, r'$G=\{1\}$, $F=\mathrm{Inv}\,G=E$', 'fixe', 's')
box(ax, 6, 8, 12, 14, 'autre', label=r'$1$', size='s')
box(ax, 54, 8, 12, 14, 'sujet', label=r'$1$', size='s')
text(ax, 44, 15, r'$\leq$', 'resultat', 'l')
save(fig, '63-084')
