import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 57, r'$\prod\ (r_i - r_j)\ ,\ i<j$', 'sujet', 'l', weight='bold')
text(ax, 44, 49, 'racines 1, 2, 3 : une paire, un facteur', 'fixe', 's')
pairs = [(1, 2), (1, 3), (2, 3)]
bw, gap = 24.0, 6.0
x0 = (88 - 3 * bw - 2 * gap) / 2
prod = 1
for k, (a, b) in enumerate(pairs):
    x = x0 + k * (bw + gap)
    v = a - b
    prod *= v
    box(ax, x, 22, bw, 20, 'sujet', label='(%d − %d)' % (a, b))
    arrow(ax, (x + bw / 2, 22), (x + bw / 2, 15), 'varie', lw=0.9)
    text(ax, x + bw / 2, 11, '%d' % v if v >= 0 else '−%d' % -v, 'varie', 'l', weight='bold')
    if k < 2:
        text(ax, x + bw + gap / 2, 32, r'$\times$', 'fixe', 'l')
assert prod == -2
text(ax, 44, 3.5, 'produit : −1 × −2 × −1 = −2', 'resultat', 'm', weight='bold')
save(fig, '65-034')
