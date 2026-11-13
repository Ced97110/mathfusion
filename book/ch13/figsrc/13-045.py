import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, r, lab, top in [(3, 'fixe', r'$8\geq 0$ : vrai', 'comparer'), (32, 'sujet', r'$|a|=a$', 'lire la ligne'), (61, 'resultat', r'$|8|=8$', 'remplacer')]:
    box(ax, x, 38, 24, 12, r, label=lab, size='m'); text(ax, x + 12, 54, top, 'varie', 's')
arrow(ax, (27, 44), (32, 44), 'varie'); arrow(ax, (56, 44), (61, 44), 'varie')
f = numberline(ax, 10, 70, 18, 0, 8, labels=False, arrow_right=False)
line(ax, [(f(0), 18), (f(8), 18)], 'resultat', lw=2.4)
disc(ax, f(0), 18, 1.8, 'fixe'); disc(ax, f(8), 18, 1.8, 'sujet')
text(ax, f(0), 13, '0', 'fixe'); text(ax, f(8), 13, '8', 'sujet')
text(ax, (f(0) + f(8)) / 2, 23, 'on recopie le nombre', 'resultat', 's')
text(ax, 44, 4, r'même chose pour 0 : $|0|=0$', 'resultat', 's')
save(fig, '13-045')
