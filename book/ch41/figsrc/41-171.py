import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# chaque ligne = un vecteur de dimension 4 ; case pleine = composante 1, case vide = composante 0
rows = [((1, 0, 0, 0), 'sujet', 58), ((0, 1, 0, 0), 'sujet', 48),
        ((0, 0, 1, 0), 'resultat', 30), ((0, 0, 0, 1), 'resultat', 20), ((0, 0, 1, 1), 'resultat', 10)]
for comp, role, y in rows:
    for j, c in enumerate(comp):
        if c:
            box(ax, 6 + j * 9, y, 8, 8, role, r=0.6)
        else:
            box(ax, 6 + j * 9, y, 8, 8, 'fixe', fill=False, r=0.6, lw=0.5)
    text(ax, 46, y + 4, '⟨' + ', '.join(str(c) for c in comp) + '⟩', role, 's', ha='left')
brace(ax, 6, 23, 70, 'fixe', label='cases 1 et 2', down=False)
brace(ax, 33, 50, 70, 'fixe', label='cases 3 et 4', down=False)
text(ax, 22, 43.5, 'les deux vecteurs donnés', 'sujet', 's')
text(ax, 22, 4, 'perpendiculaires aux deux', 'resultat', 's')
save(fig, '41-171')
