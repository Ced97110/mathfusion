import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 6, 62, 16, 14, 'sujet', label='0', size='l')
text(ax, 44, 69, r'$\mapsto$', 'varie', 'xl')
text(ax, 44, 78, 'est envoyé sur', 'varie', 's')
box(ax, 66, 62, 16, 14, 'resultat', label='1', size='l')
text(ax, 14, 57, 'départ', 'sujet', 's'); text(ax, 74, 57, 'image', 'resultat', 's')
line(ax, [(4, 50), (84, 50)], 'fixe')
text(ax, 22, 42, 'ligne de 1 :', 'fixe', 's')
for i in range(4):
    text(ax, 60, 42 - i * 9, rf'${i}\mapsto{(i + 1) % 4}$', 'encre', 'm')
text(ax, 22, 33, 'une ligne par', 'fixe', 's'); text(ax, 22, 28, 'élément', 'fixe', 's')
save(fig, '45-221')
