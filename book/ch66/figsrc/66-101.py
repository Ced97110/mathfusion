import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 26, 32, 15
P = lambda k, r: (cx + r * math.cos(math.radians(90 - 40 * k)), cy + r * math.sin(math.radians(90 - 40 * k)))
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx, cy), P(9, R)], 'varie', lw=1.2)
line(ax, [(cx, cy), P(3, R)], 'varie', lw=1.2)
line(ax, [(cx, cy), P(1, R)], 'varie', lw=0.8, dash=True)
line(ax, [(cx, cy), P(2, R)], 'varie', lw=0.8, dash=True)
line(ax, [(cx + 8 * math.cos(math.radians(t)), cy + 8 * math.sin(math.radians(t))) for t in range(-30, 91, 5)], 'varie')
for k in range(1, 10):
    r = 'sujet' if math.gcd(k, 9) == 1 else 'fixe'
    x, y = P(k, R)
    disc(ax, x, y, 1.3, r)
    lx, ly = P(k, R + 4.5)
    text(ax, lx, ly, str(k), r, 'm')
box(ax, 50, 46, 8, 9, 'fixe', label='9', size='m')
line(ax, [(59.5, 49), (62.5, 49)], 'encre'); line(ax, [(59.5, 52), (62.5, 52)], 'encre')
box(ax, 64, 46, 8, 9, 'limite', label='3', size='m')
line(ax, [(73.2, 48), (75.8, 53)], 'encre'); line(ax, [(73.2, 53), (75.8, 48)], 'encre')
box(ax, 77, 46, 8, 9, 'limite', label='3', size='m')
text(ax, 68, 38, r'$\varphi(9)=6$ : pas puissance de 2', 'limite', 's')
text(ax, 68, 24, 'revient à partager\n120° en trois pas égaux', 'varie', 's')
save(fig, '66-101')
