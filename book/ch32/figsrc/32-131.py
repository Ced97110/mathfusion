import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(66)
text(ax, 44, 61, 'trouvés par le calcul', 'fixe', 's')
xs = [2, 31.5, 61]; w = 25
for x, a in zip(xs, ['0°', '90°', '180°']):
    box(ax, x, 42, w, 10, 'fixe', True, label=a, size='l')
roles = ['resultat', 'varie', 'resultat']
labs = [r'$0=0$', "$\\tan 90°$\nn'existe pas", r'$0=0$']
for x, r, l in zip(xs, roles, labs):
    arrow(ax, (x + w / 2, 42), (x + w / 2, 34), 'fixe')
    box(ax, x, 18, w, 16, r, True, label=l, size='s')
for x, r, l in zip(xs, roles, ['vrai', 'ni vrai ni faux', 'vrai']):
    text(ax, x + w / 2, 12, l, r, 's')
text(ax, 44, 4, '90° : solution interdite', 'varie', 'm', weight='bold')
save(fig, '32-131')
