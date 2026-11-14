import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
c = 2.8   # même taille de case partout : l'aire d'un groupe de cases = son nombre d'éléments

def cells(x, ytop, cols, rows, role):
    for i in range(cols):
        for j in range(rows):
            ax.add_patch(Rectangle((x + i * c, ytop - (j + 1) * c), c, c, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))

# S4 : facteurs 2, 3, 2, 2
text(ax, 7, 45.4, r'$S_4$', 'sujet', 'xl')
x = 20
for n in (2, 3, 2, 2):
    cells(x, 46, n, 1, 'resultat')
    text(ax, x + n * c / 2, 50, str(n), 'resultat', 'm')
    x += n * c + 7
text(ax, 44, 38, 'quatre facteurs, tous premiers', 'resultat', 's')

# S5 : facteurs 2 et 60 (60 = 10 colonnes x 6 rangées)
text(ax, 7, 21.6, r'$S_5$', 'sujet', 'xl')
cells(20, 23, 2, 1, 'resultat')
text(ax, 20 + c, 27, '2', 'resultat', 'm')
cells(40, 30, 10, 6, 'limite')
text(ax, 40 + 5 * c, 33.5, '60', 'limite', 'm')
text(ax, 54, 8, 'un facteur de 60 : pas premier', 'limite', 's')
save(fig, '64-142')
