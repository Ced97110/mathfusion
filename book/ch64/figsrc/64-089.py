import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(r'$F_1=\mathbb{Q}$', 'sujet'), (r'$d_1=\sqrt{5}$', 'varie'),
        (r'$d_1^{\,2}=5\in F_1$', 'resultat'), (r'$F_2=\mathbb{Q}(\sqrt{5})$', 'sujet')]
ys = [60 - 15 * i for i in range(4)]
tags = ['départ', 'on ajoute', 'on vérifie', 'étage suivant']
for (lab, role), y, tg in zip(rows, ys, tags):
    box(ax, 28, y, 58, 9, role, label=lab)
    text(ax, 2, y + 4.5, tg, role, 's', ha='left', weight='bold')
for i in range(3):
    arrow(ax, (57, ys[i]), (57, ys[i + 1] + 9), 'fixe')
text(ax, 57, 4, r'contient $(3\pm\sqrt{5})/2$', 'resultat', 's')
save(fig, '64-089')
