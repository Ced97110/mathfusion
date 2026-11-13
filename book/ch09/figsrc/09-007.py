import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [('6 sur 8', 75, 'sujet'), ('14 sur 20', 70, 'autre'), ('31 sur 40', 77.5, 'resultat')]
for i, (n, p, role) in enumerate(rows):
    b = 40 - i * 13
    box(ax, 22, b, 60, 8, role, fill=False, r=0.4)
    box(ax, 22, b, p * 0.6, 8, role, label=f'{p:g}'.replace('.', ','), size='s', r=0.4)
    text(ax, 2, b + 4, n, role, 'm', ha='left')
text(ax, 22, 8, '0', 'fixe', 's'); text(ax, 82, 8, '100', 'fixe', 's')
text(ax, 44, 52, 'tout ramené à un total de 100', 'encre', 'm')
text(ax, 44, 3, 'le plus grand : 77,5', 'resultat', 'm')
save(fig, '09-007')
