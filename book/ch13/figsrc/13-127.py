import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 74, 30, -3, 3, 1, every=3)
for v, r in [(-3, 'limite'), (3, 'limite'), (0, 'resultat')]:
    disc(ax, f(v), 30, 1.8, r)
    text(ax, f(v), 40, f'|{v}| = {abs(v)}'.replace('-', '−'), r, 's')
brace(ax, f(0), f(3), 22, 'limite', label='3'); brace(ax, f(-3), f(0), 22, 'limite', label='3')
text(ax, 44, 52, 'distance 0 : seulement a = 0', 'resultat', 's')
save(fig, '13-127')
