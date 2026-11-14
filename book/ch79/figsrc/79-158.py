import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 27, 87, 'la preuve', 'fixe', 's'); text(ax, 70, 87, 'avec les nombres', 'fixe', 's')
rows = [('fixe', r'départ : $H_2 \subseteq H_1$', r'$\{0, 4, 8\}$ ⊆ pairs'),
        ('autre', r'$h_2\in H_2$, $k\in H_1\cap H_3$', r'$4\in H_2$, $6\in H_1\cap H_3$'),
        ('varie', r'$h_2+k\in H_1$, car $H_2 \subseteq H_1$', r'4 + 6 = 10 : pair'),
        ('resultat', r'$H_2(H_1\cap H_3)\subseteq H_1\cap H_2H_3$', 'tous les pairs')]
for i, (r, a, b) in enumerate(rows):
    y = 70 - i * 19
    box(ax, 2, y, 52, 11, r, label=a, size='s', weight='bold' if i == 2 else 'normal')
    box(ax, 58, y, 28, 11, r, label=b, size='s')
    if i < 3:
        arrow(ax, (28, y), (28, y - 8), 'fixe'); arrow(ax, (72, y), (72, y - 8), 'fixe')
text(ax, 2, 5, r'$H_2H_3$ : les sommes $h_2+h_3$', 'fixe', 's', ha='left')
save(fig, '79-158')
