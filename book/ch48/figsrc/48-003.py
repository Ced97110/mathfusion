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

fig, ax = canvas(56)
f = numberline(ax, 6, 76, 34, 0, 13, labels=False, arrow_right=False)
for v in (0, 7, 12, 13):
    text(ax, f(v), 30.4, str(v), 'encre', 's')
arrow(ax, (f(0), 38), (f(7), 38), 'varie', curve=-0.35)
text(ax, f(3.5), 47, '7', 'varie', 's')
arrow(ax, (f(7), 38), (f(13), 38), 'autre', curve=-0.35)
text(ax, f(10), 46, '6', 'autre', 's')
brace(ax, f(0), f(12), 26, 'sujet', label='3 × 4 = 12 : retour à 0')
brace(ax, f(12), f(13), 26, 'resultat', label='reste 1')
box(ax, 8, 3, 72, 9, 'resultat', label='13 quarts de tour : position 1', size='s')
save(fig, '48-003')
