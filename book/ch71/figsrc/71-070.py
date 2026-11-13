import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 4, 76, 26, -5, 3, 1, labels=False)
for v, r, s in [(-4, 'varie', r'$-4$'), (-1, 'sujet', r'$-1$'), (0, 'fixe', r'$0$')]:
    disc(ax, f(v), 26, 1.6, r)
    text(ax, f(v), 20, s, r, 'm')
arrow(ax, (f(-1) - 1, 30), (f(-4) + 1, 30), 'varie', curve=0.35)
text(ax, (f(-1) + f(-4)) / 2, 44, r'$\times(\det P)^2=\times 4$', 'varie', 's')
text(ax, f(-1) + 6, 36, r'$\det A=-1$', 'sujet', 's')
text(ax, f(-4) + 2, 36, r'nouveau : $-4$', 'varie', 's')
brace(ax, f(-5), f(0) - 1, 14, 'fixe', 'négatif : reste négatif', True, 's')
text(ax, f(2), 14, 'positif', 'fixe', 's')
save(fig, '71-070')
