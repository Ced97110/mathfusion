import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(1, 8.0, '1', '6,28', '3,14'), (0.5, 4.0, '0,5', '3,14', '0,785'),
        (0.1, 0.8, '0,1', '0,628', '0,0314'), (0, 0.5, '0', '0', '0')]
cy = 46
for i, (r, rad, rl, c, a) in enumerate(cols):
    cx = 12 + i * 21.3
    role = 'resultat' if r == 0 else 'sujet'
    disc(ax, cx, cy, rad, role, fill=True)
    text(ax, cx, 30, f'r = {rl}', 'varie', 's')
    text(ax, cx, 21, f'C = {c}', role, 's')
    text(ax, cx, 12, f'A = {a}', role, 's')
text(ax, 44, 59, 'le rayon diminue', 'varie', 's')
arrow(ax, (10, 56), (78, 56), 'varie')
text(ax, 44, 4, 'au bout : un point', 'resultat', 's')
save(fig, '11-153')
