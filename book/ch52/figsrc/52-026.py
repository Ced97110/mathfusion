import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def arc(ax, x0, x1, y, h, role, dash=False):
    t = np.linspace(0, 1, 40); xs = x0 + (x1 - x0) * t; ys = y + 4 * h * t * (1 - t)
    ax.plot(xs, ys, color=COL[role], lw=1.1, ls='--' if dash else '-', zorder=3)
fig, ax = canvas(70)
for x0, role, name, g, rr in [(3, 'sujet', r'$4\mathbb{Z}$', ('9−6', '9−5'), 0), (46, 'autre', r'$3\mathbb{Z}$', ('9−6', '9−5'), 1)]:
    box(ax, x0, 12, 39, 54, role, fill=False)
    text(ax, x0 + 19.5, 60, name, role, 'l')
    xs = {5: x0 + 7, 6: x0 + 19, 9: x0 + 33}
    for n, x in xs.items(): disc(ax, x, 36, 3.6, 'fixe', label=str(n), size='m')
    if rr == 0:
        arc(ax, xs[5], xs[9], 40, 8, 'resultat'); text(ax, x0 + 20, 53, '9 − 5 = 4', 'resultat', 's')
        arc(ax, xs[6], xs[9], 32, -6, 'limite', True); text(ax, x0 + 26, 22, '9 − 6 = 3', 'limite', 's')
    else:
        arc(ax, xs[6], xs[9], 40, 6, 'resultat'); text(ax, x0 + 26, 51, '9 − 6 = 3', 'resultat', 's')
        arc(ax, xs[5], xs[9], 32, -9, 'limite', True); text(ax, x0 + 20, 22, '9 − 5 = 4', 'limite', 's')
text(ax, 22, 6, 'trait plein : équivalents', 'resultat', 's'); text(ax, 66, 6, 'pointillé : séparés', 'limite', 's')
save(fig, '52-026')
