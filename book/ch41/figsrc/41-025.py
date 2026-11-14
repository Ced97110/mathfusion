import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-025 : valeur absolue (droite) et norme (plan) = la même idée : la longueur d'une flèche
fig, ax = canvas(92)
# --- haut : la droite, la flèche de 0 à -7 ---
f = numberline(ax, 8, 78, 74, -8, 2, labels=False, arrow_right=False)
text(ax, f(0), 69.5, '0', 'fixe', 's')
text(ax, f(-7), 69.5, '$-7$', 'fixe', 's')
arrow(ax, (f(0), 79), (f(-7), 79), 'autre', lw=1.4)
text(ax, (f(0) + f(-7)) / 2, 84, r'$|-7| = 7$', 'autre', 'l')
text(ax, 44, 89, 'sur une droite', 'fixe', 's')
line(ax, [(4, 62), (84, 62)], 'fixe', lw=0.5, dash=True)
# --- bas : le plan, la flèche 3 est / 4 nord ---
s = 7.0
O = (16, 10); P = (O[0] + 3 * s, O[1]); V = (O[0] + 3 * s, O[1] + 4 * s)
line(ax, [O, P], 'fixe', dash=True); line(ax, [P, V], 'fixe', dash=True)
arrow(ax, O, V, 'sujet', lw=1.4)
text(ax, (O[0] + P[0]) / 2, O[1] - 3.2, '3', 'fixe', 's')
text(ax, P[0] + 2.5, (P[1] + V[1]) / 2, '4', 'fixe', 's', ha='left')
text(ax, 20.5, 40.5, r'$\|v\|$ = 5', 'sujet', 'l')
text(ax, 62, 30, 'dans le plan', 'fixe', 's')
save(fig, '41-025')
