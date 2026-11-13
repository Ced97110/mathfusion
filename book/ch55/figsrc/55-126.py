import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [r'$x^2y$', r'$xy^2$']
f1 = [-3, -3]
e1e2 = [1, 1]          # e1*e2 = (x+y)*xy = x^2 y + x y^2
sub = [-3 * c for c in e1e2]
f2 = [a - b for a, b in zip(f1, sub)]
assert sub == f1 and f2 == [0, 0]
neg = lambda n: str(n).replace('-', '−')
X0, ST, CW = 34, 22, 18
for j, c in enumerate(cols):
    text(ax, X0 + j * ST + CW / 2, 59, c, 'fixe', 'm')
rows = [(r'$f_1$', 'sujet', f1, 40), (r'$-3e_1e_2$', 'varie', sub, 25), (r'$f_2=0$', 'resultat', f2, 5)]
for lab, role, vals, yy in rows:
    text(ax, 3, yy + 5, lab, role, 'm', ha='left')
    for j, v in enumerate(vals):
        box(ax, X0 + j * ST, yy, CW, 10, role, label=neg(v), size='l')
text(ax, 29, 32, '−', 'varie', 'xl', weight='bold')
line(ax, [(78, 45), (80, 45), (80, 30), (78, 30)], 'fixe', lw=1.0)
text(ax, 83.5, 37.5, 'identiques', 'fixe', 's', rot=90)
line(ax, [(3, 21.5), (76, 21.5)], 'fixe', lw=0.8)
text(ax, 83, 10, 'arrêt', 'resultat', 's')
save(fig, '55-126')
