import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
xs = [16, 30, 44]
def dots(x, y, role):
    for k in range(3): disc(ax, x + k * 3.2, y, 0.45, role)
# fini
text(ax, 4, 94, 'fini : impossible', 'limite', 'm', ha='left', weight='bold')
box(ax, 8, 70, 44, 18, 'sujet', fill=False)
for x, s in zip(xs, '123'): disc(ax, x, 79, 3.5, 'sujet', label=s)
box(ax, 8, 46, 30, 16, 'autre', fill=False, dash=True)
for x, s in zip(xs[:2], '12'): disc(ax, x, 54, 3.5, 'autre', label=s)
text(ax, 42, 54, 'partie stricte :\nplus petite', 'autre', 's', ha='left')
arrow(ax, (xs[0], 75), (xs[0], 58), 'resultat'); arrow(ax, (xs[1], 75), (xs[1], 58), 'resultat')
arrow(ax, (xs[2] - 1, 75.5), (xs[1] + 2.5, 56.5), 'limite')
# infini
text(ax, 4, 38, r'infini : $n \to 2n$, possible', 'resultat', 'm', ha='left', weight='bold')
box(ax, 8, 20, 62, 12, 'sujet', fill=False)
for x, s in zip(xs, '012'): disc(ax, x, 26, 3.5, 'sujet', label=s)
dots(53, 26, 'sujet')
box(ax, 8, 2, 62, 12, 'autre', fill=False, dash=True)
for x, s in zip(xs, '024'): disc(ax, x, 8, 3.5, 'autre', label=s)
dots(53, 8, 'autre')
for x in xs: arrow(ax, (x, 22.5), (x, 12), 'resultat')
save(fig, '43-113')
