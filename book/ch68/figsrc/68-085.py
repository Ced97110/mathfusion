import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u, cy, xa = 8, 33, 20
xb = xa + 3 * u
disc(ax, xa, cy, 2 * u, 'sujet', fill=False, lw=1.1)
disc(ax, xb, cy, 2 * u, 'autre', fill=False, lw=1.1)
disc(ax, xa, cy, 1.3, 'sujet')
disc(ax, xb, cy, 1.3, 'autre')
disc(ax, xa + 2 * u, cy, 1.3, 'limite')
text(ax, xa, cy - 4.5, '000', 'sujet', 's')
text(ax, xb, cy - 4.5, '111', 'autre', 's')
text(ax, xa + 2 * u, cy + 4.5, '110', 'limite', 's')
text(ax, xa, cy + 2 * u + 4, r'$B(000,\,2)$', 'sujet', 's')
text(ax, xb, cy + 2 * u + 4, r'$B(111,\,2)$', 'autre', 's')
text(ax, xa + 2 * u, 9, '110 est dans les deux', 'limite', 's')
text(ax, 75, cy, r'$2t=4$' + "\n" + r"n'est pas $<\,3$", 'limite', 's')
save(fig, '68-085')
