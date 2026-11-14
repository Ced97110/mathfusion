import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'propriété : « deux fois = neutre »', 'encre', 'm', weight='bold')
box(ax, 2, 28, 46, 41, 'autre')
text(ax, 25, 64, 'rectangle', 'autre', 'm')
for i, s in enumerate([r'$h^2=e$', r'$v^2=e$', r'$d^2=e$']):
    box(ax, 7, 51 - i * 10, 24, 8, 'resultat', label=s, size='m')
    text(ax, 40, 55 - i * 10, 'vrai', 'resultat', 's')
box(ax, 52, 28, 34, 41, 'sujet')
text(ax, 69, 64, r'horloge $\mathbb{Z}/4$', 'sujet', 'm')
box(ax, 55, 45, 28, 9, 'limite', label=r'$1+1=2\neq0$', size='m')
text(ax, 69, 38, 'faux', 'limite', 's')
box(ax, 4, 6, 80, 15, 'fixe', label='un isomorphisme conserverait\nla propriété : impossible', size='m')
save(fig, '45-228')
