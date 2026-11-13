import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, 'matrice d’un homomorphisme', 'encre', 's')
def grid(x0, y0, vals, roles, s=12):
    for k, (v, r) in enumerate(zip(vals, roles)):
        i, j = k % 2, k // 2
        box(ax, x0 + i * s, y0 - j * s, s - 0.8, s - 0.8, r, label=v, size='m')
roles1 = ('sujet', 'varie', 'varie', 'sujet')
grid(8, 32, ('2', '1', '1', '3'), roles1)
roles2 = ('sujet', 'fixe', 'fixe', 'sujet')
grid(58, 32, ('d₁', '0', '0', 'd₂'), roles2)
arrow(ax, (34, 26), (54, 26), 'encre', lw=1.2)
text(ax, 44, 33, 'bases de départ', 'encre', 's')
text(ax, 44, 21, 'et d’arrivée', 'encre', 's')
text(ax, 20, 46, 'nombres partout', 'varie', 's')
text(ax, 70, 46, 'rien hors diagonale', 'resultat', 's')
box(ax, 8, 2, 72, 8, 'sujet', label='sur ℤ ou K[x] : anneau principal', size='s')
save(fig, '58-329')
