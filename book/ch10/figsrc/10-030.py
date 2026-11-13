import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'surestimation : $E > 0$', 'sujet', 'l')
f = numberline(ax, 8, 80, 28, 3300, 3550, 50, labels=False, arrow_right=False)
disc(ax, f(3358), 28, 1.5, 'sujet'); disc(ax, f(3500), 28, 1.5, 'varie')
brace(ax, f(3358), f(3500), 32, 'varie', r'$E = +142$', down=False)
text(ax, f(3358) + 2, 19, r'$V$ = 3 358', 'sujet', 's'); text(ax, f(3500) - 2, 19, r'$\tilde{V}$ = 3 500', 'varie', 's')
text(ax, 44, 8, r'$\tilde{V}$ est plus grand que $V$', 'varie', 's')
save(fig, '10-030')
