import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
items = [('sujet', 'départ', 'n impair : n = 2k + 1', '7 = 2 × 3 + 1'),
         ('varie', 'étape qui porte tout', 'n² = 4k² + 4k + 1', '= 2(2k² + 2k) + 1'),
         ('resultat', 'arrivée', 'n² est impair', '49 = 2 × 24 + 1')]
for i, (role, nom, f, ex) in enumerate(items):
    y = 62 - i * 30
    text(ax, 4, y + 23, nom, role, 's', ha='left', weight='bold')
    box(ax, 4, y, 80, 19, role, lw=1.6 if role == 'varie' else 0.8)
    text(ax, 44, y + 12.5, f, role, 'm'); text(ax, 44, y + 5.5, ex, role, 's')
    if i < 2: arrow(ax, (44, y), (44, y - 7), 'fixe')
save(fig, '42-084')
