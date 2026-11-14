import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 24, 33, 18
pos = lambda h, r=R: (cx + r * math.sin(math.radians(30 * h)), cy + r * math.cos(math.radians(30 * h)))
for h in range(12):
    x, y = pos(h)
    role = 'varie' if h == 2 else ('resultat' if h in (4, 8, 0) else 'fixe')
    disc(ax, x, y, 1.7, role)
for h, lab, role in [(2, '2', 'varie'), (4, '4', 'resultat'), (8, '8', 'resultat'), (0, '0', 'resultat')]:
    x, y = pos(h, R + 5)
    text(ax, x, y, lab, role, 'm')
arrow(ax, pos(2, R - 3), pos(4, R - 3), 'varie', curve=-0.3)
for a, b in [(4, 8), (8, 0)]:
    arrow(ax, pos(a, R - 3), pos(b, R - 3), 'resultat', curve=-0.2)
text(ax, 66, 52, r'$a=2$ , $r=2$', 'varie', 'm')
text(ax, 66, 40, r'$ra=2\times2=4$', 'resultat', 'm')
text(ax, 66, 28, '4, 8, 12 = 0', 'resultat', 's')
text(ax, 66, 18, '3 pas : ordre 3', 'resultat', 'm')
save(fig, '60-118')
