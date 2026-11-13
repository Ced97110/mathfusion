import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71.5, 'on teste 21 en sautant le 3', 'encre', 'm')
cx = [14, 34, 54, 74]
for x, p in zip(cx, [2, 3, 5, 7]):
    if p == 3:
        box(ax, x - 6, 48, 12, 10, 'limite', fill=False, label='3', size='l', dash=True)
    elif p == 7:
        box(ax, x - 6, 48, 12, 10, 'fixe', fill=False, label='7', size='l', dash=True)
    else:
        box(ax, x - 6, 48, 12, 10, 'varie', label=str(p), size='l')
for a, b, role in [(14, 34, 'varie'), (34, 54, 'varie')]:
    pass
arrow(ax, (16, 58.3), (52, 58.3), 'varie', lw=0.9, curve=-0.35)
text(ax, 34, 66.2, 'saute le 3', 'limite', 's')
text(ax, 14, 41, 'reste 1', 'varie', 's')
text(ax, 54, 41, r'$21 \div 5$ : $4 < 5$', 'varie', 's')
text(ax, 74, 41, 'jamais essayé', 'fixe', 's')
arrow(ax, (54, 47), (54, 44), 'varie', lw=0.8)
box(ax, 40, 26, 28, 8, 'limite', label='critère : « stop »', size='s')
arrow(ax, (54, 38.3), (54, 34.5), 'limite')
text(ax, 58, 21, 'il conclurait : 21 est premier', 'limite', 's')
box(ax, 8, 4, 72, 10, 'limite', label=r'faux : $21 = 3 \times 7$, le 3 divise 21', size='s')
arrow(ax, (34, 47), (34, 15), 'limite', lw=0.8, curve=0)
save(fig, '05-054')
