import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
rows = [('nombre seul à droite', 'x² + 6x = 16'), ('diviser par a', 'a = 1 : rien à faire'),
        ('ajouter 9 des deux côtés', 'x² + 6x + 9 = 25'), ('côté gauche en carré', '(x + 3)² = 25'),
        ('racine, avec ±', 'x = 2 ou x = −8')]
for i, (a, v) in enumerate(rows):
    y = 66 - i * 15
    box(ax, 3, y, 38, 9, 'fixe', label=a, size='s')
    box(ax, 46, y, 38, 9, 'resultat' if i == 4 else 'sujet', label=v, size='s')
    if i < 4: arrow(ax, (22, y - 0.5), (22, y - 5.5), 'varie')
save(fig, '23-047')
