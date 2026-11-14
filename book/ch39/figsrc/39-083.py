import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
c = (56, 36); s = 12.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=60): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
line(ax, arc(2, 0, 360), 'fixe', dash=True)
arrow(ax, (c[0] - 31, c[1]), (c[0] + 31, c[1]), 'fixe', lw=0.6)
arrow(ax, (c[0], c[1] - 31), (c[0], c[1] + 31), 'fixe', lw=0.6)
for d in (0, 120, 240):
    disc(ax, *P(2, d), 1.8, 'sujet')
text(ax, P(2, 0)[0] + 2.5, P(2, 0)[1] + 3.5, '2', 'sujet', 's')
text(ax, P(2, 120)[0] - 3, P(2, 120)[1] + 3, 'w', 'sujet', 's')
text(ax, P(2, 240)[0] - 3, P(2, 240)[1] - 3, 'w', 'sujet', 's')
box(ax, 3, 46, 26, 11, 'fixe', label='donné : 8', size='s')
arrow(ax, (16, 46), (16, 38), 'varie')
box(ax, 3, 26, 26, 11, 'sujet', label='$w^{3}$ = 8', size='m')
text(ax, 16, 18, '3 nombres w', 'sujet', 's')
text(ax, 16, 13, 'dont le cube vaut 8', 'sujet', 's')
save(fig, '39-083')
