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

fig, ax = canvas(70)
text(ax, 62, 63, 'avant', 'fixe'); text(ax, 62, 35, 'après', 'fixe')
bar(ax, 8, 50, 72, 9, 2, {0: 'sujet'}); text(ax, 62, 54.5, '1/2', 'fixe', size='s')
arrow(ax, (86, 48), (86, 36), 'varie'); text(ax, 78, 42, 'recouper', 'varie', ha='right', size='s')
bar(ax, 8, 22, 72, 9, 6, {0: 'sujet', 1: 'sujet', 2: 'sujet'}); text(ax, 62, 26.5, '3/6', 'fixe', size='s')
line(ax, [(8, 20), (8, 60)], 'fixe', dash=True); line(ax, [(44, 20), (44, 60)], 'fixe', dash=True)
brace(ax, 8, 44, 18, 'resultat', label='même longueur')
save(fig, '07-010')
