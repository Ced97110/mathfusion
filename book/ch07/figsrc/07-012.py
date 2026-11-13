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

fig, ax = canvas(76)
bar(ax, 8, 54, 72, 9, 5, {0: 'sujet', 1: 'sujet', 2: 'sujet', 3: 'varie'})
text(ax, 8, 67, '3/5 + 1/5 : cinquièmes', 'resultat', ha='left')
brace(ax, 8, 62.4, 52, 'resultat', label='4 parts : 4/5')
bar(ax, 8, 18, 72, 9, 10, {0: 'limite', 1: 'limite', 2: 'limite', 3: 'limite'})
text(ax, 8, 31, '5 + 5 = 10 ? (faux)', 'limite', ha='left')
brace(ax, 8, 36.8, 16, 'limite', label='4/10 : parts plus petites')
save(fig, '07-012')
