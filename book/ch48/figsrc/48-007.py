import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ibox(ax, cx, cy, s, role, w=10, h=7, size='m', dash=False):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=s, size=size, dash=dash)

def dots(ax, cx, cy, role='fixe'):
    for d in (-2, 0, 2):
        disc(ax, cx + d, cy, 0.5, role)

def dial(ax, cx, cy, r, active, role):
    disc(ax, cx, cy, r, 'fixe')
    for k in range(4):
        a = math.radians(90 - 90 * k)
        disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 3.0, role if k == active else 'fixe', label=str(k), size='s')
    a = math.radians(90 - 90 * active)
    arrow(ax, (cx, cy), (cx + (r - 3.4) * math.cos(a), cy + (r - 3.4) * math.sin(a)), 'varie', lw=1.2)

BAR = lambda n: r'$\bar{%s}$' % n

fig, ax = canvas(88)
xs = [8 + 19 * i + 7 for i in range(4)]
text(ax, 44, 84, '0, 1, 2, 3 : une case chacun', 'resultat', 's')
for i, cx in enumerate(xs):
    ibox(ax, cx, 72, str(i), 'varie', w=14, h=8)
    ibox(ax, cx, 49, f'case {i}', 'sujet', w=14, h=10, size='s')
    arrow(ax, (cx, 68), (cx, 54.5), 'resultat')
    ibox(ax, cx, 22, str(i + 4), 'varie', w=14, h=8)
    arrow(ax, (cx, 26.5), (cx, 43.5), 'limite')
dots(ax, 85, 22)
text(ax, 44, 8, 'à partir de 4 : case prise', 'limite', 's')
save(fig, '48-007')
