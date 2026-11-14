import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(72)
C = (24, 40); R = 18
disc(ax, C[0], C[1], R, 'fixe')
for rr in (5, 10.5, 16):
    pts = arc(C[0], C[1], rr, 0.3, 0.3 + 5.6)
    line(ax, pts, 'varie', lw=1.3); arrow(ax, pts[-4], pts[-1], 'varie', lw=1.0)
for k, rr in enumerate((2.5, 7.75, 13.25)):
    text(ax, C[0], C[1] - rr, str(k + 1), 'varie', 's', weight='bold')
line(ax, [C, (C[0] + R, C[1])], 'sujet', lw=2.0)
text(ax, 44.5, 40, r'$r = 0{,}35$ m', 'sujet', 's', ha='left')
text(ax, 24, 64, 'aiguille : 3 tours', 'varie')
text(ax, 24, 17, 'un seul disque : 0,385 m²', 'fixe', 's')
for i in range(3):
    box(ax, 58, 22 + 10 * i, 28, 8, 'varie', label=f'tour {i + 1} : 0,385 m²', size='s')
text(ax, 71, 64, 'surface balayée', 'varie')
text(ax, 72, 12, r'$3\times 0{,}385 \approx 1{,}15$ m$^2$', 'varie', 's', weight='bold')
save(fig, '29-105')
