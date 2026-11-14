import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
k = 0.28
O = (6, 24)
u, v = (180, 0), (50, 86.6)
T = lambda p, q: (p[0] + k * q[0], p[1] + k * q[1])
U, S = T(O, u), T(O, (230, 86.6))
arrow(ax, O, U, 'sujet', lw=1.6)
arrow(ax, U, S, 'autre', lw=1.6)
arrow(ax, O, S, 'resultat', lw=1.0)
text(ax, 28, 29, r'avion $a$', 'sujet', 's')
text(ax, 62, 30, r'vent $v$', 'autre', 's', ha='left')
# est : deux additions de longueurs sur l'axe horizontal
line(ax, [S, (S[0], O[1])], 'fixe', lw=0.5, dash=True)
brace(ax, O[0], U[0], 20, 'sujet', '180', depth=1.6)
brace(ax, U[0], S[0], 20, 'autre', '50', depth=1.6)
text(ax, 36, 8, r'est : $180+50=230$', 'resultat', 's')
# nord : sur l'axe vertical
line(ax, [S, (S[0] + 6, S[1])], 'fixe', lw=0.5, dash=True)
line(ax, [(S[0] + 6, O[1]), (S[0] + 6, S[1])], 'autre', lw=1.6)
text(ax, 79, 36, '86,60', 'autre', 's', ha='center')
text(ax, 62, 66, r'nord : $0+86{,}60$', 'resultat', 's')
save(fig, '41-052')
