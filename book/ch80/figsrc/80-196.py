import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
y1, y2 = 50, 24
xs = (6, 82)
for y, labs, role in ((y1, (r'$a$', r'$b$'), 'sujet'), (y2, (r'$a^{\prime}$', r'$b$'), 'autre')):
    line(ax, [(14, y), (24, y)]); line(ax, [(38, y), (46, y)]); line(ax, [(60, y), (74, y)])
    box(ax, 24, y - 5, 14, 10, role, label=labs[0], size='l')
    box(ax, 46, y - 5, 14, 10, role, label=labs[1], size='l')
line(ax, [(14, y1), (14, y2)]); line(ax, [(74, y1), (74, y2)])
line(ax, [(6, 37), (14, 37)]); line(ax, [(74, 37), (82, 37)])
disc(ax, 6, 37, 1.4); disc(ax, 82, 37, 1.4)
text(ax, 42, y1 + 10, r'série $(1,\ 1)$', 'sujet', 's')
text(ax, 42, y2 - 10, r'série $(0,\ 1)$', 'autre', 's')
text(ax, 44, 3.5, 'en parallèle : 2 positions', 'resultat', 'm')
save(fig, '80-196')
