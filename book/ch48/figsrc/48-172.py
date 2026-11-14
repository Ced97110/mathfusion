import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, R = 44, 44, 31
P = lambda h, r=R: (cx + r * math.sin(math.pi * h / 6), cy + r * math.cos(math.pi * h / 6))
mult = [0, 3, 6, 9]
for k in range(4):
    a, b = P(mult[k]), P(mult[(k + 1) % 4])
    dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy); u = (dx / L, dy / L)
    arrow(ax, (a[0] + u[0] * 3.8, a[1] + u[1] * 3.8), (b[0] - u[0] * 3.8, b[1] - u[1] * 3.8), 'varie')
for h in range(12):
    x, y = P(h)
    disc(ax, x, y, 3.3, 'sujet' if h in mult else 'fixe', fill=True, label=str(h), size='s')
text(ax, 44, 52, r'$+3$ à chaque pas', 'varie', 's')
text(ax, 44, 40, '4 multiples de 3', 'sujet', 's')
save(fig, '48-172')
