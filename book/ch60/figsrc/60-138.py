import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
bx, bw, bh = 22, 64, 11
ys = [74, 55, 36, 17]
steps = [(r'$b$ est dans $\langle g\rangle$ et dans $K$', 'sujet', 'départ'),
         (r'dans $G/H$ : classe nulle, $b \in H$', 'sujet', ''),
         (r'revenir dans $G$ : $b \in \langle g\rangle \cap H$', 'varie', 'décisive'),
         (r'donc $b = 0$', 'resultat', 'arrivée')]
for y, (s, role, tag) in zip(ys, steps):
    box(ax, bx, y, bw, bh, role, label=s, size='s')
    if tag:
        text(ax, 11, y + bh / 2, tag, role, 's', weight='bold')
for y in ys[:-1]:
    arrow(ax, (bx + bw / 2, y - 0.4), (bx + bw / 2, y - 7.6), 'varie')
text(ax, 44, 8, 'grille : seul (0, 0) est commun', 'fixe', 's')
save(fig, '60-138')
