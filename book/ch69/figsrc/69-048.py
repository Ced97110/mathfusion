import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 56, r'$(F,\,P)$', 'sujet', 18)
f = numberline(ax, 8, 70, 28, -5, 5, every=5)
line(ax, [(f(0), 28), (f(5) + 5, 28)], 'sujet', lw=3.0)
brace(ax, f(0), f(5) + 5, 32, 'sujet', label=r'$P$ : à droite de 0', down=False)
brace(ax, f(-5), f(5) + 5, 22, 'fixe', label=r'$F=\mathbb{R}$', down=True)
save(fig, '69-048')
