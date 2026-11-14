import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 22, 70, r'$x^3-3x+1$', 'sujet', 'm')
text(ax, 66, 70, r'$x^3-3x+2$', 'autre', 'm')
text(ax, 22, 62, r'dernier terme : $9/4$', 'sujet', 's')
text(ax, 66, 62, r'dernier terme : $2x-2$', 'autre', 's')
# gauche : constante 9/4 = 2,25 (4 mm par unité)
ay = 38
line(ax, [(4, ay), (40, ay)], 'fixe', lw=0.8)
line(ax, [(4, ay + 2.25 * 4), (40, ay + 2.25 * 4)], 'sujet', lw=1.6)
# droite : 2x-2 sur x de -1 à 3 (9 mm par unité), 2 mm par unité en ordonnée
g = lambda v: 48 + (v + 1) * 9
line(ax, [(48, ay), (84, ay)], 'fixe', lw=0.8)
line(ax, [(g(-1), ay + 2 * (-4)), (g(3), ay + 2 * 4)], 'autre', lw=1.6)
disc(ax, g(1), ay, 1.6, 'autre')
text(ax, g(1) + 8, ay - 5, r'$x=1$', 'autre', 's')
text(ax, 22, 20, 'jamais nul :\npas de racine multiple', 'sujet', 's')
text(ax, 66, 20, 'nul en $x=1$ :\nracine multiple', 'autre', 's')
save(fig, '69-135')
