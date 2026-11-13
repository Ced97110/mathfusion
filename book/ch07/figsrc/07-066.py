import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def stack(ax, xc, yc, top, bot, w, rb="varie", rt="sujet", rbot="sujet", d=4.6, size="m"):
    line(ax, [(xc - w / 2, yc), (xc + w / 2, yc)], rb, lw=1.6)
    text(ax, xc, yc + d, top, rt, size); text(ax, xc, yc - d, bot, rbot, size)

fig, ax = canvas(100)
xs, xn = 28, 66
ys = [86, 62, 38, 14]
stack(ax, xs, ys[0], r'$\frac{1}{2}$', r'$\frac{3}{4}$', 22, rt='sujet', rbot='sujet', d=7)
text(ax, xn, ys[0], 'la grande barre est un ÷', 'varie', 's')
text(ax, xs, ys[1], r'$\frac{1}{2} \div \frac{3}{4}$', 'sujet', 'l')
text(ax, xn, ys[1], 'on retourne 3/4', 'varie', 's')
text(ax, xs, ys[2], r'$\frac{1}{2} \times \frac{4}{3} = \frac{4}{6}$', 'varie', 'l')
text(ax, xn + 6, ys[2], 'on réduit', 'varie', 's')
text(ax, xs, ys[3], r'$\frac{2}{3}$', 'resultat', 'xl')
text(ax, xn, ys[3], 'plus petit que 1', 'resultat', 's')
for a, b, dy in [(0, 1, 11), (1, 2, 6), (2, 3, 7)]:
    arrow(ax, (xs, ys[a] - dy), (xs, ys[b] + 6), 'fixe')
save(fig, '07-066')
