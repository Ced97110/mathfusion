import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 27, 33, 18
pos = lambda h, r=R: (cx + r * math.sin(math.radians(30 * h)), cy + r * math.cos(math.radians(30 * h)))
members = [0, 3, 6, 9]
for h in range(12):
    x, y = pos(h)
    disc(ax, x, y, 1.6, 'sujet' if h in members else 'fixe')
for h in members:
    x, y = pos(h, R + 5)
    text(ax, x, y, str(h), 'sujet', 'm')
for a, b in zip(members, members[1:] + [0]):
    arrow(ax, pos(a, R - 2.5), pos(b, R - 2.5), 'varie', curve=-0.25)
text(ax, 70, 50, r'$g=3$', 'sujet', 'l')
text(ax, 70, 38, r'$|g|=4$', 'varie', 'l')
text(ax, 70, 28, '4 × 3 = 12 = 0', 'varie', 's')
text(ax, 70, 16, r'$\langle g\rangle=\{0,3,6,9\}$', 'sujet', 'm')
save(fig, '60-111')
