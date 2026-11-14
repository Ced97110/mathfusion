import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [3, 34, 65]
labs = [r'$\mathbb{Q}$', r'$\mathbb{Q}(\sqrt{2})$', r'$\mathbb{R}$']
for x, s in zip(xs, labs):
    box(ax, x, 26, 20, 14, 'sujet', label=s, size='m')
arrow(ax, (23, 33), (34, 33), 'resultat')
arrow(ax, (54, 33), (65, 33), 'limite')
text(ax, 28.5, 38, '2', 'resultat', 'l', weight='bold')
text(ax, 28.5, 28, 'fini', 'resultat', 's')
text(ax, 59.5, 38, r'$\infty$', 'limite', 'l', weight='bold')
text(ax, 59.5, 28, 'infini', 'limite', 's')
brace(ax, 3, 85, 24, 'limite', label=r'total : $\infty$')
text(ax, 44, 6, 'un étage fini ne suffit pas', 'limite', 's')
save(fig, '61-099')
