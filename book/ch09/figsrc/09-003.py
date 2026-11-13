import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for b, role, name, mi, n, eq in [(28, 'sujet', 'Vous', 50, 2, '50 ÷ 2 = 25'), (8, 'autre', 'Voisin', 100, 4, '100 ÷ 4 = 25')]:
    for g in range(n):
        box(ax, 20 + g * 16, b, 16, 8, role, label='25', size='s', r=0.4)
    text(ax, 2, b + 4, name, role, 'm', ha='left', weight='bold')
    text(ax, 20, b + 12, eq, role, 'm', ha='left')
text(ax, 52, 46, 'chaque case : 25 miles', 'resultat', 'm')
save(fig, '09-003')
