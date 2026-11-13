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

fig, ax = canvas(62)
bar(ax, 8, 40, 72, 9, 6, {0: 'sujet', 1: 'sujet', 2: 'sujet'}); text(ax, 8, 53, '1/2 = 3 parts', 'sujet', ha='left')
bar(ax, 8, 22, 72, 9, 6, {0: 'varie', 1: 'varie'}); text(ax, 8, 35, '1/3 = 2 parts', 'varie', ha='left')
brace(ax, 8, 20, 20, 'fixe', label='1 part = 1/6')
text(ax, 60, 55, 'mur coupé en 6', 'fixe')
save(fig, '07-003')
