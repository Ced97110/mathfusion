import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o, u = (22, 10), 5.5
cubes(ax, [(i, j, k) for i in range(2) for j in range(3) for k in range(4)], o, u)
p = iso(1, 0, 0, o, u); text(ax, p[0] + 4, p[1] - 3, '2', 'sujet', 'm')
p = iso(0, 1.5, 0, o, u); text(ax, p[0] - 4, p[1] - 2, '3', 'sujet', 'm')
p = iso(2, 0, 2, o, u); text(ax, p[0] + 4, p[1], '4', 'sujet', 'm')
text(ax, 44, 42, '(2 × 3) × 4 = 24', 'sujet', 'm', ha='left')
text(ax, 44, 34, '2 × (3 × 4) = 24', 'sujet', 'm', ha='left')
text(ax, 44, 24, '24 : reste 4 (mod 5)', 'resultat', 'm', ha='left')
save(fig, '44-155')
