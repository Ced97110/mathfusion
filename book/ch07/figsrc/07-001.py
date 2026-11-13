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
text(ax, 44, 57, '1 € = 100 centimes', 'fixe', 'm')
rect(ax, 4, 36, 80, 9, 'fixe', fill=False); rect(ax, 4, 36, 20, 9, 'sujet'); rect(ax, 24, 36, 8, 9, 'varie')
text(ax, 14, 48, '25/100', 'sujet'); text(ax, 30, 48, '10/100', 'varie', ha='left')
arrow(ax, (28, 34), (18, 25), 'varie', curve=0.2)
rect(ax, 4, 14, 80, 9, 'fixe', fill=False); rect(ax, 4, 14, 28, 9, 'resultat')
text(ax, 18, 26.5, '35/100', 'resultat'); text(ax, 60, 24, '25 + 10 = 35', 'encre')
text(ax, 44, 5, 'le 100 reste : même unité', 'fixe')
save(fig, '07-001')
