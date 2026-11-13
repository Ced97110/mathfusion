import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'$a \equiv b (\mathrm{mod}\ n)$ : $n$ divise $a - b$', 'encre', 'm')
text(ax, 44, 62, r'$7 \equiv 2 (\mathrm{mod}\ 5)$', 'sujet', 'm')
f = numberline(ax, 8, 78, 46, 0, 10, labels=False, arrow_right=False)
for v, lab in ((2, 'b = 2'), (7, 'a = 7')):
    disc(ax, f(v), 46, 1.8, 'sujet'); text(ax, f(v), 40, lab, 'sujet', 's')
arrow(ax, (f(2), 48.5), (f(7), 48.5), 'varie', curve=-0.4); text(ax, f(4.5), 57, 'un pas de 5', 'varie', 's')
text(ax, 44, 30, r'$26 \equiv 2 (\mathrm{mod}\ 12)$', 'autre', 'm')
g = numberline(ax, 8, 78, 14, 2, 26, step=12, labels=False, arrow_right=False)
for v, lab in ((2, 'b = 2'), (26, 'a = 26')):
    disc(ax, g(v), 14, 1.8, 'autre'); text(ax, g(v), 8, lab, 'autre', 's')
arrow(ax, (g(2), 16.5), (g(14), 16.5), 'varie', curve=-0.5); arrow(ax, (g(14), 16.5), (g(26), 16.5), 'varie', curve=-0.5)
text(ax, g(8), 24, '12', 'varie', 's'); text(ax, g(20), 24, '12', 'varie', 's')
save(fig, '44-143')
