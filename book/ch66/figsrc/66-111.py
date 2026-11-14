import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# boîtes emboîtées : (x, y, w, h, rôle, nom, nombre)
B = [(2, 2, 84, 74, 'fixe', 'réels ℝ', 'π'),
     (5, 5, 78, 56, 'varie', 'algébriques', '∛2'),
     (8, 8, 72, 38, 'resultat', 'constructibles', '√2'),
     (11, 11, 66, 20, 'sujet', 'rationnels ℚ', '1/2')]
for x, y, w, h, r, nom, nb in B:
    box(ax, x, y, w, h, r, r=1.2)
    text(ax, x + 3, y + h - 3.8, nom, r, 's', ha='left', weight='bold')
for (x, y, w, h, r, nom, nb), yy in zip(B, [68.5, 53.5, 38.5, 20.5]):
    disc(ax, 66, yy, 1.2, r)
    text(ax, 70, yy, nb, r, 'm', ha='left')
save(fig, '66-111')
