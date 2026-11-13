import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
a = 32; o = 0.8391 * a
A = (4, 18); B = (4 + a, 18); C = (4 + a, 18 + o)
poly(ax, [A, B, C], 'fixe')
line(ax, [(B[0] - 3, B[1]), (B[0] - 3, B[1] + 3), (B[0], B[1] + 3)], 'fixe', lw=0.7)
th = [math.radians(i * 40 / 8) for i in range(9)]
line(ax, [(A[0] + 9 * math.cos(t), A[1] + 9 * math.sin(t)) for t in th], 'sujet', lw=1.2)
text(ax, 15, 21.5, '40°', 'sujet', 's')
text(ax, 20, 13, 'adjacent', 'fixe', 's')
text(ax, 39.5, 32, 'opposé', 'fixe', 's', rot=90)
for y, role, val, d in ((62, 'sujet', r'angle $A$ = 40°', "l'angle lui-même"), (38, 'autre', r'$\tan A$ = 0,8391', 'opposé ÷ adjacent'), (14, 'resultat', r'$1/\tan A$ ≈ 1,1918', 'adjacent ÷ opposé')):
    box(ax, 44, y, 42, 14, role); text(ax, 65, y + 9, val, role, 'm'); text(ax, 65, y + 3.8, d, role, 's')
arrow(ax, (50, 62), (50, 52), 'varie'); text(ax, 53, 57, 'tan', 'varie', 's', ha='left')
arrow(ax, (50, 38), (50, 28), 'varie'); text(ax, 53, 33, '1 ÷', 'varie', 's', ha='left')
arrow(ax, (82, 52), (82, 62), 'varie'); text(ax, 79, 57, 'arctan', 'varie', 's', ha='right')
save(fig, '25-082')
