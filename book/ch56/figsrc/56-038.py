import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 22, 95, 'avec les lettres', 'encre', 'm')
text(ax, 65, 95, 'avec 3 et −3', 'encre', 'm')
h, pitch, top = 11, 17, 87
L = [('1. b = a u', 'sujet'), ('2. a = b v', 'sujet'), ('3. b = b v u', 'varie'),
     ('4. b × 1 = b × v u', 'varie'), ('5. v u = 1 : u unité', 'resultat')]
R = ['−3 = 3 × (−1)', '3 = −3 × (−1)', '−3 = −3 × (−1) × (−1)', '−3 × 1 = −3 × (−1)(−1)', '(−1) × (−1) = 1']
ys = [top - h - pitch * i for i in range(5)]
for (lab, role), y, num in zip(L, ys, R):
    box(ax, 3, y, 38, h, role, label=lab, size='s')
    box(ax, 46, y, 39, h, role, label=num, size='s')
for i in range(4):
    arrow(ax, (22, ys[i] - 0.5), (22, ys[i + 1] + h + 0.5), 'fixe')
text(ax, 25, ys[1] - 3, 'on remplace a par b v', 'fixe', 's', ha='left')
text(ax, 25, ys[3] - 3, 'on barre b (non nul)', 'varie', 's', ha='left')
save(fig, '56-038')
