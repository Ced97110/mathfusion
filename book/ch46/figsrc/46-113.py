import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
x0, dx = 14, 3.6
X = lambda v: x0 + v * dx
text(ax, 44, 56, 'multiple de 2 et de 3 : multiple de 6', 'encre', 'm')
rows = [(44, 2, 'autre', '2ℤ'), (32, 3, 'varie', '3ℤ'), (18, 6, 'sujet', '6ℤ')]
for v in (0, 6, 12, 18):
    line(ax, [(X(v), 44), (X(v), 18)], 'fixe', dash=True)
for y, s, role, lab in rows:
    line(ax, [(X(0), y), (X(18), y)], 'fixe', lw=0.5)
    for v in range(19):
        if v % s == 0: disc(ax, X(v), y, 1.5, role)
        else: disc(ax, X(v), y, 0.5, 'fixe')
    text(ax, 6, y, lab, role, 'l')
for v in (0, 6, 12, 18):
    text(ax, X(v), 11, str(v), 'fixe', 's')
brace(ax, X(0), X(18), 8, 'fixe', label=None)
text(ax, 44, 2.5, 'les colonnes liées : dans les deux', 'resultat', 's')
save(fig, '46-113')
