import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert math.gcd(4, 26) == 2 and 26 // 2 == 13 and 4 * 13 == 52 == 2 * 26

fig, ax = canvas(76)
ys = [56, 32, 8]
box(ax, 4, ys[0], 80, 14, 'sujet', label=r'départ' + '\n' + r'$a = 4$, PGCD$(4, 26) = 2 = d$')
box(ax, 4, ys[1], 80, 14, 'varie', lw=1.8, label=r'étape décisive' + '\n' + r'$4 \times 13 = 52 = 2 \times 26$')
box(ax, 4, ys[2], 80, 14, 'limite', label=r'arrivée' + '\n' + r'lettres 0 et 13 : même image')
for i, n in enumerate([r'$26 \div d = 13$', r'multiple de 26 : vaut 0']):
    arrow(ax, (14, ys[i]), (14, ys[i + 1] + 14), 'fixe')
    text(ax, 19, ys[i] - 5, n, 'fixe', 's', ha='left')
save(fig, '53-055')
