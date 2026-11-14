import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, cells, c=6.0):
    """n x n cases de coin bas-gauche (x, y) ; cells : {(ligne, colonne): (texte ou None, role)}."""
    for i in range(n):
        for j in range(n):
            lab, r = cells.get((i, j), (None, 'fixe'))
            box(ax, x + j * c, y + (n - 1 - i) * c, c, c, r, label=lab, size='s', r=0.3, lw=0.6)

def eq(ax, x, y, w=3.6):
    line(ax, [(x - w / 2, y + 0.9), (x + w / 2, y + 0.9)], 'encre', lw=0.9)
    line(ax, [(x - w / 2, y - 0.9), (x + w / 2, y - 0.9)], 'encre', lw=0.9)

def zero(n=2):
    return {(i, j): (None, 'limite') for i in range(n) for j in range(n)}

fig, ax = canvas(66)
text(ax, 5, 61, 'stable par :', 'fixe', 's', ha='left')
cx = [48, 64, 80]
for x, s in zip(cx, ['somme', 'multiples', 'produit']): text(ax, x, 61, s, 'fixe', 's')
rows = [('sous-anneau', r'ex. : entiers, ×½ sort', [1, 0, 1], 'fixe'), ('sous-espace', 'ex. : le produit sort', [1, 1, 0], 'fixe'), ('sous-algèbre', None, [1, 1, 1], 'sujet')]
for k, (lab, note, ok, role) in enumerate(rows):
    y = 50 - 16 * k
    box(ax, 2, y - 7.5, 84, 15, role, fill=True)
    text(ax, 5, y + (2.5 if note else 0), lab, 'sujet' if role == 'sujet' else 'encre', 'm', ha='left')
    if note: text(ax, 5, y - 3.5, note, 'fixe', 's', ha='left')
    for x, v in zip(cx, ok):
        r = 'resultat' if v else 'limite'
        disc(ax, x, y, 3.8, r)
        if v: line(ax, [(x - 1.8, y), (x - 0.5, y - 1.5), (x + 2, y + 1.8)], r, lw=1.2)
        else:
            line(ax, [(x - 1.5, y - 1.5), (x + 1.5, y + 1.5)], r, lw=1.2); line(ax, [(x - 1.5, y + 1.5), (x + 1.5, y - 1.5)], r, lw=1.2)
save(fig, '76-043')
