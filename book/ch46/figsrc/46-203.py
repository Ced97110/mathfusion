import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [9 + 11 * i for i in range(7)]
for i, x in enumerate(cx):
    even = i % 2 == 0
    box(ax, x - 4.5, 6, 9, 8, 'resultat' if even else 'fixe', label=str(i), size='m', dash=not even)
for dx, y, role, name in [(-2.5, 30, 'sujet', '(1 2 3)'), (2.5, 44, 'autre', 'identité')]:
    for n in (2, 4):
        x = cx[n] + dx
        disc(ax, x, y, 3, role)
        line(ax, [(x, y - 3), (x, 14.5)], role, lw=0.8, dash=True)
    text(ax, 71, y, name, role, 's')
text(ax, 44, 56, 'le nombre change, la parité reste', 'fixe', 's')
save(fig, '46-203')
