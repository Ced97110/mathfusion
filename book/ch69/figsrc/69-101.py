import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 10, 70, 12, -2, 2, 1)
Y = lambda n: 16 + 9 * n
roots_f = [-1.88, 0.35, 1.53]
roots_g = [-1, 0.5, 1]
for r in roots_g:
    line(ax, [(f(r), 13.5), (f(r), 46)], 'fixe', dash=True, lw=0.7)
for r in roots_f:
    line(ax, [(f(r), 13.5), (f(r), 46)], 'sujet', dash=True, lw=0.9)
pts = [(10, Y(3))]
for k, r in enumerate(roots_f):
    pts += [(f(r), Y(3 - k)), (f(r), Y(2 - k))]
pts.append((f(2), Y(0)))
line(ax, pts, 'varie', lw=1.5)
for k, r in enumerate(roots_f):
    disc(ax, f(r), Y(2.5 - k), 1.3, 'sujet')
for r in roots_g:
    v = 3 - sum(1 for q in roots_f if q < r)
    disc(ax, f(r), Y(v), 1.3, 'fixe')
for n in range(4):
    text(ax, 5, Y(n), str(n), 'varie', 'm')
text(ax, 5, 50, r'$V$', 'varie', 'm')
text(ax, 14, 56, 'bleu : racine de $f$ : marche', 'sujet', 's', ha='left')
text(ax, 14, 52, r'gris : $f_1$ ou $f_2$ : plat', 'fixe', 's', ha='left')
save(fig, '69-101')
