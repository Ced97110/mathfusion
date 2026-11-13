import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\mathbb{Z}/6\mathbb{Z}$ ↔ $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$', 'sujet', 'l')
x0, y0, cw, ch = 32, 24, 14, 11
for n in range(6):
    c, r = n % 3, n % 2
    role = 'resultat' if n == 5 else 'sujet'
    box(ax, x0 + c * cw, y0 + (1 - r) * ch, cw, ch, role, label=str(n))
for c in range(3): text(ax, x0 + c * cw + cw / 2, y0 - 3, str(c), 'fixe', 's')
for r in range(2): text(ax, x0 - 3, y0 + (1 - r) * ch + ch / 2, str(r), 'fixe', 's')
text(ax, x0 + 1.5 * cw, y0 - 9, 'reste par 3', 'autre', 's')
text(ax, 13, y0 + ch, 'reste par 2', 'varie', 's')
save(fig, '52-179')
