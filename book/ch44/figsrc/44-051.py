import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'premier exemple de monoïde', 'encre', 'm', weight='bold')
box(ax, 4, 24, 80, 36, 'sujet', fill=False, dash=True)
text(ax, 44, 55, r'$M(S)$ : 4 transformations', 'sujet', 'm')
roles = ['fixe', 'sujet', 'sujet', 'resultat']
labs = [r'$1_S$', 'α', 'β', 'γ']
for k in range(4):
    box(ax, 6.5 + 20*k, 30, 15, 12, roles[k], label=labs[k], size='l')
text(ax, 17, 46.5, 'ne change rien', 'fixe', 's')
text(ax, 26, 12, r'α ∘ β = γ', 'encre', 'm')
arrow(ax, (40, 12), (74, 29.5), 'varie', curve=0.2)
text(ax, 66, 12, r'reste dans $M(S)$', 'resultat', 's')
save(fig, '44-051')
