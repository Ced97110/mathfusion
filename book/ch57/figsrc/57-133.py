import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
yt, yb = 44.0, 14.0
f = numberline(ax, 8, 70, yt, -12, 18, 6)
for v in range(-12, 19, 6):
    disc(ax, f(v), yt, 1.4, 'sujet')
arrow(ax, (f(12) + 1, yt + 2), (f(18) - 1, yt + 2), 'varie', curve=-0.5)
text(ax, f(15), yt + 8, r'$+\,6$', 'varie', 's')
arrow(ax, (f(6) - 1, yt + 2), (f(-12) + 1, yt + 2), 'varie', curve=0.4)
text(ax, f(-3), yt + 12, r'$\times(-2)$', 'varie', 's')
text(ax, 2, 62, 'multiples de 6 : idéal', 'sujet', 'm', ha='left')
g = numberline(ax, 8, 62, yb, 0, 10, 1, labels=False)
for v in (3, 5):
    disc(ax, g(v), yb, 1.4, 'sujet')
disc(ax, g(8), yb, 1.4, 'limite', fill=False)
text(ax, g(3), yb - 5, '3', 'sujet', 's'); text(ax, g(5), yb - 5, '5', 'sujet', 's')
text(ax, g(8), yb - 5, r'$8\notin$', 'limite', 's')
arrow(ax, (g(3) + 1, yb + 2), (g(8) - 1, yb + 2), 'varie', curve=-0.5)
text(ax, g(5.5), yb + 12.5, r'$+\,5$', 'varie', 's')
text(ax, 2, 34, 'les impairs : pas stables par +', 'limite', 's', ha='left')
save(fig, '57-133')
