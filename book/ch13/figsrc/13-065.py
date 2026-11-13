import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 24
f = numberline(ax, 6, 78, y, -6, 6, labels=False)
for v, r in ((-5, 'sujet'), (0, 'fixe'), (5, 'fixe')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(5), y, 2, 'fixe')
disc(ax, f(-5), y, 2, 'sujet')
text(ax, f(5), y + 6, r'$b$', 'fixe', 'l')
text(ax, f(-5), y + 6, r'$-b$', 'sujet', 'l')
arrow(ax, (f(5) - 1, y + 9), (f(-5) + 1, y + 9), 'varie', curve=0.35)
text(ax, f(0), y + 20, 'de l’autre côté de 0', 'varie', 's')
brace(ax, f(0), f(5), y - 7, 'fixe', '5 pas')
brace(ax, f(-5), f(0), y - 7, 'sujet', '5 pas')
text(ax, 44, 3, r'$-b$ : l’opposé de $b$'.replace('\\u2019', '’'), 'sujet', 'm')
save(fig, '13-065')
