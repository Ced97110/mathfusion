import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for i, (s, e, r) in enumerate([('sous-estimation', r'$E < 0$', 'sujet'), ('exacte', r'$E = 0$', 'fixe'), ('surestimation', r'$E > 0$', 'fixe')]):
    x = 3 + i * 28.5
    box(ax, x, 52, 27, 15, r); text(ax, x + 13.5, 62, s, r, 's'); text(ax, x + 13.5, 56, e, r, 'm')
f = numberline(ax, 10, 76, 26, 1700, 2000, 50, labels=False, arrow_right=False)
disc(ax, f(1976), 26, 1.5, 'fixe'); disc(ax, f(1750), 26, 1.5, 'sujet')
arrow(ax, (f(1976) - 1, 28), (f(1750) + 1, 28), 'sujet', curve=0.25); text(ax, 45, 42, r'$E = 1\,750 - 1\,976 = -226$', 'sujet', 's')
text(ax, f(1750) + 3, 17, r'$\tilde{V}$ = 1 750', 'sujet', 's'); text(ax, f(1976) - 2, 17, r'$V$ = 1 976', 'fixe', 's')
save(fig, '10-031')
