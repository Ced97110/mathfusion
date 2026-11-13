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

fig, ax = canvas(74)
frac(ax, 10, 66, 'a', 'd', 'sujet', 'fixe'); text(ax, 20, 66, '+', 'encre', 'l'); frac(ax, 30, 66, 'b', 'd', 'varie', 'fixe')
text(ax, 40, 66, '=', 'encre', 'l'); frac(ax, 54, 66, 'a + b', 'd', 'resultat', 'fixe', gap=3.4)
bar(ax, 8, 40, 72, 9, 7, {0: 'sujet', 1: 'sujet', 2: 'varie', 3: 'varie', 4: 'varie', 5: 'varie'})
text(ax, 8, 52, '2/7 + 4/7', 'encre', ha='left')
text(ax, 8, 28, '1. même d : 7 et 7', 'fixe', ha='left')
text(ax, 8, 20, '2. on additionne : 2 + 4 = 6', 'encre', ha='left')
text(ax, 8, 12, '3. on garde d = 7', 'fixe', ha='left')
text(ax, 62, 52, '= 6/7', 'resultat', 'l', ha='left')
save(fig, '07-014')
