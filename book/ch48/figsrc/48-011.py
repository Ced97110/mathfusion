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

fig, ax = canvas(102)
ROLE = ['sujet', 'varie', 'resultat', 'autre']
text(ax, 14, 99, 'entiers', 'encre', 's')
text(ax, 60, 99, 'cases', 'encre', 's')
dots(ax, 14, 91, 'fixe')
ys = [84 - 10 * i for i in range(7)]
cy = {0: 66, 1: 52, 2: 38, 3: 24}
for i, y in zip(range(-1, 6), ys):
    r = ROLE[i % 4]
    ibox(ax, 14, y, str(i).replace('-', '−'), r, w=12, h=7)
    arrow(ax, (20, y), (53, cy[i % 4]), r, lw=0.8)
dots(ax, 14, 14, 'fixe')
for k in range(4):
    ibox(ax, 60, cy[k], str(k), ROLE[k], w=14, h=10)
text(ax, 69, 66, 'noyau 4ℤ', 'sujet', 's', ha='left')
save(fig, '48-011')
