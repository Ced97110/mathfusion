import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 2, 62, 'Soustraire : de combien ?', 'encre', 'm', ha='left', weight='bold')
box(ax, 4, 46, 25, 7, 'sujet', label='50 miles', size='s')
box(ax, 4, 36, 50, 7, 'autre', label='100 miles', size='s')
box(ax, 29, 46, 25, 7, 'varie', dash=True)
text(ax, 58, 49.5, '50 de plus', 'varie', 's', ha='left')
text(ax, 2, 26, 'Diviser : combien par gallon ?', 'encre', 'm', ha='left', weight='bold')
for g in range(2):
    box(ax, 4 + g * 25, 10, 25, 8, 'resultat', label='25 miles', size='s')
    text(ax, 16.5 + g * 25, 5, '1 gallon', 'fixe', 's')
brace(ax, 4, 54, 21, 'sujet', down=False)
text(ax, 57, 14, '50 miles en tout', 'sujet', 's', ha='left')
save(fig, '09-004')
