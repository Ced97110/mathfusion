import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
f1 = numberline(ax, 10, 78, 46, 49, 64, labels=False, arrow_right=False)
f2 = numberline(ax, 10, 78, 16, 7, 8, labels=False, arrow_right=False)
text(ax, 44, 62, 'les carrés', 'fixe', 's'); text(ax, 44, 30, 'les racines', 'fixe', 's') if False else None
text(ax, f1(49), 40, r'$49=7^2$', 'sujet', 's'); text(ax, f1(64), 40, r'$64=8^2$', 'sujet', 's')
disc(ax, f1(50), 46, 1.4, 'varie'); text(ax, f1(50) + 4, 51, '50', 'varie', 's')
disc(ax, f2(50 ** .5), 16, 1.4, 'varie'); text(ax, f2(50 ** .5) + 3, 21, r'$\sqrt{50}$', 'varie', 's', ha='left')
for a, b, r in ((f1(49), f2(7), 'sujet'), (f1(64), f2(8), 'sujet'), (f1(50), f2(50 ** .5), 'varie')):
    arrow(ax, (a, 37 if r == 'sujet' else 44), (b, 22 if r == 'sujet' else 18), r, lw=0.7)
text(ax, f2(7), 10, '7', 'sujet', 's'); text(ax, f2(8), 10, '8', 'sujet', 's')
save(fig, '10-098')
