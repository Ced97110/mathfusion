import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def mat(x, y, w, h, rows, role, dash=False):
    box(ax, x, y, w, h, role, dash=dash)
    for r, s in enumerate(rows):
        text(ax, x + w / 2, y + h * (0.7 - 0.4 * r), s, role, 'm')
text(ax, 44, 46, r'$\mathbb{N}$ : entiers sans négatifs', 'fixe', 's')
mat(3, 20, 18, 14, ['1  2', '3  4'], 'sujet')
text(ax, 26.5, 27, '+', 'encre', 'l')
mat(32, 20, 22, 14, ['−1 −2', '−3 −4'], 'limite', dash=True)
line(ax, [(32, 20), (54, 34)], 'limite', lw=1.0)
line(ax, [(32, 34), (54, 20)], 'limite', lw=1.0)
text(ax, 59, 27, '=', 'encre', 'l')
mat(64, 20, 18, 14, ['0  0', '0  0'], 'fixe')
text(ax, 12, 14, r'tableau $A$', 'sujet', 's')
text(ax, 43, 14, 'cases négatives', 'limite', 's')
text(ax, 73, 14, 'tableau nul', 'fixe', 's')
text(ax, 44, 6, r'aucun opposé dans $\mathbb{N}$', 'limite', 'm')
save(fig, '51-162')
