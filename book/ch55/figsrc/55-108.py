import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 24
f = numberline(ax, 8, 68, y, 0, 4, step=1)
line(ax, [(f(2.5), y - 6), (f(2.5), 52)], 'varie', lw=1.2, dash=True)
text(ax, f(2.5), 56, r'axe en $2{,}5$', 'varie', 'm')
for r in (2, 3):
    disc(ax, f(r), y, 2.0, 'sujet')
    text(ax, f(r), y + 6, rf'$r_{r - 1}={r}$', 'sujet', 's')
brace(ax, f(2), f(2.5), 38, 'fixe', label='0,5', down=False)
brace(ax, f(2.5), f(3), 38, 'fixe', label='0,5', down=False)
text(ax, 44, 5, r'$(2+3)/2=2{,}5$ : demi-somme', 'varie', 'm')
save(fig, '55-108')
