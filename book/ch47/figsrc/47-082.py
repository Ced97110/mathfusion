import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [10, 28, 46, 64]; vals = ['2', '4', '8', '6']
text(ax, 44, 57, r'puissances de 2 dans $\times$ mod 10', 'sujet', 'm')
for i, (x, v) in enumerate(zip(xs, vals)):
    box(ax, x, 38, 12, 10, 'sujet', label=v, size='l')
    if i < 3: arrow(ax, (x + 12.5, 43), (xs[i + 1] - 0.5, 43), 'varie')
arrow(ax, (xs[3] + 6, 37.5), (xs[0] + 6, 37.5), 'varie', curve=-0.45)
text(ax, 44, 24.5, 'on recommence', 'varie', 's')
box(ax, 76.5, 38, 9.5, 10, 'limite', fill=False, label='1', size='l', dash=True)
text(ax, 81.3, 51.5, 'jamais', 'limite', 's')
text(ax, 44, 12, r'$2^{10}=1024$ : reste 4, pas 1', 'limite', 'm')
text(ax, 44, 4.5, 'ce n’est pas un groupe', 'fixe', 's')
save(fig, '47-082')
