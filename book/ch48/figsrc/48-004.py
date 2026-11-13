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
text(ax, 17, 64, 'quarts de tour', 'encre', 's')
text(ax, 71, 64, 'position', 'encre', 's')
for s, p, y in zip(['7', '6', '13'], ['3', '2', '1'], [52, 38, 24]):
    ibox(ax, 17, y, s, 'fixe', w=20, h=9)
    ibox(ax, 71, y, BAR(p), 'resultat', w=20, h=9)
    arrow(ax, (28, y), (60, y), 'sujet')
    text(ax, 44, y + 3.5, r'$f$', 'sujet', 'm')
text(ax, 44, 8, r'$f(7)=\bar{3}$', 'sujet', 'l')
save(fig, '48-004')
