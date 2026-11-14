import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 76, 22, 0, 420, step=30, every=4, arrow_right=False)
brace(ax, f(0), f(360), 28, 'fixe', label='un tour : 360°', down=False)
brace(ax, f(360), f(390), 28, 'varie', label='+ 30°', down=False)
disc(ax, f(390), 22, 1.8, 'resultat')
line(ax, [(f(390), 24), (f(390) + 3, 40)], 'resultat')
text(ax, 82, 43, r'390° : $t=13$', 'resultat', 'm', ha='right')
save(fig, '32-012')
