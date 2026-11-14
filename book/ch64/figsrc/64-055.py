import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 21, 31, 15
P = lambda k: (cx + R * math.sin(math.radians(72 * k)), cy + R * math.cos(math.radians(72 * k)))
for k in range(5):
    a, b = P(k), P((k + 1) % 5)
    d = math.hypot(b[0] - a[0], b[1] - a[1]); u = ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
    arrow(ax, (a[0] + u[0] * 3.9, a[1] + u[1] * 3.9), (b[0] - u[0] * 3.9, b[1] - u[1] * 3.9), 'varie', lw=1.1)
for k in range(5):
    disc(ax, P(k)[0], P(k)[1], 3.4, 'sujet', label=str(k + 1), size='m')
text(ax, 65, 52, r'$(a_1\ a_2\ \cdots\ a_r)$', 'sujet', 'l')
text(ax, 65, 45, 'le dernier revient au premier', 'fixe', 's')
text(ax, 65, 33, r'$(1\ 2\ 3\ 4\ 5)$', 'varie', 'xl', weight='bold')
text(ax, 65, 24, r'longueur $r=5$', 'resultat', 'm')
text(ax, 65, 17, '5 flèches, 1 écriture', 'encre', 's')
save(fig, '64-055')
