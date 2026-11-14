import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 17, 73, r"anneau $\mathbb{Z}$", 'sujet', 'm')
text(ax, 66, 73, r"règles sur $\mathbb{Z}$", 'varie', 'm')
left = ['3', '5', '3 + 5 = 8', '3 × 5 = 15']
right = ['× 3', '× 5', '× 3  plus  × 5  =  × 8', '× 3  puis  × 5  =  × 15']
for i, (a, b) in enumerate(zip(left, right)):
    y = 55 - i * 15
    box(ax, 2, y, 30, 10, 'sujet', label=a, size='s')
    role = 'varie' if i < 2 else 'resultat'
    box(ax, 40, y, 46, 10, role, label=b, size='s')
    arrow(ax, (32.5, y + 5), (39.5, y + 5), 'varie')
text(ax, 44, 4, 'somme ↦ somme, produit ↦ composée', 'resultat', 's')
save(fig, '57-059')
