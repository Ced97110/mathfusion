import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$SL_n(F)$ : déterminant 1', 'sujet', 'l')
def shear(cx, cy, h, kind, sg):
    k = 0.7 * sg
    sq = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    line(ax, [(cx + h * a, cy + h * b) for a, b in sq] + [(cx - h, cy - h)], 'fixe', lw=0.5, dash=True)
    if kind == 'h': Q = [(cx + h * (a + k * b), cy + h * b) for a, b in sq]
    else: Q = [(cx + h * a, cy + h * (b + k * a)) for a, b in sq]
    poly(ax, Q, 'varie')
def row(y, n, bw, gap, x0, lab, tgt):
    kinds = [('h', 1), ('v', -1)] * 3
    for i in range(n):
        bx = x0 + i * (bw + gap)
        box(ax, bx, y, bw, 11, 'fixe', r=0.8)
        shear(bx + bw / 2, y + 5.5, bw * 0.2, *kinds[i])
    xe = x0 + n * (bw + gap) - gap
    brace(ax, x0, xe, y, 'varie', lab)
    arrow(ax, (xe + 2, y + 5.5), (58, y + 5.5), 'varie')
    box(ax, 59, y - 0.5, 27, 12, 'resultat', label=tgt, size='s')
row(40, 3, 12, 3, 4, '3 cisaillements', 'quart de tour')
row(14, 6, 7, 2, 4, '6 cisaillements', 'dilatation')
text(ax, 44, 55, 'produit de transvections', 'varie', 's')
text(ax, 44, 3, 'pointillé gris : le carré avant', 'fixe', 's')
save(fig, '73-049')
