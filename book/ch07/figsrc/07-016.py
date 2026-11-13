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
frac(ax, 20, 62, 'a', 'd', 'sujet', 'fixe', size='xl', gap=4.2); text(ax, 34, 62, '+', 'encre', 'xl')
frac(ax, 48, 62, 'b', 'd', 'varie', 'fixe', size='xl', gap=4.2)
text(ax, 20, 76, '1re fraction', 'sujet', 's'); arrow(ax, (20, 73.5), (20, 69), 'sujet')
text(ax, 52, 76, '2e fraction', 'varie', 's'); arrow(ax, (48, 73.5), (48, 69), 'varie')
for y, n, a, b in ((32, 5, 3, 1), (10, 9, 2, 4)):
    w = 32
    bar(ax, 6, y, w, 8, n, {i: 'sujet' for i in range(a)}); text(ax, 6 + w + 6, y + 4, '+', 'encre', 'l')
    bar(ax, 50, y, w, 8, n, {i: 'varie' for i in range(b)})
    text(ax, 6 + w / 2, y - 4, f'a = {a}', 'sujet', 'm'); text(ax, 50 + w / 2, y - 4, f'b = {b}', 'varie', 'm')
save(fig, '07-016')
