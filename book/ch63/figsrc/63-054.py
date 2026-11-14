import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 31, 44, 24, 10, 'sujet', label=r'$\sqrt{3}\mapsto\sqrt{3}$', size='s')
box(ax, 57, 44, 24, 10, 'sujet', label=r'$\sqrt{3}\mapsto-\sqrt{3}$', size='s')
box(ax, 3, 28, 26, 14, 'sujet', label=r'$\sqrt{2}\mapsto\sqrt{2}$', size='s')
box(ax, 3, 12, 26, 14, 'sujet', label=r'$\sqrt{2}\mapsto-\sqrt{2}$', size='s')
cells = [['1', r'$\tau$'], [r'$\sigma$', r'$\sigma\tau$']]
for r in range(2):
    for c in range(2):
        box(ax, 31 + 26 * c, 28 - 16 * r, 24, 14, 'resultat', label=cells[r][c], size='l')
text(ax, 44, 5, r'$2\times2=4$ choix, les 4 existent', 'resultat', 'm')
save(fig, '63-054')
