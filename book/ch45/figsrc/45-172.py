import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def drow(y, s, role, xc=58):
    t = text(ax, xc, y, '   '.join(s), role, 'xl'); fig.canvas.draw()
    bb = t.get_window_extent().transformed(ax.transData.inverted()); n = len(s)
    d = (bb.x1 - bb.x0) / (n + 1.5 * (n - 1)); return [bb.x0 + d / 2 + i * 2.5 * d for i in range(n)], d
a, b, c = '01011101', '01001011', '00010110'
cols, d = drow(40, a, 'sujet'); drow(28, b, 'autre')
for i in range(8):
    if a[i] != b[i]: ax.add_patch(Rectangle((cols[i] - 1.4 * d, 10), 2.8 * d, 36, fc=FILL['varie'], ec='none', zorder=1))
drow(15, c, 'resultat')
text(ax, 22, 40, 'liste 1', 'sujet', 's'); text(ax, 22, 28, 'liste 2', 'autre', 's'); text(ax, 22, 15, 'somme', 'resultat', 's')
text(ax, 30, 34, '+', 'encre', 'xl'); line(ax, [(33, 21.5), (84, 21.5)], 'encre')
text(ax, 3, 5, 'chiffres différents : 1', 'varie', 's', ha='left'); text(ax, 85, 5, 'chiffres égaux : 0', 'fixe', 's', ha='right')
save(fig, '45-172')
