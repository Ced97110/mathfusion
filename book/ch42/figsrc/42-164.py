import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
x0 = [24 + 18 * i for i in range(3)]
for x, n in zip(x0, '123'):
    box(ax, x, 26, 14, 24, 'sujet')
    text(ax, x + 7, 54, n, 'sujet', 'm')
    for y in (32, 44): disc(ax, x + 7, y, 2.6, 'sujet')
text(ax, 15, 32, 'a', 'autre', 'm'); text(ax, 15, 44, r'$b$', 'autre', 'm')
brace(ax, x0[0], x0[2] + 14, 58, 'sujet', r'$m=3$ choix de $s$', down=False)
brace(ax, x0[0], x0[0] + 14, 24, 'autre', r'$n=2$ choix de $t$')
text(ax, 64, 10, r'$3\times2=6$ couples', 'resultat', 'm', weight='bold')
save(fig, '42-164')
