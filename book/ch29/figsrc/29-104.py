import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(60)
gy = 32
line(ax, [(5, gy), (84, gy)], 'fixe')
xs = [10 + 22 * k for k in range(4)]
for x in xs:
    disc(ax, x, gy + 3.5, 3.5, 'sujet'); disc(ax, x, gy, 0.9, 'varie')
text(ax, 10, 43, r'$r = 0{,}35$ m', 'sujet', 's')
text(ax, 25, 40, 'valve', 'varie', 's'); arrow(ax, (21.5, 39), (11, 32.8), 'varie', lw=0.7)
for k in range(3):
    brace(ax, xs[k] + 0.5, xs[k + 1] - 0.5, 29, 'fixe', label='2,20 m')
brace(ax, xs[0], xs[3], 20, 'resultat', label='3 tours : 6,60 m')
text(ax, 44, 7, r'$s = 0{,}35 \times 6\pi \approx 6{,}60$ m', 'resultat')
save(fig, '29-104')
