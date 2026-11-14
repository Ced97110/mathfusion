import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$\sigma(3)=3$ et $\sigma(1/2)=1/2$', 'fixe', 's')
rows = [('somme', r'$3+1/2=3{,}5$', r'$\sigma(3{,}5)=3{,}5$'),
        ('produit', r'$3\times1/2=1{,}5$', r'$\sigma(1{,}5)=1{,}5$'),
        ('inverse', r'$3^{-1}=1/3$', r'$\sigma(1/3)=1/3$')]
for i, (nom, g, d) in enumerate(rows):
    y = 38 - i * 16
    text(ax, 9, y + 6, nom, 'fixe', 's')
    box(ax, 20, y, 28, 12, 'sujet', label=g, size='s')
    arrow(ax, (48.5, y + 6), (55.5, y + 6), 'varie')
    box(ax, 56, y, 30, 12, 'resultat', label=d, size='s')
text(ax, 52, 3.5, r'$\sigma$ garde somme, produit, inverse', 'fixe', 's')
save(fig, '63-073')
