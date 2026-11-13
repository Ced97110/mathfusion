import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 5.2; oy = 26.0
def panel(ox, which):
    P = lambda x, y: (ox + x * u, oy + y * u)
    if which == 'N':
        line(ax, [P(0, 0), P(4, 2)], 'sujet', lw=1.2)
    for i in range(5):
        for j in range(3):
            on = (i, j) in ((0, 0), (2, 1), (4, 2))
            if which == 'S':
                if (i, j) == (2, 1): disc(ax, *P(i, j), 1.3, 'autre')
                else: disc(ax, *P(i, j), 0.5, 'fixe')
            elif which == 'N':
                if on: disc(ax, *P(i, j), 1.3, 'sujet')
                else: disc(ax, *P(i, j), 0.5, 'fixe')
            else:
                disc(ax, *P(i, j), 0.9, 'fixe')
    return P
P = panel(6, 'S')
disc(ax, *P(4, 2), 1.4, 'limite', fill=False)
panel(35, 'N'); panel(64, 'M')
text(ax, 17, 44, r'$S$', 'autre', 'l'); text(ax, 46, 44, r'$\langle S\rangle$', 'sujet', 'l'); text(ax, 75, 44, r'$M$', 'fixe', 'l')
text(ax, 17, 11, 'trop petite', 'autre', 's'); text(ax, 46, 11, 'le plus petit', 'sujet', 's'); text(ax, 75, 11, 'trop grand', 'fixe', 's')
text(ax, 17, 18, r'$(4\,;\,2)\notin S$', 'limite', 's')
text(ax, 31.5, oy + 5, r'$\subset$', 'encre', 'm'); text(ax, 60.5, oy + 5, r'$\subset$', 'encre', 'm')
save(fig, '57-137')
