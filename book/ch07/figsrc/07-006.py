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

fig, ax = canvas(92)
text(ax, 8, 87, 'deux moitiés de pizza', 'resultat', ha='left')
bar(ax, 8, 70, 72, 8, 2, {0: 'sujet', 1: 'varie'}); text(ax, 26, 81, '1/2', 'sujet', 's'); text(ax, 62, 81, '1/2', 'varie', 's')
text(ax, 44, 64, '1/2 + 1/2 = 1 entier : vrai', 'resultat')
line(ax, [(8, 58), (80, 58)], 'fixe', lw=0.5, dash=True)
text(ax, 8, 52, 'règle fausse : on additionne tout', 'limite', 's', ha='left')
text(ax, 44, 41, r'$\frac{1+1}{2+2}=\frac{2}{4}$', 'limite', 'l')
bar(ax, 8, 22, 72, 8, 4, {0: 'limite', 1: 'limite'})
brace(ax, 8, 44, 21, 'limite', '2/4 = 1/2 seulement', depth=1.6)
text(ax, 44, 6, 'deux moitiés : pas une moitié', 'limite', 's')
save(fig, '07-006')
