import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u, x0 = 4.0, 30
def row(y, n, role, name):
    text(ax, 2, y + 3, name, role, 's', ha='left')
    box(ax, x0, y, n * u, 6, role, r=0.6)
    text(ax, x0 + n * u + 4, y + 3, str(n), role, 'm', weight='bold')
text(ax, 2, 60, 'nombre d’éléments : égaux', 'fixe', 'm', ha='left')
row(48, 12, 'sujet', 'horloge'); row(38, 12, 'autre', 'grille 2 × 6')
text(ax, 2, 28, 'additions pour revenir à 0\n(maximum) : différents', 'varie', 'm', ha='left')
row(12, 12, 'sujet', 'horloge'); row(2, 6, 'autre', 'grille 2 × 6')
save(fig, '60-012')
