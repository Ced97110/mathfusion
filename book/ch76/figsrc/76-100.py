import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 11, 54, r'$\times$', 'encre', 'l')
text(ax, 34, 54, r'$1$', 'sujet', 'm'); text(ax, 58, 54, r'$4i$', 'sujet', 'm')
text(ax, 11, 45, r'$2$', 'autre', 'm'); text(ax, 11, 33, r'$3i$', 'autre', 'm')
cells = [(0, 0, r'$2$'), (0, 1, r'$8i$'), (1, 0, r'$3i$'), (1, 1, r'$-12$')]
for r, c, s in cells:
    key = (r, c) == (1, 1)
    box(ax, 22 + 24 * c, 40 - 12 * r, 24, 10, 'varie' if key else 'fixe', label=s, weight='bold' if key else 'normal')
text(ax, 58, 22, r'$3i\times4i=12\,i\times i$, $i\times i=-1$', 'varie', 's')
box(ax, 4, 4, 80, 12, 'resultat', label=r'$2+8i+3i-12=-10+11i$')
save(fig, '76-100')
