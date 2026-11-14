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
box(ax, 3, 10, 38, 56, 'fixe')
text(ax, 22, 60, 'tous les entiers', 'encre', 's')
box(ax, 6, 18, 32, 28, 'sujet')
text(ax, 22, 36, 'noyau', 'sujet', 'l', weight='bold')
text(ax, 22, 27, 'ce qui est perdu', 'sujet', 's')
box(ax, 52, 10, 33, 56, 'autre')
text(ax, 68.5, 60, 'positions atteintes', 'autre', 's')
for k in range(4):
    ibox(ax, 68.5, 49 - 10 * k, str(k), 'autre', w=14, h=7)
arrow(ax, (41, 38), (52, 38), 'varie')
text(ax, 46.5, 42, r'$f$', 'varie', 'm')
save(fig, '48-010')
