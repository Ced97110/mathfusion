import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 20, 49, 'tableau 2 × 2', 'fixe', 'm')
for (r, c, v, role) in [(0, 0, '2', 'sujet'), (0, 1, '1', 'varie'), (1, 0, '1', 'varie'), (1, 1, '2', 'sujet')]:
    box(ax, 6 + 13 * c, 28 - 13 * r, 12, 12, role, label=v, size='l')
text(ax, 62, 40, r'$2\times2=4$', 'sujet', 'm')
text(ax, 62, 30, r'$1\times1=1$', 'varie', 'm')
text(ax, 62, 20, r'$4-1=3$', 'resultat', 'l')
text(ax, 62, 10, 'déterminant', 'resultat', 's')
save(fig, '66-143')
