import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
RO = {2: 'sujet', 3: 'varie', 5: 'resultat'}
X1, X2, XM = 22, 66, 44
ys = [86, 66, 46, 26, 6]
def chain(xs_sizes, x):
    pts = []
    for y, s in zip(ys, xs_sizes): pts.append((x, y, s))
    return pts
left = [60, 20, 4, 2, 1]
right = [60, 30, 15, 3, 1]
def draw(sizes, x):
    for k in range(4):
        r = sizes[k] // sizes[k + 1]
        arrow(ax, (x if k else XM, ys[k] - 4.2), (x if k < 3 else XM, ys[k + 1] + 4.2), RO[r], lw=1.6)
for k in range(1, 4):
    box(ax, X1 - 6, ys[k] - 4, 12, 8, 'fixe', label=str(left[k]))
    box(ax, X2 - 6, ys[k] - 4, 12, 8, 'fixe', label=str(right[k]))
box(ax, XM - 6, ys[0] - 4, 12, 8, 'fixe', label='60')
box(ax, XM - 6, ys[4] - 4, 12, 8, 'fixe', label='1')
draw(left, X1); draw(right, X2)
text(ax, X1, 93, 'suite 1', 'encre', 's'); text(ax, X2, 93, 'suite 2', 'encre', 's')
for k, (r, lab) in enumerate(((2, '2'), (3, '3'), (5, '5'))):
    x = 1.5 + k * 5
    ax.add_patch(Rectangle((x, 62 - 12), 3.5, 1.6, fc=COL[RO[r]], ec='none', zorder=2))
    text(ax, x + 1.75, 62 - 15, lab, RO[r], 's')
text(ax, 8, 56, 'facteur', 'encre', 's')
save(fig, '64-098')
