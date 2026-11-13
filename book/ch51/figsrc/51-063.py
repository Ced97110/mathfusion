import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'addition seule : groupe commutatif', 'sujet', 'm')
rows = [('échanger', '1 + 2 = 2 + 1'), ('regrouper', '(1+2)+3 = 1+(2+3)'), ('ajouter 0', '3 + 0 = 3'), ('défaire', '3 + 1 = 0')]
for k, (a, b) in enumerate(rows):
    y = 58 - k * 13.5
    box(ax, 4, y, 26, 10, 'sujet', label=a, size='s')
    box(ax, 32, y, 52, 10, 'resultat', label=b, size='m')
box(ax, 4, 2, 80, 9, 'fixe', fill=False, dash=True, label='la multiplication est mise de côté', size='s')
text(ax, 44, 13.8, 'sur le cadran à 4 heures', 'fixe', 's') if False else None
save(fig, '51-063')
