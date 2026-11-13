import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 12, 72, 24, -2, 2, step=1, arrow_right=False, size='m')
for v in range(-2, 3):
    disc(ax, f(v), 24, 1.4, 'resultat')
brace(ax, f(-2), f(2), 15, 'resultat', label='cinq entiers permis', down=True)
for v, lx, ly, lb in [(0.618, 36, 40, '72° : 0,618'), (1.247, 64, 52, '≈ 51,4° : 1,247')]:
    disc(ax, f(v), 24, 1.4, 'limite')
    text(ax, lx, ly, lb, 'limite', 's')
    arrow(ax, (lx + 4, ly - 2.2), (f(v), 26.2), 'limite', lw=1.0)
text(ax, 20, 56, 'pas entiers : exclus', 'limite', 's')
save(fig, '74-128')
