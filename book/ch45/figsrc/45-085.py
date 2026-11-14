import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'ligne de 2 : $2\times x$ modulo 4', 'sujet', 'm')
x0, bw, gap = 26, 11, 4
text(ax, 12, 44.5, r'$x$', 'fixe', 'l'); text(ax, 12, 14.5, 'valeur', 'sujet', 'm')
for i in range(4):
    x = x0 + i * (bw + gap)
    box(ax, x, 40, bw, 9, 'fixe', label=str(i))
    hit = i in (0, 2)
    box(ax, x, 10, bw, 9, 'limite' if hit else 'fixe', label=str(i), dash=not hit, fill=hit)
    j = (2 * i) % 4
    arrow(ax, (x + bw / 2, 39.5), (x0 + j * (bw + gap) + bw / 2, 19.5), 'varie')
text(ax, x0 + 1 * (bw + gap) + bw / 2, 4.5, 'jamais atteint', 'limite', 's')
text(ax, x0 + 3 * (bw + gap) + bw / 2 - 1, 4.5, 'jamais atteint', 'limite', 's')
save(fig, '45-085')
