import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
yb, bh, bw = 42, 16, 13
xs = [2, 16.5, 31, 45.5, 62]

def cluster(x):
    for dx in (4, 9):
        for dy in (4.2, 11.8):
            ax.add_patch(Circle((x + dx, yb + dy - 0.2), 1.7, ec=COL['sujet'], fc=FILL['sujet'], lw=0.7, zorder=3))

for k, x in enumerate(xs):
    box(ax, x, yb, bw, bh, 'fixe')
    cluster(x)
    text(ax, x + bw / 2, yb + bh + 3.5, f'cas {k + 1}', 'sujet' if k < 4 else 'varie', 's')
# le cinquième objet b, hors du groupe d'objets de sigma
disc(ax, 82, yb + bh / 2, 3.4, 'varie', label=r'$b$')
brace(ax, 2, 58.5, yb - 2, 'sujet', label='dans les objets de $\\sigma$')
brace(ax, 62, 85.5, yb - 2, 'varie', label='un objet de plus')

text(ax, 44, 27, r'seul le cas 5 exige $b$ : $n\geq5$', 'varie', 's')
# n = 4 : pas de cinquième objet
box(ax, 4, 4, 80, 15, 'limite')
text(ax, 44, 14.8, r'$n=4$ : $V$ est normal dans $A_4$,', 'limite', 's')
text(ax, 44, 8.8, 'sans 3-cycle : pas de 5e objet', 'limite', 's')
save(fig, '64-135')
