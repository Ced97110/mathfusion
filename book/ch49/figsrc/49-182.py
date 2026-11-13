import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
sizes = [1, 1, 2, 2, 2]; d = 4.2; pad = 1.6; gap = 3
def row(y, order, joint):
    ws = [n * d + 2 * pad for n in sizes]
    xs = []; x = 10
    for k, w in enumerate(ws):
        xs.append(x); x += w + (1.2 if (joint and k == 1) else gap)
    for k, n in enumerate(sizes):
        role = ('fixe' if k < 2 else 'sujet') if joint else 'sujet'
        box(ax, xs[k], y - 4, ws[k], 8, role)
        for i in range(n): disc(ax, xs[k] + pad + d / 2 + i * d, y, 1.4, role)
    return xs, ws
text(ax, 4, 80, 'action quelconque : orbites', 'sujet', 'm', ha='left', weight='bold')
xs, ws = row(70, 0, False)
text(ax, W / 2, 60, 'tailles : 1, 1, 2, 2, 2', 'sujet', 's')
arrow(ax, (44, 56), (44, 44), 'varie')
text(ax, 48, 50, 'G agit sur lui-même', 'varie', 's', ha='left')
text(ax, 4, 38, 'conjugaison : classes', 'sujet', 'm', ha='left', weight='bold')
xs, ws = row(26, 0, True)
brace(ax, xs[0], xs[1] + ws[1], 19, 'fixe', r'centre $|C|$', depth=2.4)
brace(ax, xs[2], xs[4] + ws[4], 19, 'sujet', 'classes à plusieurs éléments', depth=2.4)
text(ax, W / 2, 5, r'$|G| = |C| + \sum_j [G:C(y_j)]$', 'resultat', 'm', weight='bold')
save(fig, '49-182')
