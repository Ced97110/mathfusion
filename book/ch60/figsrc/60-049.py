import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 70, 24, -4, 4, step=1)
for v in range(-4, 5):
    disc(ax, f(v), 24, 1.6, 'resultat' if v == 1 else 'fixe')
for v in (0, -3, 1):
    line(ax, [(f(v), 26), (f(v), 40 if v != 0 else 32)], 'fixe', lw=0.5, dash=True)
arrow(ax, (f(0), 32), (f(-3), 32), 'varie')
text(ax, f(-3) + 1.5, 36, r'$a h$ = (−1) × 3 = −3', 'varie', 's', ha='left')
arrow(ax, (f(-3), 40), (f(1), 40), 'autre')
text(ax, f(-3) + 1.5, 44, r'$b g$ = 1 × 4 = 4', 'autre', 's', ha='left')
text(ax, f(1) + 3, 32, '−3 + 4 = 1', 'resultat', 's', ha='left')
text(ax, 44, 56, r'$g$ = 4, $h$ = 3, $a$ = −1, $b$ = 1', 'encre', 'm')
text(ax, 44, 13, r'$y$ = $h x$ et $z$ = $g x$', 'fixe', 's')
text(ax, 44, 5, r'donc $x$ = $a y$ + $b z$', 'resultat', 'm')
save(fig, '60-049')
