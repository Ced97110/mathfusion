import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rect(ax, x, y, w, h, role, fill=True, lw=0.7, dash=False):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, ls='--' if dash else '-', zorder=2))
def bar(ax, x, y, w, h, n, roles, dash=()):
    for i in range(n):
        r = roles.get(i)
        rect(ax, x + i * w / n, y, w / n, h, r or 'fixe', fill=r is not None, dash=i in dash)
    rect(ax, x, y, w, h, 'encre', fill=False, lw=1.0)
def frac(ax, x, y, a, d, ra='sujet', rd='sujet', size='l', gap=3.2):
    text(ax, x, y + gap, a, ra, size); text(ax, x, y - gap, d, rd, size)
    line(ax, [(x - 3, y), (x + 3, y)], 'encre', lw=0.8)

fig, ax = canvas(84)
text(ax, 8, 79, 'avant', 'fixe', ha='left', size='s')
bar(ax, 8, 64, 72, 8, 2, {0: 'sujet'}); text(ax, 84, 68, 'A', 'sujet', ha='right', size='s'); text(ax, 26, 75, '1/2', 'sujet', size='s')
bar(ax, 8, 48, 72, 8, 3, {0: 'varie'}); text(ax, 84, 52, 'B', 'varie', ha='right', size='s'); text(ax, 20, 59, '1/3', 'varie', size='s')
arrow(ax, (66, 45), (66, 38), 'varie'); text(ax, 62, 41.5, 'recouper en 6', 'varie', ha='right', size='s')
text(ax, 8, 41.5, 'après', 'fixe', ha='left', size='s')
bar(ax, 8, 26, 72, 8, 6, {0: 'sujet', 1: 'sujet', 2: 'sujet'}); text(ax, 26, 21.5, '3 parts', 'sujet', size='s')
bar(ax, 8, 8, 72, 8, 6, {0: 'varie', 1: 'varie'}); text(ax, 20, 3.5, '2 parts', 'varie', size='s')
line(ax, [(44, 64), (44, 34)], 'sujet', lw=1.0, dash=True)
line(ax, [(32, 48), (32, 16)], 'varie', lw=1.0, dash=True)
save(fig, '07-007')
