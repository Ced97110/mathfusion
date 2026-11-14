import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
f = lambda v: 44 + v * 3.3
# ligne 1 : 6ℤ
text(ax, 44, 64, 'les multiples de 6 : base (6)', 'sujet', 's', weight='bold')
line(ax, [(f(-12), 48), (f(12), 48)], 'fixe', lw=0.5)
for v in range(-12, 13):
    mult = v % 6 == 0
    disc(ax, f(v), 48, 2.0 if mult else 0.7, 'sujet' if mult else 'fixe')
for v in (-12, -6, 0, 6, 12):
    text(ax, f(v), 41.5, str(v).replace('-', '−'), 'sujet', 's')
arrow(ax, (f(0), 55), (f(6), 55), 'varie', lw=1.5)
text(ax, f(0) - 10, 55, 'base (6)', 'varie', 's')
# ligne 2 : 0ℤ
text(ax, 44, 28, 'les multiples de 0 : base vide', 'fixe', 's', weight='bold')
line(ax, [(f(-12), 14), (f(12), 14)], 'fixe', lw=0.5)
for v in range(-12, 13):
    z = v == 0
    disc(ax, f(v), 14, 2.0 if z else 0.7, 'sujet' if z else 'fixe')
text(ax, f(0), 7.5, '0', 'sujet', 's')
text(ax, f(6) + 6, 21, 'seul 0 : base ( )', 'fixe', 's')
save(fig, '58-324')
