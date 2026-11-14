import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ay, cx = 34, 44
text(ax, 44, 62, r'coefficient dominant $-6p$', 'encre', 'm')
arrow(ax, (8, ay), (82, ay), 'fixe')
text(ax, 85, ay, r'$p$', 'fixe', 'm')
line(ax, [(cx, ay - 17), (cx, ay + 17)], 'fixe', dash=True, lw=0.6)
line(ax, [(cx - 30, ay + 18), (cx + 30, ay - 18)], 'sujet', lw=1.4)
disc(ax, cx + 20, ay - 12, 1.8, 'resultat')
text(ax, cx + 12, 11, r'$p=1$ : $-6$, on divise', 'resultat', 's')
disc(ax, cx, ay, 1.8, 'limite')
arrow(ax, (cx + 8, ay + 8), (cx + 1.5, ay + 1.5), 'limite')
text(ax, cx + 18, ay + 14, r'$p=0$ : $0$' + '\n' + 'division impossible', 'limite', 's')
save(fig, '69-118')
