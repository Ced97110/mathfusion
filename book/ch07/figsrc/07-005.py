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

fig, ax = canvas(80)
frac(ax, 12, 68, '1', '2', 'sujet', 'sujet'); text(ax, 22, 68, '+', 'encre', 'l'); frac(ax, 32, 68, '1', '3', 'varie', 'varie')
text(ax, 42, 68, '=', 'encre', 'l'); frac(ax, 52, 68, '2', '5', 'limite', 'limite')
text(ax, 72, 72, 'règle fausse', 'limite'); text(ax, 72, 64, 'haut + haut', 'limite', 's')
text(ax, 72, 58, 'bas + bas', 'limite', 's')
bar(ax, 8, 32, 72, 8, 2, {0: 'sujet'}); text(ax, 8, 43, '1/2', 'sujet', ha='left')
bar(ax, 8, 14, 72, 8, 5, {0: 'limite', 1: 'limite'}); text(ax, 8, 25, '2/5', 'limite', ha='left')
text(ax, 62, 6, '2/5 est plus petit que 1/2', 'limite', 's')
save(fig, '07-005')
