import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, R = 30, 34, 20
ang = lambda h: math.radians(90 - 30 * h)
P = lambda h, r=R: (cx + r * math.cos(ang(h)), cy + r * math.sin(ang(h)))
for h in range(12):
    x, y = P(h)
    disc(ax, x, y, 3.6, 'varie' if h == 9 else 'resultat' if h == 2 else 'sujet', label=str(h), size='s')
n = 24
pts = [(cx + 26 * math.cos(ang(9.35 + 4.3 * i / n)), cy + 26 * math.sin(ang(9.35 + 4.3 * i / n))) for i in range(n + 1)]
line(ax, pts[:-1], 'varie', lw=1.2)
arrow(ax, pts[-2], pts[-1], 'varie', lw=1.2)
x, y = cx + 31 * math.cos(ang(11.5)), cy + 31 * math.sin(ang(11.5))
text(ax, x, y, '+5', 'varie', 'm', weight='bold')
text(ax, 58, 34, '9 + 5 = 14\n14 revient à 2', 'encre', 'm', ha='left')
save(fig, '60-001')
