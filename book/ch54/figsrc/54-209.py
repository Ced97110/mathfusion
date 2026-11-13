import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'valeurs de $p$ modulo 3', 'sujet', 'm')
u = 9.0           # mm per unit of height
y0 = 22
line(ax, [(8, y0), (84, y0)], 'fixe', lw=1.6)
text(ax, 8, y0 - 4, 'niveau 0 = racine', 'fixe', 's', ha='left')
for i, v in enumerate((2, 1, 2)):
    x = 16 + i * 25
    box(ax, x, y0, 14, v * u, 'sujet', label=str(v), size='l')
    text(ax, x + 7, y0 - 9, f'a = {i}', 'encre', 'm')
text(ax, 44, 4, 'aucune barre à 0 : pas de racine', 'resultat', 'm', weight='bold')
save(fig, '54-209')
