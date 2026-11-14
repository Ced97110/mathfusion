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

fig, ax = canvas(84)
box(ax, 29, 70, 30, 10, 'fixe', label='7 et 6')
box(ax, 2, 46, 40, 10, 'varie', label='d’abord : 7 + 6 = 13', size='s')
box(ax, 2, 28, 40, 10, 'varie', label=r'puis : $f(13)=\bar{1}$', size='s')
box(ax, 46, 46, 40, 10, 'autre', label=r'$f(7)=\bar{3}$ ; $f(6)=\bar{2}$', size='s')
box(ax, 46, 28, 40, 10, 'autre', label='3 + 2 = 5 → position 1', size='s')
box(ax, 22, 6, 44, 10, 'resultat', label='même position', weight='bold')
arrow(ax, (38, 70), (24, 56.8), 'varie'); arrow(ax, (50, 70), (64, 56.8), 'autre')
arrow(ax, (22, 46), (22, 38.8), 'varie'); arrow(ax, (66, 46), (66, 38.8), 'autre')
arrow(ax, (26, 28), (34, 16.8), 'varie'); arrow(ax, (62, 28), (54, 16.8), 'autre')
save(fig, '48-005')
