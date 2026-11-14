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

fig, ax = canvas(66)
xs = [38, 51, 64, 77]
text(ax, 44, 61, 'un hasard ?', 'encre', 'm')
text(ax, 3, 46, 'position 0', 'sujet', 's', ha='left')
text(ax, 3, 20, 'position 1', 'autre', 's', ha='left')
for i, cx in enumerate(xs):
    ibox(ax, cx, 46, str(4 * i), 'sujet', w=10, h=7)
    ibox(ax, cx, 20, str(4 * i + 1), 'autre', w=10, h=7)
    arrow(ax, (cx, 42), (cx, 24), 'varie')
dots(ax, 85, 46, 'sujet'); dots(ax, 85, 20, 'autre')
text(ax, xs[0] + 3, 33, '+ 1', 'varie', 's', ha='left')
text(ax, 44, 6, 'toujours + 1 : un décalage', 'varie', 's')
save(fig, '48-016')
