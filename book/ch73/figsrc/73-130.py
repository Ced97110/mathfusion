import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 6, 36, 22, 12, 'sujet', label='(3, 4)')
box(ax, 60, 36, 22, 12, 'sujet', label='(6, 2)')
arrow(ax, (29, 42), (59, 42), 'varie')
text(ax, 44, 47, r'$\times 2$ ; $\div 2$', 'varie', 's')
text(ax, 44, 37, 'la transformation', 'varie', 's')
text(ax, 17, 56, 'départ', 'sujet', 's'); text(ax, 71, 56, 'image', 'sujet', 's')
for x, s in [(17, r'$3 \times 4 = 12$'), (71, r'$6 \times 2 = 12$')]:
    arrow(ax, (x, 34), (x, 24), 'fixe')
    box(ax, x - 14, 10, 28, 12, 'resultat', label=s)
text(ax, 44, 16, '=', 'resultat', 'l')
text(ax, 44, 4, r'$Q$ est gardée', 'resultat', 's')
save(fig, '73-130')
