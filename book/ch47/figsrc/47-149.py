import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [14 + 14 * c for c in range(5)]
for c, x in enumerate(xs):
    box(ax, x - 6, 20, 12, 28, 'sujet' if c == 0 else 'fixe', fill=True, dash=True, r=1.2)
    for r, y in enumerate([41, 27]):
        disc(ax, x, y, 3.8, 'sujet' if c == 0 else 'fixe', label=str(5 * r + c), size='m')
text(ax, 8, 56, r'$5\mathbb{Z}$ : multiples de 5', 'sujet', 'm', ha='left')
brace(ax, 8, 76, 18, 'resultat', label=r'$\mathbb{Z}/5\mathbb{Z}$ : 5 classes', size='m')
save(fig, '47-149')
