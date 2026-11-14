import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# le signe découpé : chevron, liste de vecteurs, chevron
box(ax, 4, 44, 12, 14, 'fixe', label=r'$\langle$', size='xl')
box(ax, 20, 44, 48, 14, 'sujet', label=r'$v_1,\ \ldots,\ v_n$', size='l')
box(ax, 72, 44, 12, 14, 'fixe', label=r'$\rangle$', size='xl')
text(ax, 10, 63, 'chevrons', 'fixe', 's')
text(ax, 44, 63, 'liste de vecteurs de départ', 'sujet', 's')
text(ax, 78, 63, 'chevrons', 'fixe', 's')
text(ax, 44, 37, 'écriture abrégée :', 'fixe', 's')
box(ax, 30, 24, 28, 10, 'sujet', label=r'$\langle v_i\rangle$', size='l')
arrow(ax, (44, 22.5), (44, 15), 'resultat')
box(ax, 4, 3, 80, 10, 'resultat', label='ensemble de toutes les combinaisons')
save(fig, '58-139')
