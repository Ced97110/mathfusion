import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
lv = [44, 33, 22, 11]
xs = [38, 54, 70]
pts = [(20, lv[0])]
for k, x in enumerate(xs):
    pts += [(x, lv[k]), (x, lv[k + 1])]
pts.append((84, lv[3]))
line(ax, pts, 'varie', lw=1.5)
for k, x in enumerate(xs):
    disc(ax, x, (lv[k] + lv[k + 1]) / 2 + 0.0, 3.0, 'sujet', label=str(k + 1), size='s')
text(ax, 20, 49, r'$V(-2)=3$', 'varie', 'm')
text(ax, 76, 6.5, r'$V(2)=0$', 'varie', 'm')
arrow(ax, (6, lv[0]), (6, lv[3]), 'encre', lw=1.0)
text(ax, 17, 27.5, r'$3-0=3$', 'encre', 'm')
text(ax, 50, 3, 'chaque marche : une racine', 'sujet', 's')
save(fig, '69-102')
