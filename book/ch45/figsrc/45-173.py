import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def drow(y, s, role, xc=58):
    t = text(ax, xc, y, '   '.join(s), role, 'xl'); fig.canvas.draw()
    bb = t.get_window_extent().transformed(ax.transData.inverted()); n = len(s)
    d = (bb.x1 - bb.x0) / (n + 1.5 * (n - 1)); return [bb.x0 + d / 2 + i * 2.5 * d for i in range(n)], d
cols, d = drow(40, '0101', 'sujet'); drow(28, '0111', 'autre')
ax.add_patch(Rectangle((cols[2] - 1.6 * d, 8), 3.2 * d, 38, fc=FILL['varie'], ec='none', zorder=1))
drow(13, '0010', 'resultat')
text(ax, 22, 40, 'envoyé', 'sujet', 's'); text(ax, 22, 28, 'reçu', 'autre', 's'); text(ax, 22, 13, 'somme', 'resultat', 's')
text(ax, 36, 34, '+', 'encre', 'xl'); line(ax, [(39, 20.5), (80, 20.5)], 'encre')
text(ax, 44, 3.5, 'le 1 marque le rang changé', 'varie', 's')
save(fig, '45-173')
