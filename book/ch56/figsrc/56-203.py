import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'distance du centre au coin', 'fixe', 's')
x0, u = 22, 45
rows = [(42, r'$\mathbb{Z}[i]$', np_ := math.sqrt(2) / 2, 'resultat', r'$\frac{\sqrt{2}}{2}\approx0{,}71$'),
        (28, r'$\mathbb{Z}[\sqrt{3}\,i]$', 1.0, 'varie', r'$1$'),
        (14, r'$\mathbb{Z}[\sqrt{-5}]$', math.sqrt(1.5), 'limite', r'$\sqrt{\frac{1}{4}+\frac{5}{4}}\approx1{,}22$')]
for y, name, d, role, lab in rows:
    text(ax, 2, y + 4, name, 'encre', 's', ha='left')
    box(ax, x0, y, d * u, 8, role, label=lab, size='s')
line(ax, [(x0 + u, 8), (x0 + u, 54)], 'encre', lw=1.0, dash=True)
text(ax, x0 + u, 57, 'frontière : 1', 'encre', 's', ha='left')
save(fig, '56-203')
