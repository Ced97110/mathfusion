import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 105 % 26 == 1 and 105 == 4 * 26 + 1 and 1 % 26 == 1

fig, ax = canvas(92)
cx, cy, R = 44, 48, 23
ang = lambda k: math.radians(90 - k * 360 / 26)
pt = lambda k, r=R: (cx + r * math.cos(ang(k)), cy + r * math.sin(ang(k)))
for k in range(26):
    x, y = pt(k)
    disc(ax, x, y, 2.0 if k == 1 else 1.1, 'resultat' if k == 1 else 'fixe')
text(ax, *pt(0, R + 4.5), '0', 'fixe', 's')
x1, y1 = pt(1)
lx, ly = pt(1, R + 8)
text(ax, lx + 3, ly, '1', 'sujet', 'm')
arrow(ax, (lx + 1.2, ly - 1.2), (x1 + 0.8, y1 + 2.0), 'sujet', lw=0.8)
bx = cx + 36 * math.cos(math.radians(14))
by = cy + 36 * math.sin(math.radians(14))
text(ax, bx, by, '105', 'varie', 'm')
arrow(ax, (bx - 3.5, by + 1.5), (x1 + 2.0, y1 - 0.5), 'varie', lw=0.8, curve=0.25)
text(ax, cx, cy + 3, r'$105 \equiv 1\ (\mathrm{mod}\ 26)$', 'resultat', 'm')
text(ax, cx, cy - 3, 'même case', 'resultat', 's')
text(ax, cx, 14, r'$105 = 4 \times 26 + 1$ : 4 tours', 'varie', 's')
text(ax, cx, 8, 'et 1 de plus', 'varie', 's')
save(fig, '53-052')
