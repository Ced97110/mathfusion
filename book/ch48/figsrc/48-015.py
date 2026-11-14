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

fig, ax = canvas(52)
f = numberline(ax, 8, 76, 28, 0, 10, labels=False, arrow_right=False)
for v in range(11):
    role = ['sujet', 'varie', 'resultat', None][v % 4]
    if role is None: continue
    disc(ax, f(v), 28, 2.8, role, label=str(v), size='s')
for v in (0, 4, 8):
    arrow(ax, (f(v) + 1.5, 31), (f(v + 1) - 1.5, 31), 'varie', curve=-0.8, lw=0.9)
    arrow(ax, (f(v) + 1.5, 25), (f(v + 2) - 1.5, 25), 'resultat', curve=0.6, lw=0.9)
text(ax, f(0.5), 38, '+ 1', 'varie', 's')
text(ax, f(1), 17, '+ 2', 'resultat', 's')
text(ax, 44, 6, 'fibre = le noyau décalé', 'encre', 's')
save(fig, '48-015')
