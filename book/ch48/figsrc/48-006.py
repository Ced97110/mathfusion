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
text(ax, 44, 85, 'cas de 5 et 9 : respecté', 'resultat', 'm', weight='bold')
text(ax, 22, 77, 'additionner, puis position', 'varie', 's')
text(ax, 66, 77, 'positions, puis additionner', 'autre', 's')
box(ax, 2, 62, 40, 11, 'varie', label='5 + 9 = 14 → position 2', size='s')
box(ax, 46, 62, 40, 11, 'autre', label='positions 1 + 1 = 2', size='s')
text(ax, 44, 67.5, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 49, 'le carré ne la respecte pas', 'limite', 'm', weight='bold')
text(ax, 22, 41, 'additionner, puis carré', 'varie', 's')
text(ax, 66, 41, 'carrés, puis additionner', 'autre', 's')
box(ax, 2, 26, 40, 11, 'varie', label=r'$(3+2)^2 = 25$', size='s')
box(ax, 46, 26, 40, 11, 'autre', label=r'$3^2+2^2 = 9+4 = 13$', size='s')
text(ax, 44, 31.5, r'$\neq$', 'limite', 'l', weight='bold')
save(fig, '48-006')
