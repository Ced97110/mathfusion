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

fig, ax = canvas(56)
bar(ax, 8, 38, 72, 9, 2, {0: 'sujet'}); text(ax, 8, 51, 'matin : 1/2 du mur', 'sujet', ha='left')
bar(ax, 8, 20, 72, 9, 3, {0: 'varie'}); text(ax, 8, 33, 'après-midi : 1/3 du mur', 'varie', ha='left')
text(ax, 44, 8, '1/2 + 1/3 = ?', 'encre', 'l')
save(fig, '07-002')
