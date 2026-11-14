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

fig, ax = canvas(90)
box(ax, 3, 72, 40, 12, 'fixe', label='isomorphisme')
box(ax, 45, 72, 40, 12, 'sujet', label='homomorphisme')
box(ax, 3, 48, 40, 12, 'resultat', label='respecte l’opération', size='s')
box(ax, 45, 48, 40, 12, 'resultat', label='respecte l’opération', size='s')
text(ax, 65, 43, r'$f(7+6)=f(7)+f(6)$', 'resultat', 's')
box(ax, 3, 20, 40, 12, 'resultat', label='un pour un')
box(ax, 45, 20, 40, 12, 'limite', label='un pour un : abandonné', size='s', dash=True)
text(ax, 65, 15, r'$f(1)=f(5)$', 'limite', 's')
save(fig, '48-008')
