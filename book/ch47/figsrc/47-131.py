import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'1. on choisit $g=s$', 'varie', 'm')
res = [r'$1$', r'$r^{3}$', r'$r^{2}$', r'$r$']
src = [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$']
xs = [14, 32, 50, 68]
text(ax, 44, 68, r'2. on conjugue chaque élément', 'varie', 'm')
for x, l in zip(xs, res): box(ax, x - 6, 52, 12, 9, 'varie', label=l)
for x, l in zip(xs, src): box(ax, x - 6, 14, 12, 9, 'sujet', label=l)
# each result goes to the equal element of N
tgt = {0: 0, 1: 3, 2: 2, 3: 1}
for i, j in tgt.items():
    arrow(ax, (xs[i], 51.5), (xs[j], 23.5), 'resultat', lw=0.8)
text(ax, 44, 8, '3. on compare à N', 'varie', 'm')
text(ax, 44, 2.5, r'même ensemble : $gNg^{-1}=N$', 'resultat', 's')
save(fig, '47-131')
