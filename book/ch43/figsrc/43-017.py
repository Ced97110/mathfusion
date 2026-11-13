import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 21, 32, 14
P = lambda n, r=R: (cx + r*math.sin(math.radians(30*n)), cy + r*math.cos(math.radians(30*n)))
for n in range(12):
    x, y = P(n); disc(ax, x, y, 1.5, 'sujet' if n == 3 else 'fixe')
for n, lab in ((0, '0'), (3, '3'), (11, '11')):
    x, y = P(n, R+5); text(ax, x, y, lab, 'sujet' if n == 3 else 'encre', 's')
arrow(ax, P(11, R-5.5), P(0, R-5.5), 'varie', curve=-0.4)
text(ax, cx, cy, 'après 11 : 0', 'varie', 's')
text(ax, 66, 54, r'$3+12k$', 'sujet', 'l')
xs = {-9: 50, 3: 62, 15: 74, 27: 86}
f = lambda v: 50 + (v + 9) / 12 * 12
line(ax, [(46, 32), (87, 32)], 'fixe')
for v in (-9, 3, 15, 27):
    disc(ax, f(v), 32, 1.5, 'sujet'); text(ax, f(v), 26.5, str(v).replace('-', '−'), 'sujet', 's')
for v in (-9, 3, 15):
    arrow(ax, (f(v)+1.5, 34), (f(v+12)-1.5, 34), 'varie', curve=-0.6)
    text(ax, f(v)+6, 41, '+12', 'varie', 's')
save(fig, '43-017')
