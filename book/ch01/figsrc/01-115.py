import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
# légende
ax.add_patch(Rectangle((4, 88.5), 3, 3, ec=COL['sujet'], fc=COL['sujet'], lw=0.5, zorder=2))
text(ax, 9, 90, r'somme 1 + 2 + ⋯ + $n$', 'sujet', 's', ha='left')
ax.add_patch(Rectangle((4, 81.5), 3, 3, ec=COL['autre'], fc=COL['autre'], lw=0.5, zorder=2))
text(ax, 9, 83, r'formule $n(n + 1)/2$', 'autre', 's', ha='left')
text(ax, 70, 90, r'4 × 5 / 2 = 10', 'autre', 's')
text(ax, 70, 83, r'5 × 6 / 2 = 15', 'autre', 's')
# barres
base = 20
line(ax, [(8, base), (84, base)], 'fixe')
xs = [14 + 13 * i for i in range(5)]
hs = [3 * (n * (n + 1) // 2) for n in range(1, 6)]
for c, h in zip(xs, hs):
    ax.add_patch(Rectangle((c - 3.2, base), 3, h, ec=COL['sujet'], fc=COL['sujet'], lw=0.4, zorder=2))
    ax.add_patch(Rectangle((c + 0.2, base), 3, h, ec=COL['autre'], fc=COL['autre'], lw=0.4, zorder=2))
text(ax, 5.5, 16, r'$n$ =', 'fixe', 'm')
for n, c in enumerate(xs, 1): text(ax, c, 16, str(n), 'fixe', 'm')
text(ax, 78, 16, '…', 'fixe', 'm')
for n, txt, ty in [(4, '10', 53), (5, '15', 68)]:
    c = xs[n - 1]; yt = base + hs[n - 1]
    line(ax, [(c - 3.2, yt), (c + 3.2, yt)], 'resultat', lw=0.6)
    text(ax, c, ty, txt, 'resultat', 's')
text(ax, 44, 6, r'une phrase par entier $n$', 'encre', 'm')
save(fig, '01-115')
