import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
x0, x1 = 20, 74
fx = lambda v: x0 + (v + 4) / 8 * (x1 - x0)
# top: ideal (2) in Z
text(ax, 44, 95, r'$(2)$ dans $\mathbb{Z}$ : un seul pas', 'sujet', 's')
line(ax, [(fx(-4) - 3, 82), (fx(4) + 3, 82)], 'fixe')
for v in range(-4, 5):
    if v % 2 == 0:
        disc(ax, fx(v), 82, 1.6, 'sujet')
    else:
        disc(ax, fx(v), 82, 0.9, 'fixe')
arrow(ax, (fx(0), 86), (fx(2), 86), 'varie', curve=-0.4)
text(ax, fx(1), 91, '2', 'varie', 's')
text(ax, fx(0), 76, '0', 'fixe', 's')
# bottom: ideal (2, x) in Z[x]
text(ax, 44, 66, r'$(2,\,x)$ dans $\mathbb{Z}[x]$ : deux pas', 'sujet', 's')
fy = lambda k: 22 + k * 11
for v in range(-4, 5):
    for k in range(4):
        if v % 2 == 0:
            disc(ax, fx(v), fy(k), 1.6, 'sujet')
        else:
            disc(ax, fx(v), fy(k), 0.9, 'fixe')
disc(ax, fx(1), fy(0), 2.2, 'limite')
text(ax, fx(1) + 4, fy(0) - 4, '1', 'limite', 's')
arrow(ax, (fx(0) + 1.5, fy(0) + 3.5), (fx(2) - 1.5, fy(0) + 3.5), 'varie')
text(ax, fx(1), fy(0) + 7.5, '2', 'varie', 's')
arrow(ax, (fx(-4) - 4, fy(0)), (fx(-4) - 4, fy(2.7)), 'varie')
text(ax, 8, fy(1.5), r'$x$', 'varie', 'm')
text(ax, 44, 8, 'terme constant', 'fixe', 's')
text(ax, 8, fy(3) + 6, 'coef. de $x$', 'fixe', 's', ha='left')
save(fig, '56-190')
