import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 14; f = numberline(ax, 6, 76, y, 46, 54, 1, every=4, arrow_right=False)
for i in range(4):
    a, b = 46 + i, 47 + i
    arrow(ax, (f(a), y + 1.5), (f(b), y + 1.5), 'varie', curve=-0.6)
    text(ax, (f(a) + f(b)) / 2, y + 7.5, str(i + 1), 'varie', 's')
brace(ax, f(46), f(50), y + 11, 'varie', '4 pas', down=False)
brace(ax, f(51), f(52), y - 7, 'sujet', '1 pas = 1', down=True)
save(fig, '10-010')
