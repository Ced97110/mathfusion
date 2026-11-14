import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def pts(y, labs=True):
    f = numberline(ax, 8, 70, y, 0, 7, every=2, arrow_right=True)
    return f
f = pts(60)
text(ax, 84, 66, r'$d$', 'fixe', 's')
text(ax, 22, 72, r'$3 + 2d = 15$', 'autre', 'm')
disc(ax, f(6), 60, 1.8, 'autre')
for v in (1, 4):
    disc(ax, f(v), 60, 1.8, 'limite', fill=False)
text(ax, f(2.5), 66, 'refusés à tort', 'limite', 's')
g = pts(25)
text(ax, 25, 37, r'$3 + 2d \leq 15$', 'sujet', 'm')
line(ax, [(g(0), 25), (g(6), 25)], 'resultat', lw=2.4)
for v in (0, 1, 4, 6):
    disc(ax, g(v), 25, 1.8, 'resultat')
text(ax, f(3), 31, 'tous acceptés', 'resultat', 's')
save(fig, '17-003')
