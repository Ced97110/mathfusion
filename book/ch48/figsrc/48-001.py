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

fig, ax = canvas(70)
dial(ax, 24, 35, 15, 1, 'resultat')
text(ax, 24, 8, 'bouton à 4 positions', 'sujet', 's')
text(ax, 69, 64, 'quarts de tour', 'varie', 's')
ys = [54, 44, 34, 24]
for s, y in zip(['1', '5', '9', '13'], ys):
    ibox(ax, 69, y, s, 'varie', w=14)
    arrow(ax, (62, y), (43, 35 + (y - 39) * 0.15), 'resultat', lw=0.8)
text(ax, 69, 12, 'même position : 1', 'resultat', 's')
save(fig, '48-001')
