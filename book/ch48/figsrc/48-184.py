import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
rows = [(74, lambda i: i == 0, 'resultat', '×3 : noyau {0}', 'rien perdu'),
        (46, lambda i: i % 4 == 0, 'varie', 'bouton : noyau 4ℤ', 'une partie perdue'),
        (18, lambda i: True, 'limite', 'tout sur 0 : noyau ℤ', 'tout perdu')]
for y, hit, role, cap, res in rows:
    text(ax, 4, y + 9, cap, role, 's', ha='left'); text(ax, 84, y + 9, res, role, 's', ha='right')
    for i in range(12):
        disc(ax, 8 + i * 6.9, y, 2.4, role if hit(i) else 'fixe', label=str(i) if i < 0 else None)
arrow(ax, (3, 86), (3, 4), 'fixe', lw=0.8)
save(fig, '48-184')
