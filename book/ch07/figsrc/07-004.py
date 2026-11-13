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
rect(ax, 8, 58, 36, 9, 'sujet'); rect(ax, 44, 58, 24, 9, 'varie'); rect(ax, 68, 58, 12, 9, 'fixe', fill=False)
text(ax, 26, 70, '1/2', 'sujet'); text(ax, 56, 70, '1/3', 'varie')
brace(ax, 8, 68, 56, 'limite', label='« 2 parts » ? tailles ≠')
bar(ax, 8, 16, 72, 9, 6, {0: 'sujet', 1: 'sujet', 2: 'sujet', 3: 'varie', 4: 'varie'})
text(ax, 26, 28, '3/6', 'sujet'); text(ax, 56, 28, '2/6', 'varie')
brace(ax, 8, 68, 14, 'resultat', label='5 parts de même taille')
save(fig, '07-004')
