import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
y = 20
f = numberline(ax, 4, 70, y, 0, 13, step=1, labels=True, every=5, arrow_right=False)
line(ax, [(70, y), (76, y)], 'fixe', dash=True)
line(ax, [(76, y), (86, y)], 'fixe')
line(ax, [(80, y - 1.2), (80, y + 1.2)], 'fixe', lw=0.8)
text(ax, 80, y - 3.4, '40', 'fixe', 's')
text(ax, f(7), 16, '7', 'fixe', 's')
text(ax, f(12), 16, '12', 'fixe', 's')
for v in (5, 7, 12):
    disc(ax, f(v), y, 1.2, 'sujet')
disc(ax, 80, y, 1.2, 'sujet')
for i in range(5):
    arrow(ax, (f(i), 21), (f(i + 1), 21), 'varie', curve=-0.5)
text(ax, 8, 10, 'départ', 'varie', 's')
brace(ax, f(0), f(5), 26, 'fixe', label='5 pas', down=False)
disc(ax, f(5), y, 2.4, 'resultat', fill=False)
text(ax, f(5), 35, 'première rencontrée : 5', 'resultat', 'm')
save(fig, '01-152')
