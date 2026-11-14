import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
d = 16
for cx, role, z in ((22, 'limite', 0), (66, 'resultat', 1)):
    box(ax, cx - 14, 20, 28, 28, role, fill=False, dash=True)
    for i in range(2):
        for j in range(2):
            disc(ax, cx - d / 2 + i * d, 27 + j * d, 3.0, role)
    text(ax, cx, 53, f'3e coordonnée : {z}', role, 's')
text(ax, 22 + 8 + 5, 24, r'$u_1$', 'sujet', 'm', ha='left')
text(ax, 22 - 8, 40, r'$u_2$', 'sujet', 'm', ha='right')
text(ax, 22, 14, 'plan de $u_1$, $u_2$ : 4 points', 'limite', 's')
text(ax, 66, 14, '4 restent', 'resultat', 's')
text(ax, 44, 4.5, r'$q^n-q^2=8-4=4$', 'resultat', 'l')
save(fig, '75-108')
