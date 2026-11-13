import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$\pi$ sur les fractions', 'encre', 'm')
labs = ['1', r'$\pi$', r'$\pi^2$', r'$\pi^3$']
for i, s in enumerate(labs):
    box(ax, 4 + i * 17, 46, 15, 13, 'autre', label=s, size='m')
text(ax, 77, 52.5, '…', 'autre', 'xl')
brace(ax, 4, 83, 45, 'autre', label='briques sans fin, indépendantes')
box(ax, 26, 8, 36, 14, 'limite', label=r'$1/\pi$', size='l', dash=True)
text(ax, 44, 27, 'hors de $F[\\pi]$', 'limite', 's')
text(ax, 44, 3.5, 'pas une valeur de polynôme', 'limite', 's')
save(fig, '61-087')
