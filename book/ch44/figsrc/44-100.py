import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, "un monoïde : on regarde chaque élément", 'encre', 's')
text(ax, 4, 54, 'carreau : 8 mouvements', 'resultat', 's', ha='left')
for i in range(8):
    x = 8 + i * 10.5
    disc(ax, x, 44, 3.6, 'resultat', label='✓', size='s')
text(ax, 44, 34, 'les 8 se défont : un groupe', 'resultat', 'm')
text(ax, 4, 24, 'compteur de passages', 'limite', 's', ha='left')
for i in range(5):
    disc(ax, 8 + i * 10.5, 14, 3.6, 'limite', label='✗', size='s')
text(ax, 64, 14, '...', 'limite', 'l')
text(ax, 44, 4, 'aucun ne se défait : pas un groupe', 'limite', 's')
save(fig, '44-100')
