import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$D_4$ : 8 mouvements', 'sujet', 'l', weight='bold')
x0, s, g = 5.0, 8.0, 2.0
xs = [x0 + i * (s + g) for i in range(8)]
for i, x in enumerate(xs):
    box(ax, x, 26, s, s, 'sujet' if i < 6 else 'limite')
brace(ax, xs[0], xs[2] + s, 24, 'sujet', '3')
brace(ax, xs[3], xs[5] + s, 24, 'sujet', '3')
brace(ax, xs[6], xs[7] + s, 24, 'limite', 'reste 2')
text(ax, 44, 8, r'$8 = 2 \times 3 + 2$ : 3 ne divise pas 8', 'encre', 'm')
save(fig, '44-270')
