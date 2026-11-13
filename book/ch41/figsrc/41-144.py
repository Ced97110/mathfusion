import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
k = 0.03
y0 = 10
items = [(22, 0, 1000.0, '1 000 J', 'fixe'), (44, 30, 50 * 20 * math.cos(math.radians(30)), '≈ 866,0 J', 'resultat'), (66, 90, 0.0, '0 J', 'fixe')]
line(ax, [(8, y0), (80, y0)], 'fixe')
for x, ang, w, lab, role in items:
    h = w * k
    if h > 0.05:
        box(ax, x - 8, y0, 16, h, role, fill=True)
    text(ax, x, y0 + h + 3.5, lab, role, 's')
    text(ax, x, y0 - 3.5, f'{ang}°', role, 's')
text(ax, 44, 52, r'$50\times20\times\cos 30°$', 'resultat', 'm')
save(fig, '41-144')
