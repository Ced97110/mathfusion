import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 17, 62, r'$\mathbb{Z}$ : $n$', 'sujet', 'm')
text(ax, 55, 62, r'$\mathbb{Z}/7$ : $n1$', 'resultat', 'm')
pairs = [(0, 0), (7, 0), (14, 0), (5, 5), (10, 3), (15, 1)]
yr = {0: 43.5, 5: 26.5, 3: 18, 1: 9.5}
for i, (n, im) in enumerate(pairs):
    y = 52 - 8.5 * i
    box(ax, 10, y, 14, 7, 'varie' if im == 0 else 'sujet', label=str(n))
    arrow(ax, (24.5, y + 3.5), (47.5, yr[im] + 3.5), 'fixe')
for im, y in yr.items():
    box(ax, 48, y, 14, 7, 'resultat', label=str(im))
text(ax, 75, 47, 'noyau :', 'varie', 's', weight='bold')
text(ax, 75, 43, 'multiples de 7', 'varie', 's')
save(fig, '51-139')
