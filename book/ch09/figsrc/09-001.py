import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for b, role, name, mi, ga in [(30, 'sujet', 'Vous', 50, 2), (6, 'autre', 'Voisin', 100, 4)]:
    box(ax, 22, b + 10, mi * 0.45, 7, role, label=f'{mi} miles', size='s')
    for g in range(ga):
        box(ax, 22 + g * 8.5, b, 7.5, 7, role, fill=False)
    text(ax, 22 + ga * 8.5 + 1, b + 3.5, f'{ga} gallons', role, 's', ha='left')
    text(ax, 2, b + 10, name, role, 'm', ha='left', weight='bold')
text(ax, 44, 48, 'deux nombres par voiture', 'encre', 'm')
save(fig, '09-001')
