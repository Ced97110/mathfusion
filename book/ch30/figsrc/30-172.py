import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
X = lambda x: 8 + (x + 1.7) * 11
yc, sy = 44, 10
box(ax, 8, yc - sy, 74, 2 * sy, 'limite', dash=True)
line(ax, [(8, yc), (82, yc)], 'fixe', lw=0.6)
def br(c, sign):
    pts = []
    for i in range(-100, 101):
        x = c + 1.2 * i / 100
        y = sign / math.cos(x - c) if False else 1 / math.cos(x)
        if abs(y) <= 3: pts.append((X(x), yc + sy * y))
    line(ax, pts, 'sujet', lw=1.6)
br(0, 1); br(math.pi, -1)
line(ax, [(8, yc + sy * 0.5), (82, yc + sy * 0.5)], 'limite', dash=True, lw=1.2)
text(ax, 4, yc + sy, '1', 'fixe', 's'); text(ax, 3.5, yc - sy, '−1', 'fixe', 's')
text(ax, X(0), 78, r'$\sec x$', 'sujet', 'm')
text(ax, 66, yc + 7, r'$\sec x = 0{,}5$', 'limite', 's')
text(ax, 46, yc - 5.5, 'aucune valeur entre −1 et 1', 'limite', 's')
save(fig, '30-172')
