import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [32, 48, 64]; cw = 16
for x, h in zip(cx, ['centaines', 'dizaines', 'unités']):
    text(ax, x + cw / 2, 61, h, 'fixe', 's')
    line(ax, [(x, 12), (x, 56)], 'fixe', dash=True, lw=0.5)
line(ax, [(cx[0] + cw, 12), (cx[0] + cw, 56)], 'fixe', dash=True, lw=0.5)
line(ax, [(cx[2] + cw, 12), (cx[2] + cw, 56)], 'fixe', dash=True, lw=0.5)
for digits, y, role in [('235', 44, 'sujet'), ('142', 30, 'autre'), ('377', 10, 'resultat')]:
    for x, d in zip(cx, digits):
        box(ax, x + 2, y, cw - 4, 10, role, label=d, size='l')
text(ax, 22, 35, '+', 'encre', 'xl')
line(ax, [(28, 27), (84, 27)], 'encre', lw=1.0)
save(fig, '08-004')
