import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ay, uy = 18, 7
f = numberline(ax, 8, 64, ay, 0, 4, arrow_right=True)
line(ax, [(8, ay), (8, ay + 30)], 'fixe', lw=0.5)
line(ax, [(f(x), ay + (x - 2) ** 2 * uy) for x in [i / 20 for i in range(0, 81)]], 'sujet', lw=1.5)
line(ax, [(f(1.2), ay), (f(2.8), ay)], 'varie', lw=2.4)
disc(ax, f(2), ay, 1.4, 'resultat')
text(ax, 20, 52, r'$y=f(x)$', 'sujet', 'm')
text(ax, f(2), ay + 16, r'touche l’axe : $f(r)=0$', 'resultat', 's')
text(ax, f(2), ay + 9, r'à plat : $f′(r)=0$', 'varie', 's')
text(ax, f(2), 8, 'tangente horizontale', 'varie', 's')
save(fig, '70-057')
