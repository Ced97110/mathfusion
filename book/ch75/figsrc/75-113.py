import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(46, 1, 7), (34, 2, 6), (22, 4, 4)]
for i, (y, out, ok) in enumerate(rows):
    text(ax, 2, y, f'colonne {i+1}', 'encre', 's', ha='left')
    for k in range(8):
        disc(ax, 28 + k * 6.2, y, 2.2, 'fixe' if k < out else 'sujet')
    text(ax, 86, y, f'{ok} choix', 'sujet', 's', ha='right')
text(ax, 44, 57, '8 vecteurs, on en retire 1, 2, 4', 'encre', 's')
box(ax, 8, 4, 72, 9, 'resultat', label=r'$7\times 6\times 4=168$', size='l')
text(ax, 6, 15.5, '', 'encre', 's')
arrow(ax, (44, 18), (44, 14), 'varie')
save(fig, '75-113')
