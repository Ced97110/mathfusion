import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
labels = [r'$\eta(4)$', r'$\eta(4\cdot 1)$', r'$\eta(4_L(1))$', r'$4_L(\eta(1))$', r'$4\cdot\eta(1)=4\cdot 3=12$']
roles = ['sujet', 'fixe', 'fixe', 'varie', 'resultat']
ys = [78 - i * 17.5 for i in range(5)]
for lab, role, y in zip(labels, roles, ys):
    box(ax, 3, y, 46, 8, role, label=lab)
steps = [r'écrire $4 = 4\cdot 1$', r'lire $4\cdot 1$ comme $4_L(1)$', r'échanger $\eta$ et $4_L$', r'$\eta(1)=3$, puis $4\cdot 3$']
for i in range(4):
    heavy = (i == 2)
    arrow(ax, (26, ys[i]), (26, ys[i + 1] + 8), 'varie' if heavy else 'fixe', lw=2.4 if heavy else 1.0)
    text(ax, 53, (ys[i] + ys[i + 1] + 8) / 2 + (1.6 if heavy else 0), steps[i], 'varie' if heavy else 'fixe', 's', ha='left', weight='bold' if heavy else 'normal')
text(ax, 53, (ys[2] + ys[3] + 8) / 2 - 2.2, "l'étape qui compte", 'varie', 's', ha='left')
save(fig, '57-121')
