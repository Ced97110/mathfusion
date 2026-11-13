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

fig, ax = canvas(86)
x0, W0 = 24, 50
ys = [62 - i * 12 for i in range(5)]
line(ax, [(x0 + W0 / 2, 74), (x0 + W0 / 2, ys[-1] - 2)], 'sujet', lw=0.8, dash=True)
line(ax, [(x0 + W0 / 3, 74), (x0 + W0 / 3, ys[-1] - 2)], 'varie', lw=0.8, dash=True)
text(ax, x0 + W0 / 2 + 1, 77, '1/2', 'sujet', 's', ha='left')
text(ax, x0 + W0 / 3 - 1, 77, '1/3', 'varie', 's', ha='right')
for y, n in zip(ys, (2, 3, 4, 5, 6)):
    bar(ax, x0, y, W0, 8, n, {})
    text(ax, 4, y + 4, f'{n} parts', 'encre', 's', ha='left')
    oks = []
    for f in (1 / 2, 1 / 3):
        ok = abs(f * n - round(f * n)) < 1e-9; oks.append(ok)
        disc(ax, x0 + f * W0, y + 4, 1.7, 'resultat' if ok else 'limite')
    good = all(oks)
    text(ax, x0 + W0 + 4, y + 4, 'oui' if good else 'non', 'resultat' if good else 'limite', 'm', ha='left', weight='bold')
text(ax, x0 + W0 / 2, ys[-1] - 6, '6 : le plus petit qui réussit', 'resultat', 's')
save(fig, '07-009')
