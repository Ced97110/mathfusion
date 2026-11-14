import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, x0 = 13, 20
A = [2, -1, 0, 3, 0]; B = [1, 1, 0, 0, 4]
S = [a + b for a, b in zip(A, B)]
assert S == [3, 0, 0, 3, 4]
f = lambda v: str(v).replace('-', '−')
text(ax, 6, 56, 'rang', 'fixe', 's')
for r in range(5):
    text(ax, x0 + (r + 0.5) * cw, 56, str(r), 'fixe', 's')
for vals, role, y, lab in [(A, 'sujet', 42, r'$A$'), (B, 'autre', 30, r'$B$'), (S, 'resultat', 8, r'$A+B$')]:
    text(ax, 10, y + 4, lab, role, 'm')
    for r, v in enumerate(vals):
        box(ax, x0 + r * cw + 0.5, y, cw - 1, 8, role, label=f(v), size='m')
text(ax, 4, 36, '+', 'encre', 'l')
line(ax, [(x0, 27), (x0 + 5 * cw, 27)], 'encre', lw=0.8)
for r in range(5):
    arrow(ax, (x0 + (r + 0.5) * cw, 26), (x0 + (r + 0.5) * cw, 17.5), 'varie')
text(ax, 44, 2.5, 'chaque position seule', 'varie', 's')
save(fig, '54-090')
