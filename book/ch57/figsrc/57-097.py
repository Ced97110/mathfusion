import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 77, 'quart de tour, $v$ = (2 ; 1)', 'encre', 'm')
blocks = [('$f=2x+3$', [('$2x$', '2·$Tv$ = (−2 ; 4)'), ('3', '3·$v$ = (6 ; 3)')], '(4 ; 7)'),
          ('$f=5x^2+1$', [('$5x^2$', '5·$T^2v$ = (−10 ; −5)'), ('1', '1·$v$ = (2 ; 1)')], '(−8 ; −4)')]
for b, (head, rows, res) in enumerate(blocks):
    y0 = 69 - b * 32
    text(ax, 2, y0, head, 'encre', 'm', ha='left')
    for (t, a), yc in zip(rows, (y0 - 10, y0 - 20)):
        box(ax, 2, yc - 4, 16, 8, 'sujet', label=t, size='m')
        arrow(ax, (19, yc), (27, yc), 'varie')
        box(ax, 28, yc - 4, 36, 8, 'varie', label=a, size='s')
        arrow(ax, (65, yc), (71.5, y0 - 15), 'resultat')
    box(ax, 72, y0 - 20, 14, 10, 'resultat', label=res, size='s')
save(fig, '57-097')
