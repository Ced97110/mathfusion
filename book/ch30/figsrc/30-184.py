import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 6, 78, 30, 0, 20, step=5, every=2, arrow_right=False)
A = [2 * math.pi * m for m in (1, 2, 3)]; B = [math.pi * math.sqrt(2) * n for n in (1, 2, 3, 4)]
for v in A:
    line(ax, [(f(v), 30), (f(v), 41)], 'fixe', dash=True, lw=0.5); disc(ax, f(v), 41, 1.4, 'sujet')
    text(ax, f(v), 46, f'{v:.3f}'.replace('.', ','), 'sujet', 's')
for v in B:
    line(ax, [(f(v), 30), (f(v), 19)], 'fixe', dash=True, lw=0.5); disc(ax, f(v), 19, 1.4, 'autre')
    text(ax, f(v), 13, f'{v:.3f}'.replace('.', ','), 'autre', 's')
text(ax, 2, 54, r'multiples de $2\pi$', 'sujet', 's', ha='left')
text(ax, 2, 6, r'multiples de $\pi\sqrt{2}$', 'autre', 's', ha='left')
text(ax, 86, 6, 'aucun point commun', 'encre', 's', ha='right')
save(fig, '30-184')
