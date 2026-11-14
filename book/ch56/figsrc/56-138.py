import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y0 = 12.0; u = 11.0
ns = [-3, -2, -1, 1, 2, 3]
xs = {n: 14 + i * 11 for i, n in enumerate(ns)}
line(ax, [(6, y0), (82, y0)], 'fixe')
for n in ns:
    unit = abs(n) == 1
    role = 'sujet' if unit else 'fixe'
    h = abs(n) * u * 0.8
    box(ax, xs[n] - 4, y0, 8, h, role, r=0.6)
    text(ax, xs[n], y0 - 3.5, f'{n}'.replace('-', '−'), role, 's')
    text(ax, xs[n], y0 + h + 3, f'{abs(n)}', role, 's')
line(ax, [(6, y0 + 0.8 * u), (82, y0 + 0.8 * u)], 'varie', dash=True)
text(ax, 6, 60, r'$\nu(n)=|n|$ dans $\mathbb{Z}$', 'encre', 's', ha='left')
text(ax, 82, y0 + 0.8 * u + 3.5, 'taille minimale', 'varie', 's', ha='right')
text(ax, 31, 50, r'unités : $\pm1$', 'sujet', 's') if False else None
save(fig, '56-138')
