import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 24, 57, 'heures : 0 à 3', 'fixe', 's')
for i in range(4):
    box(ax, 4 + 12 * i, 44, 10, 8, 'fixe', label=str(i))
box(ax, 58, 44, 10, 8, 'limite', fill=False, label='5', dash=True)
text(ax, 63, 40, 'hors cadran', 'limite', 's')
for i in range(5):
    box(ax, 4 + 13 * i, 22, 10, 9, 'sujet', label='2', size='l')
brace(ax, 4, 66, 22, 'varie', label=r'$n=5$ termes')
text(ax, 77, 26.5, r'$=10=2$', 'resultat', 'l')
save(fig, '51-130')
