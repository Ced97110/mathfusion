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
box(ax, 6, 64, 76, 12, 'sujet', label='même reste modulo 4 : 2')
box(ax, 6, 30, 76, 24, 'resultat', fill=False, dash=True)
text(ax, 44, 49.5, 'le même paquet', 'resultat', 's')
for cx, v in zip((22, 40, 58), ('2', '6', '10')):
    ibox(ax, cx, 38, v, 'resultat', w=12, h=8)
dots(ax, 72, 38, 'resultat')
box(ax, 6, 8, 76, 12, 'autre', label='même position du bouton : 2')
arrow(ax, (44, 64), (44, 54.5), 'sujet'); arrow(ax, (44, 20), (44, 29.5), 'autre')
save(fig, '48-014')
