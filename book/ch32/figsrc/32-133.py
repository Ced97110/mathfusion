import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(52)
text(ax, 44, 47, 'la somme doit valoir 1', 'encre', 's')
w, g, x0 = 19, 2, 3
angs = ['0°', '90°', '180°', '270°']
sums = [r'$0+1=1$', r'$1+0=1$', r'$0+(-1)=-1$', r'$-1+0=-1$']
ok = [True, True, False, False]
for i in range(4):
    x = x0 + i * (w + g); r = 'resultat' if ok[i] else 'limite'
    box(ax, x, 30, w, 10, 'fixe', True, label=angs[i], size='m')
    arrow(ax, (x + w / 2, 30), (x + w / 2, 26), 'fixe')
    box(ax, x, 14, w, 12, r, True, label=sums[i], size='s')
    text(ax, x + w / 2, 8, 'vrai' if ok[i] else 'faux', r, 's')
save(fig, '32-133')
