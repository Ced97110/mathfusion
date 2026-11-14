import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 63, r'$\sqrt{3}$ garde', 'encre', 'm')
text(ax, 70, 63, r'$\sqrt{3}$ change', 'encre', 'm')
text(ax, 29, 45, r'$\sqrt{2}$ garde', 'encre', 'm', ha='right')
text(ax, 29, 27, r'$\sqrt{2}$ change', 'encre', 'm', ha='right')
cells = [[('1', 'fixe'), (r'$\tau$', 'varie')], [(r'$\sigma$', 'varie'), (r'$\sigma\tau$', 'varie')]]
for i in range(2):
    for j in range(2):
        lab, role = cells[i][j]
        box(ax, 32 + 26 * j, 38 - 18 * i, 24, 14, role, label=lab, size='l')
text(ax, 44, 8, r'$2\times2=4$ combinaisons', 'resultat', 'm')
save(fig, '63-017')
