import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
cx, cy, R = 62, 31, 17
pos = lambda k: (cx + R * math.sin(2 * math.pi * k / 5), cy + R * math.cos(2 * math.pi * k / 5))
for k in range(5):
    disc(ax, *pos(k), 4.2, 'resultat' if k in (2, 3) else 'sujet', label=str(k), size='m')
for k in (3, 4, 0, 1):
    a, b = pos(k), pos((k + 1) % 5)
    d = math.hypot(b[0] - a[0], b[1] - a[1]); t = 4.6 / d
    arrow(ax, (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t), (b[0] - (b[0] - a[0]) * t, b[1] - (b[1] - a[1]) * t), 'varie', lw=1.1)
text(ax, 62, cy, '+ 4 pas', 'varie', 's')
text(ax, 3, 55, r'$\mathbb{F}_p=\mathbb{Z}/p\mathbb{Z}$', 'sujet', 'xl', ha='left')
text(ax, 3, 46, r'avec $p=5$ premier', 'encre', 's', ha='left')
text(ax, 3, 38, 'restes de la division', 'sujet', 's', ha='left')
text(ax, 3, 33.5, 'par 5 : 0, 1, 2, 3, 4', 'sujet', 's', ha='left')
text(ax, 3, 22, r'$3+4=7$, reste $2$', 'varie', 's', ha='left')
text(ax, 3, 14, r'$2\times3=6$, reste $1$', 'resultat', 's', ha='left')
text(ax, 3, 9.5, '3 est l’inverse de 2', 'resultat', 's', ha='left')
save(fig, '73-023')
