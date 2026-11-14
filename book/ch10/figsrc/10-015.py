import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
y = 30; f = numberline(ax, 10, 70, y, 50, 54, 1, arrow_right=False)
for v in (51, 52, 53, 54): disc(ax, f(v), y, 1.5, 'sujet')
disc(ax, f(50), y, 2.2, 'autre')
for i, v in enumerate((51, 52, 53, 54)):
    lv = 5 + 4.5 * i
    line(ax, [(f(v), y + 2), (f(v), y + lv)], 'fixe', dash=True)
    arrow(ax, (f(v), y + lv), (f(50) + 0.6, y + lv), 'varie')
    text(ax, (f(v) + f(50)) / 2 + 2, y + lv + 2.2, r'$-%d$' % (i + 1), 'varie', 's')
text(ax, 44, y - 11, 'tous dans le même sens : −10', 'varie', 'm')
text(ax, 44, y - 18, r'vrai : 51 + 52 + 53 + 54 = 210', 'resultat', 'm')
text(ax, 44, y - 25, r'estimé : 4 $\times$ 50 = 200', 'limite', 'm')
save(fig, '10-015')
