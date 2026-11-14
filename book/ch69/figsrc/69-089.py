import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [26, 43, 60, 77]
heads = [r'$x=-2$', r'$x=0$', r'$x=1$', r'$x=2$']
cols = ['−\n+\n−\n+', '+\n−\n−\n+', '−\n0\n+\n+', '+\n+\n+\n+']
vs = ['3', '2', '1', '0']
text(ax, 7, 36, 'f0\nf1\nf2\nf3', 'encre', 'm', style='italic')
text(ax, 7, 14, 'V', 'resultat', 'l')
for x, h, c, v in zip(cx, heads, cols, vs):
    text(ax, x, 51, h, 'encre', 's')
    box(ax, x - 6.5, 26, 13, 20, 'fixe', label=c)
    text(ax, x, 14, v, 'resultat', 'l')
for i in range(3):
    arrow(ax, (cx[i] + 3, 14), (cx[i + 1] - 3, 14), 'varie')
save(fig, '69-089')
