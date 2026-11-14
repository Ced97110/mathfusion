import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 2.6; X = 5 * u; oy = 24
for ox, b, ctr in [(8, 3, 6), (50, 5, 10)]:
    B = b * u
    box(ax, ox, oy, X, X, 'sujet', True, label=r'$x^2$', size='s', r=0.3)
    box(ax, ox + X, oy, B, X, 'fixe', True, r=0.3)
    box(ax, ox, oy + X, X, B, 'fixe', True, r=0.3)
    box(ax, ox + X, oy + X, B, B, 'varie', True, label=str(b * b), size='s', r=0.3)
    text(ax, ox + X + B + 2.8, oy + X + B / 2, str(b), 'varie', 's')
    text(ax, ox + (X + B) / 2, 16, f'moitié de {ctr} = {b}', 'encre', 's')
    text(ax, ox + (X + B) / 2, 9, f'{b} × {b} = {b * b}', 'varie', 's')
save(fig, '23-013')
