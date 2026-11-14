import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
rows = [(56, 'sujet', r'$SL_2(\mathbb{R})$', 'une infinité de matrices'),
        (32, 'fixe', r'$\{I,\ -I\}$', '2 matrices'),
        (8, 'resultat', r'$\{1\}$', '1 matrice')]
for y, role, lab, cnt in rows:
    box(ax, 3, y, 34, 12, role, label=lab, size='l')
    text(ax, 43, y + 6, cnt, role, 's', ha='left')
for y in (56, 32):
    arrow(ax, (20, y), (20, y - 12), 'varie')
    text(ax, 23, y - 6, 'quotient', 'varie', 's', ha='left')
text(ax, 20, 3, 'fin : plus rien à retirer', 'fixe', 's')
save(fig, '73-146')
