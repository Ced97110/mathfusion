import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# coefficient table in the monomials x^3, x^2 y, x y^2, y^3
cols = [r'$x^3$', r'$x^2y$', r'$xy^2$', r'$y^3$']
row1 = [1, 0, 0, 1]          # x^3 + y^3
row2 = [1, 3, 3, 1]          # (x+y)^3 = e1^3
row3 = [a - b for a, b in zip(row1, row2)]   # f1
assert row3 == [0, -3, -3, 0]
neg = lambda n: str(n).replace('-', '−')
X0, ST, CW = 29, 15, 13
for j, c in enumerate(cols):
    text(ax, X0 + j * ST + CW / 2, 64, c, 'fixe', 'm')
rows = [(r'$x^3+y^3$', 'sujet', row1, 48), (r'$e_1^3$', 'varie', row2, 33), (r'$f_1$', 'resultat', row3, 14)]
for lab, role, vals, yy in rows:
    text(ax, 3, yy + 4, lab, role, 'm', ha='left')
    for j, v in enumerate(vals):
        box(ax, X0 + j * ST, yy, CW, 9, role if v else 'fixe', label=neg(v), size='m')
text(ax, 24.5, 45.5, '−', 'varie', 'xl', weight='bold')
line(ax, [(3, 28.5), (86, 28.5)], 'fixe', lw=0.6)
# x^3 and y^3 cancel: mark with arrows from rows to rows
text(ax, 44, 7, r'nouveau plus haut monôme : $x^2y$', 'resultat', 's')
arrow(ax, (X0 + ST + CW / 2, 10), (X0 + ST + CW / 2, 13.5), 'resultat')
save(fig, '55-125')
