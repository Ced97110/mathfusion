import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [(5, 4, 'resultat', r'$4=2^2$ : se construit'), (7, 6, 'limite', r'6 n’est pas une puissance de 2'),
        (17, 16, 'resultat', r'$16=2^4$ : se construit')]
s, p, x0 = 2.4, 2.9, 20
for k, (n, ph, role, tag) in enumerate(rows):
    y = 42 - k * 17
    text(ax, 2, y + 1.2, rf'$n={n}$', 'encre', 'm', ha='left')
    for j in range(ph):
        box(ax, x0 + j * p, y, s, s, role, r=0.2, lw=0.6)
    text(ax, x0, y - 3.6, tag, role, 's', ha='left')
text(ax, 2, 54, r'une case = une unité de $\varphi(n)$', 'encre', 's', ha='left')
save(fig, '66-062')
