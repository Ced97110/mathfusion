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

fig, ax = canvas(62)
for cy, vals, role, lab, ly in ((44, ['1', '5', '9', '13'], 'varie', 'position 1', 57), (14, ['3', '7', '11'], 'autre', 'position 3', 27)):
    n = len(vals)
    for i, v in enumerate(vals):
        ibox(ax, 11 + 11 * i, cy, v, role, w=9, h=8)
    xd = 11 + 11 * n + 1
    dots(ax, xd, cy, role)
    box(ax, 3, cy - 8, xd + 4 - 3, 16, role, fill=False, dash=True)
    text(ax, 4, ly, 'fibre de la ' + lab.replace('position', 'case'), role, 's', ha='left')
    arrow(ax, (xd + 5, cy), (68, cy), role)
    ibox(ax, 76.5, cy, lab, role, w=17, h=10, size='s')
save(fig, '48-012')
