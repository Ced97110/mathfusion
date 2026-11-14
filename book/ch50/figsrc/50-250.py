import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 20, 36, 11
P = [(cx + R * math.cos(math.radians(90 - 72 * k)), cy + R * math.sin(math.radians(90 - 72 * k))) for k in range(5)]
line(ax, P + [P[0]], 'sujet', lw=1.0)
for p in P: disc(ax, p[0], p[1], 2.0, 'sujet')
text(ax, 20, 58, r'$\mathbb{Z}/5\mathbb{Z}$', 'sujet', 'm', weight='bold')
text(ax, 20, 15, '5 éléments : 5-groupe', 'sujet', 's')
text(ax, 64, 61, r'$p$-Sylow : matrices', 'sujet', 'm', weight='bold')
for r in range(3):
    for c in range(3):
        x, y = 50 + 10 * c, 44 - 10 * r
        if c > r: box(ax, x, y, 9, 9, 'sujet')
        elif c == r: box(ax, x, y, 9, 9, 'fixe', label='1')
        else: box(ax, x, y, 9, 9, 'fixe', label='0')
text(ax, 64, 18, '1 sur la diagonale, 0 dessous', 'fixe', 's')
text(ax, 64, 12, 'nombres libres au-dessus', 'sujet', 's')
save(fig, '50-250')
