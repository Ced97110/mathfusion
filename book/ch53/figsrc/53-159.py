import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
U = 1.1   # côté d'un petit carré (mm) : un carré = un essai
def grille(x, y, cols, rows):
    for i in range(cols):
        for j in range(rows):
            ax.add_patch(Rectangle((x + i * U, y + j * U), U, U, fc=FILL['sujet'], ec=COL['sujet'], lw=0.25, zorder=2))
# 55 = 11 x 5 carrés ; 667 = 29 x 23 carrés (quantités exactes)
grille(2, 66, 11, 5)
text(ax, 20, 69, r'$n = 55$ : 55 essais', 'sujet', 's', ha='left')
grille(2, 34, 29, 23)
text(ax, 38, 47, r'$n = 667$ : 667 essais', 'sujet', 's', ha='left')
box(ax, 2, 10, 84, 15, 'fixe', dash=True, fill=False, label='600 chiffres : impossible')
text(ax, 44, 3.5, r'1 chiffre de plus : $\times 10$ essais', 'varie', 's')
save(fig, '53-159')
