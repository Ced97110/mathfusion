import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def paren(x, y0, y1, left, role='sujet', b=1.6):
    ym, h = (y0 + y1) / 2, (y1 - y0) / 2
    sg = -1 if left else 1
    pts = [(x + sg * b * (1 - t * t), ym + t * h) for t in [i / 8 - 1 for i in range(17)]]
    line(ax, pts, role, lw=1.0)
# haut : même triplet en ligne puis en colonne
text(ax, 20, 67, 'sur une ligne', 'fixe', 's')
box(ax, 3, 48.5, 34, 10, 'sujet', label='(2, 7, −1)')
text(ax, 46, 53.5, '=', 'encre', 'l')
text(ax, 66, 67, 'en colonne', 'fixe', 's')
paren(55, 44, 63, True); paren(77, 44, 63, False)
for v, y in zip(['2', '7', '−1'], [60, 53.5, 47]):
    text(ax, 66, y, v, 'sujet', 'l')
# bas : trois formules longues, une par ligne
text(ax, 20, 18, 'une case par ligne', 'varie', 's')
paren(41, 2, 30, True); paren(79, 2, 30, False)
for s, y in zip([r'$x_1$', r'$2x_1+x_2$', r'$x_1-x_2$'], [24, 16, 8]):
    text(ax, 60, y, s, 'sujet', 'l')
save(fig, '58-122')
