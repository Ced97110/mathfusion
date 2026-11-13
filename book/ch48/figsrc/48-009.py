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

fig, ax = canvas(80)
f = numberline(ax, 6, 74, 62, 0, 10, labels=False, arrow_right=False)
for a, b, lab in ((1, 5, '+4'), (5, 9, '+4')):
    arrow(ax, (f(a), 66), (f(b), 66), 'sujet', curve=-0.4)
    text(ax, f((a + b) / 2), 74, lab, 'sujet', 's')
for v, tx in zip((1, 5, 9), (38, 44, 50)):
    disc(ax, f(v), 62, 2.8, 'varie', label=str(v), size='s')
    arrow(ax, (f(v), 58.5), (tx, 41), 'resultat', lw=0.8)
box(ax, 24, 29, 40, 12, 'resultat', label='position 1')
box(ax, 6, 6, 76, 14, 'sujet', label='noyau = ces écarts (4, 8…)', size='s')
save(fig, '48-009')
