import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 13; xs = 26
def seg(x, y, w, role, mark=True):
    line(ax, [(x, y), (x + w, y)], role, lw=2)
    for xx in (x, x + w): line(ax, [(xx, y - 1.5), (xx, y + 1.5)], role, lw=1)
# row 1 : square
yr = 44
box(ax, 4, yr - u / 2, u, u, 'sujet', r=0.3)
for i in range(4): seg(xs + i * u, yr, u - 0.4, 'sujet')
text(ax, 4 + u / 2, yr - u / 2 - 4, 'côté 1', 'sujet', 's')
text(ax, xs + 2 * u, yr + 6.5, 'périmètre : 4 fois 1', 'sujet', 's')
text(ax, xs + 2 * u, yr - 6, 'chaque pièce tombe juste', 'resultat', 's')
# row 2 : circle
yc = 16
disc(ax, 4 + u / 2, yc, u / 2, 'sujet')
line(ax, [(4, yc), (4 + u, yc)], 'varie', lw=1.2)
text(ax, 4 + u / 2, yc - u / 2 - 4, 'diamètre 1', 'varie', 's')
for i in range(3): seg(xs + i * u, yc, u - 0.4, 'sujet')
seg(xs + 3 * u, yc, math.pi * u - 3 * u, 'limite')
text(ax, xs + 1.5 * u, yc + 6.5, 'tour : 3 fois 1 + un bout', 'sujet', 's')
xe = xs + math.pi * u
line(ax, [(xe + 0.6, yc), (xe + 6, yc)], 'limite', lw=2, dash=True)
text(ax, xe + 8, yc, '…', 'limite', 'l', ha='left')
arrow(ax, (xs + 3 * u + 1, yc - 5), (xs + 3 * u + 1, yc - 1.8), 'limite')
text(ax, xs + 3 * u + 1, yc - 8, 'ne finit jamais', 'limite', 's', weight='bold')
save(fig, '11-161')
