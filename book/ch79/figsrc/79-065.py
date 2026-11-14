import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx = 46
bot, top = (cx, 16), (cx, 62)
mids = [(cx - 22, 39), (cx, 39), (cx + 22, 39)]
import math
def cut(a, b, r=4.2):
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    return (a[0]+u[0]*r, a[1]+u[1]*r), (b[0]-u[0]*r, b[1]-u[1]*r)
for m in mids:
    line(ax, list(cut(bot, m)), 'sujet'); line(ax, list(cut(m, top)), 'sujet')
disc(ax, *bot, 4.2, 'fixe', label='0'); disc(ax, *top, 4.2, 'fixe', label='1')
for m, s in zip(mids, [r'$x$', r'$y$', r'$z$']):
    disc(ax, *m, 4.2, 'sujet', label=s)
text(ax, 4, 70, r'$M_3$', 'sujet', 'xl', ha='left')
text(ax, 4, 62, 'le diamant', 'sujet', 's', ha='left')
text(ax, cx + 7, 62, 'plus grand élément', 'fixe', 's', ha='left')
text(ax, cx + 7, 16, 'plus petit élément', 'fixe', 's', ha='left')
text(ax, cx, 5, r'$x, y, z$ : incomparables', 'sujet', 's')
save(fig, '79-065')
