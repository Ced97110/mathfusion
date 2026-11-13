import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [14, 34, 54, 74]; labs = ['1', r'$r$', r'$r^2$', r'$r^3$']
labs = ['1', r'$r$', r'$r^2$', r'$r^3$']
text(ax, 44, 63, 'les 4 rotations ⟨r⟩', 'sujet', 'm')
for x, l in zip(xs, labs):
    disc(ax, x, 52, 4.2, 'sujet', label=l, size='m'); disc(ax, x, 24, 4.2, 'sujet', label=l, size='m')
for i, j in [(0, 0), (2, 2)]: arrow(ax, (xs[i], 47.4), (xs[j], 28.6), 'varie')
arrow(ax, (xs[1] + 1, 47.4), (xs[3] - 1, 28.6), 'varie', curve=0.12)
arrow(ax, (xs[3] - 1, 47.4), (xs[1] + 1, 28.6), 'varie', curve=0.12)
text(ax, 44, 14, r'après conjugaison par $s$', 'sujet', 'm')
box(ax, 6, 1, 76, 8, 'resultat', label=r'$s\,r\,s^{-1}=r^{-1}$ : encore une rotation', size='s')
save(fig, '47-152')
