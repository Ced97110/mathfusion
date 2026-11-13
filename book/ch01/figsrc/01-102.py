import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 6, 78, 14, 0, 12, step=1, labels=False)
for v in (0, 7, 10):
    text(ax, f(v), 10, str(v), 'fixe', 's')
arrow(ax, (f(0), 26), (f(7), 26), 'autre'); text(ax, 27, 29, '7 pas', 'autre', 's')
disc(ax, f(7), 14, 1, 'autre')
arrow(ax, (f(0), 34), (f(10), 34), 'sujet'); text(ax, 36, 37, '10 pas', 'sujet', 's')
disc(ax, f(10), 14, 1, 'sujet')
for a, b in [(48, 54), (54, 60), (60, 66)]:
    arrow(ax, (a, 15.5), (b, 15.5), 'varie', curve=-0.5)
text(ax, 57, 21.5, '3 pas de plus', 'varie', 's')
arrow(ax, (10, 41), (78, 41), 'resultat'); text(ax, 44, 45, 'plus grand = plus à droite', 'resultat', 's')
save(fig, '01-102')
