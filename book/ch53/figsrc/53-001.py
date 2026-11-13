import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 3, 40, 17, 10, 'sujet', label='Léa')
box(ax, 68, 40, 17, 10, 'resultat', label='Vendeur')
n, w, x0, x1 = 10, 3.4, 22.0, 66.0
gap = (x1 - x0 - n * w) / (n - 1)
for k in range(n):
    box(ax, x0 + k * (w + gap), 41, w, 8, 'fixe', r=0.5)
arrow(ax, (11.5, 51), (76.5, 51), 'varie', curve=-0.25)
text(ax, 44, 61, 'numéro de carte', 'varie')
brace(ax, x0, x1, 38, 'fixe', label='10 ordinateurs : tous lisent')
text(ax, 44, 26, 'seul le vendeur peut lire', 'encre')
box(ax, 4, 6, 38, 10, 'fixe', label='ordinateurs : illisible')
box(ax, 46, 6, 38, 10, 'resultat', label='vendeur : peut lire')
save(fig, '53-001')
