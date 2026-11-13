import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 20, 55, 'horloge à 4 heures', 'sujet', 's')
text(ax, 64, 55, 'couples (ℤ/2ℤ × ℤ/2ℤ)', 'autre', 's')
box(ax, 4, 30, 32, 9, 'varie', label='{0, 2}')
for i, s in enumerate(['{(0,0), (0,1)}', '{(0,0), (1,0)}', '{(0,0), (1,1)}']):
    box(ax, 44, 42 - 12 * i, 40, 9, 'varie', label=s, size='s')
text(ax, 20, 20, '1', 'sujet', 'xl', weight='bold')
text(ax, 64, 8, '3', 'autre', 'xl', weight='bold')
text(ax, 20, 11, 'sous-groupe propre', 'fixe', 's')
text(ax, 20, 5.5, 'non trivial', 'fixe', 's')
text(ax, 42, 31, '≠', 'limite', 'xl', weight='bold')
save(fig, '46-258')
