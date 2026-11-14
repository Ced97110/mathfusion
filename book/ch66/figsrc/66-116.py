import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
B = [(2, 2, 84, 70, 'fixe', 'réels ℝ'), (5, 5, 78, 42, 'varie', 'algébriques'),
     (8, 8, 72, 28, 'resultat', 'constructibles'), (11, 11, 66, 15, 'sujet', 'rationnels ℚ')]
for x, y, w, h, r, nom in B:
    box(ax, x, y, w, h, r, r=1.2)
    text(ax, x + 3, y + h - 3.5, nom, r, 's', ha='left', weight='bold')
disc(ax, 46, 64, 1.4, 'fixe'); text(ax, 49, 64, 'π ≈ 3,14159', 'fixe', 'm', ha='left')
disc(ax, 18, 64, 1.4, 'fixe'); text(ax, 21, 64, 'e ≈ 2,718', 'fixe', 'm', ha='left')
text(ax, 44, 57, 'aucun polynôme entier', 'limite', 's')
text(ax, 44, 52.5, 'ne les annule', 'limite', 's')
save(fig, '66-116')
