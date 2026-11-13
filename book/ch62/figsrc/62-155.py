import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# à gauche : un isomorphisme de E dans E qui laisse F en place ; à droite : l'ensemble de ces 6 isomorphismes
box(ax, 2, 14, 42, 42, 'sujet')
text(ax, 9, 51, 'E', 'sujet', 'l', weight='bold')
box(ax, 10, 20, 26, 16, 'fixe', label='F\nreste fixe', size='s')
arrow(ax, (10, 57), (36, 57), 'varie', lw=1.2, curve=-0.7)
text(ax, 23, 72, 'un isomorphisme', 'varie', 's')
text(ax, 23, 68.5, 'de E dans E', 'varie', 's')
text(ax, 68, 72, 'groupe de Galois', 'resultat', 'm', weight='bold')
text(ax, 68, 66.5, '6 isomorphismes', 'resultat', 's')
box(ax, 50, 14, 36, 46, 'resultat')
k = 0
for row in range(2):
    for col in range(3):
        k += 1
        disc(ax, 58 + 10 * col, 46 - 14 * row, 4.2, 'resultat', label=rf'$\sigma_{k}$', size='s')
assert k == 6
text(ax, 68, 26, 'en composer deux', 'resultat', 's')
text(ax, 68, 22, 'en donne un autre', 'resultat', 's')
save(fig, '62-155')
