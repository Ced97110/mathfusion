import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(78)
g = 14
line(ax, [(4, g), (82, g)], 'fixe', lw=1.0)
A, B = 14, 40
ang = math.radians(18)
for x in (A, B):
    L = 62 if x == A else 62 - (B - A) / math.cos(ang)
    disc(ax, x, g, 1.1, 'sujet')
    line(ax, [(x, g), (x + L * math.cos(ang), g + L * math.sin(ang))], 'sujet', lw=1.2)
    arc(ax, x, g, 11, 0, 18, 'varie')
    text(ax, x + 15.5, g + 2.2, '18°', 'varie', 's')
text(ax, A, g - 4, 'A', 'sujet', 'm')
text(ax, B, g - 4, 'B', 'sujet', 'm')
text(ax, 66, g + 28, 'visées parallèles', 'sujet', 'm')
text(ax, 66, g + 24, 'elles ne se coupent pas', 'sujet', 's')
box(ax, 4, 52, 38, 11, 'limite', label=r'$\sin(18°-18°)=\sin 0°=0$', size='s')
box(ax, 46, 52, 38, 11, 'limite', label=r'division par $0$ : impossible', size='s')
arrow(ax, (42, 57.5), (46, 57.5), 'limite')
text(ax, 44, 70, r'$\beta=\alpha$ : pas de sommet à calculer', 'encre', 'm')
save(fig, '38-073')
