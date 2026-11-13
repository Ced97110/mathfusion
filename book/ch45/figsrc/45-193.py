import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def clock(cx, cy, n, R=8.0):
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
    for i in range(n):
        a = math.radians(90 - 360 * i / n)
        disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.9, 'sujet', label=str(i), size='s')
text(ax, 17, 38, r'$\mathbb{Z}/m$', 'sujet', 'xl')
text(ax, 17, 28, 'horloge à', 'fixe', 's')
text(ax, 17, 24.5, r'$m$ heures', 'varie', 's')
arrow(ax, (31, 34), (38, 34), 'varie')
for cx, n in ((51, 2), (75, 3)):
    clock(cx, 34, n)
    text(ax, cx, 48, f'ℤ/{n}', 'sujet', 'm')
    text(ax, cx, 19, f'{n} heures', 'varie', 's')
save(fig, '45-193')
