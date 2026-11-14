import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
d = 4.2; y0 = 22
x = 15; centers = []
for n in (2, 4, 8):
    xs = x
    for p in range(n // 2):
        for k in range(2): box(ax, x + k * d, y0, d, d, 'autre', r=0.3, lw=0.6)
        x += 2 * d + (1.2 if p < n // 2 - 1 else 0)
    text(ax, (xs + x) / 2, y0 - 3.5, str(n), 'autre', 's'); x += 3.5
brace(ax, 15, x - 3.5, y0 + 6, 'fixe', label=r"orbites de $P''$ sur $\Sigma$", down=False)
box(ax, 4, y0, d, d, 'limite', fill=False, dash=True, r=0.3, lw=0.8)
line(ax, [(4, y0), (4 + d, y0 + d)], 'limite'); line(ax, [(4, y0 + d), (4 + d, y0)], 'limite')
text(ax, 6.1, y0 - 3.5, 'taille 1', 'limite', 's'); text(ax, 6.1, y0 - 8, 'absente', 'limite', 's')
text(ax, 44, 8, r'somme paire : $|\Sigma|\equiv 0$', 'resultat', 's')
save(fig, '50-108')
