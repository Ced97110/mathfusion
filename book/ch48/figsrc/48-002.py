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

fig, ax = canvas(55)
cs = [13, 44, 75]
for cx, a, role in zip(cs, [0, 3, 1], ['sujet', 'varie', 'resultat']):
    dial(ax, cx, 34, 7, a, role)
for cx, lab in zip(cs, ['départ', 'position 3', 'position 1']):
    text(ax, cx, 17, lab, 'encre', 's')
for i, lab in enumerate(['+ 7 quarts', '+ 6 quarts']):
    x0, x1 = cs[i] + 11, cs[i + 1] - 11
    arrow(ax, (x0, 34), (x1, 34), 'varie')
    text(ax, (x0 + x1) / 2, 42, lab, 'varie', 's')
text(ax, 44, 6, '7 + 6 = 13 quarts de tour', 'encre', 's')
save(fig, '48-002')
