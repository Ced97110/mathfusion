import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y = 26
f = numberline(ax, 6, 78, y, -3.5, 3.5, labels=False)
for v, r in ((-2, 'resultat'), (0, 'fixe'), (2, 'sujet')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(2), y, 1.8, 'sujet')
disc(ax, f(-2), y, 1.8, 'resultat')
arrow(ax, (f(2) - 1, y + 3), (f(-2) + 1, y + 3), 'varie', curve=0.4)
text(ax, f(0), y + 15, r'$\times(-1)$', 'varie', 'm')
brace(ax, f(0), f(2), y - 7, 'sujet', '2 pas')
brace(ax, f(-2), f(0), y - 7, 'resultat', '2 pas')
text(ax, 44, 57, r'$(-1)\times a=-a$', 'encre', 'l')
text(ax, 44, 4, r'$2+2\times(-1)=0$', 'varie', 's')
save(fig, '13-076')
