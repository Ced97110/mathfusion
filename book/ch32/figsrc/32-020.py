import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, cx, cy, r, a0, a1, role):
    line(ax, [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(a0, a1 + 1, 2)], role, lw=1.0)
fig, ax = canvas(100)
cx, cy, R = 44, 64, 26
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=1))
line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
dx = R * math.cos(math.radians(30)); dy = R * 0.5
O = (cx, cy); P = (cx + dx, cy + dy); H = (cx + dx, cy); Pp = (cx - dx, cy + dy); Hp = (cx - dx, cy)
poly(ax, [O, H, P], 'sujet'); poly(ax, [O, Hp, Pp], 'autre')
arc(ax, cx, cy, 7, 0, 30, 'sujet'); arc(ax, cx, cy, 7, 150, 180, 'autre')
text(ax, cx + 13, cy + 2.6, '30°', 'sujet', 's'); text(ax, cx - 13, cy + 2.6, '30°', 'autre', 's')
disc(ax, *P, 1.2, 'sujet'); disc(ax, *Pp, 1.2, 'autre')
text(ax, cx, cy - 3.2, r'$O$', 'encre', 's'); text(ax, H[0], cy - 3.2, r'$H$', 'sujet', 's'); text(ax, Hp[0], cy - 3.2, r"$H'$", 'autre', 's')
text(ax, P[0] + 3.5, P[1] + 2.5, r'$P$', 'sujet', 's'); text(ax, Pp[0] - 3.5, Pp[1] + 2.5, r"$P'$", 'autre', 's')
text(ax, cx + 9, cy + 10.5, '1', 'sujet', 's'); text(ax, H[0] + 3.2, cy + dy / 2, '0,5', 'sujet', 's'); text(ax, cx + dx / 2, cy - 3.2, '0,87', 'sujet', 's')
bx = [3, 33, 63]; labs = ['3 côtés égaux', 'angles égaux', '180° − 30° = 150°']; roles = ['fixe', 'varie', 'resultat']
for x, lb, r in zip(bx, labs, roles):
    box(ax, x, 8, 24, 14, r, label=lb, size='s', lw=1.6 if r == 'varie' else 0.8)
for i in range(2): arrow(ax, (bx[i] + 24.5, 15), (bx[i + 1] - 0.5, 15), 'fixe')
text(ax, 45, 26, 'étape clé', 'varie', 's')
save(fig, '32-020')
