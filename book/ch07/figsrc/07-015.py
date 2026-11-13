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

fig, ax = canvas(72)
frac(ax, 10, 64, 'a', 'd', 'sujet', 'fixe'); text(ax, 20, 64, '−', 'encre', 'l'); frac(ax, 30, 64, 'b', 'd', 'varie', 'fixe')
text(ax, 40, 64, '=', 'encre', 'l'); frac(ax, 54, 64, 'a − b', 'd', 'resultat', 'fixe', gap=3.4)
bar(ax, 8, 28, 72, 9, 8, {0: 'resultat', 1: 'resultat', 2: 'resultat', 3: 'resultat', 4: 'varie', 5: 'varie', 6: 'varie'})
brace(ax, 8, 71, 40, 'sujet', down=False, label='a = 7 parts')
brace(ax, 8, 44, 26, 'resultat', label='a − b = 4')
brace(ax, 44, 71, 26, 'varie', label='b = 3 retirées')
text(ax, 8, 4, '7/8 − 3/8 = 4/8', 'encre', ha='left')
save(fig, '07-015')
