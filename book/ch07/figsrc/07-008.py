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
rect(ax, 8, 50, 72, 9, 'fixe', fill=False); rect(ax, 8, 50, 36, 9, 'sujet')
text(ax, 26, 54.5, '1 part', 'sujet'); brace(ax, 8, 44, 48, 'sujet', label='taille 1/2')
rect(ax, 8, 22, 72, 9, 'fixe', fill=False); rect(ax, 8, 22, 24, 9, 'varie')
text(ax, 20, 26.5, '1 part', 'varie'); brace(ax, 8, 32, 20, 'varie', label='taille 1/3')
text(ax, 44, 63, 'même mot « part »', 'fixe')
text(ax, 44, 4, 'le mot « part » oublie la taille', 'limite', 's')
save(fig, '07-008')
