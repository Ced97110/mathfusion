import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x = 5.0
cells = [('s', 8)] * 4 + [('p', 15)] * 2
gap = 3.4
centers = []
for kind, w in cells:
    box(ax, x, 30, w, 16, 'resultat' if kind == 's' else 'varie', r=0.6)
    if kind == 's':
        disc(ax, x + w / 2, 36, 2.2, 'resultat')
    else:
        disc(ax, x + 3.6, 36, 2.2, 'varie'); disc(ax, x + w - 3.6, 36, 2.2, 'varie')
        arrow(ax, (x + 6.2, 36), (x + w - 6.2, 36), 'varie', both=True, lw=0.8)
    text(ax, x + w / 2, 49.5, r'$\times2$', 'encre', 's')
    centers.append((x, x + w)); x += w + gap
brace(ax, centers[0][0], centers[3][1], 28, 'resultat', '4 entrées seules')
brace(ax, centers[4][0], centers[5][1], 28, 'varie', '2 paires')
text(ax, 44, 58, 'échange de $a$ et $b$ : 6 cycles', 'encre', 'm')
text(ax, 44, 10, r'$2^{6}=64$ ; 3 échanges : $3\times64$', 'encre', 'm')
save(fig, '49-268')
