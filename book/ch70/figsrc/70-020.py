import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 18, 70, 38, -2, 2, step=1, role='fixe', arrow_right=False)
text(ax, f(2) + 6, 38, r'$y$', 'fixe', 's')
# roots of f : -1 and 1 (blue) ; root of g : 1 (violet) ; common root : 1 (green)
text(ax, 44, 52, r'$f=y^2-1$ : racines $-1$ et $1$', 'sujet', 's')
for v in (-1, 1):
    disc(ax, f(v), 44, 1.3, 'sujet')
text(ax, 44, 21, r'$g=y-1$ : racine $1$', 'autre', 's')
disc(ax, f(1), 28, 1.3, 'autre')
line(ax, [(f(1), 28), (f(1), 44)], 'resultat', lw=0.8, dash=True)
box(ax, 22, 4, 44, 9, 'resultat', label='racine commune : 1', size='s')
save(fig, '70-020')
