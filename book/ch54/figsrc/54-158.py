import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$\mathbb{Z}/6$, diviseur $g=2x$, dividende $0$', 'sujet', 'm')
# horloge à 6 positions
cx, cy, R = 20, 50, 13
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=1))
for k in range(6):
    a = math.radians(90 - 60 * k)
    text(ax, cx + (R - 4) * math.cos(a), cy + (R - 4) * math.sin(a), str(k), 'fixe', 's')
text(ax, cx, cy - 1, r'$6=0$', 'varie', 's')
# deux écritures du même dividende
box(ax, 42, 52, 44, 11, 'sujet', label=r'$0=0\times2x+0$', size='s')
box(ax, 42, 36, 44, 11, 'autre', label=r'$0=3\times2x+0$', size='s')
text(ax, 64, 31, r'$3\times2=6=0$', 'varie', 's')
text(ax, 20, 28, 'horloge à 6 heures', 'fixe', 's')
text(ax, 44, 16, r'quotients $0$ et $3$ : différents', 'limite', 'm')
text(ax, 44, 8, 'mêmes dividende et reste', 'limite', 's')
save(fig, '54-158')
