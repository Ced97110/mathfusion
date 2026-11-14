import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(cx, y, n, role, r=3.0, sp=7.5):
    x0 = cx - (n - 1) * sp / 2
    for k in range(n):
        disc(ax, x0 + k * sp, y, r, role)
def col(cx, title, rows, verdict1, verdict2, vrole):
    text(ax, cx, 74, title, 'encre', 'm')
    y = 62
    row(cx, y, 4, 'sujet')
    for k in range(rows):
        row(cx, y - 14 * (k + 1), 2, 'varie')
    ytop = y - 14 + 5.5
    ybot = y - 14 * rows - 5.5
    box(ax, cx - 16, ybot, 32, ytop - ybot, 'varie', fill=False, dash=True, lw=1.0, r=0.8)
    text(ax, cx - 19.5, (ytop + ybot) / 2, 'K', 'varie', 'm', weight='bold')
    text(ax, cx, ybot - 8, verdict1, vrole, 's', weight='bold')
    text(ax, cx, ybot - 13, verdict2, vrole, 's')
col(22, r'$\mathbb{Z}/4 \oplus \mathbb{Z}/2$', 1, 'K cyclique', 'un seul tour', 'resultat')
col(66, r'$\mathbb{Z}/4 \oplus \mathbb{Z}/2 \oplus \mathbb{Z}/2$', 2, 'K pas cyclique', 'il faut un second tour', 'limite')
save(fig, '60-141')
