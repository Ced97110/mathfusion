import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 18; f = numberline(ax, 6, 76, y, 46, 54, 1, arrow_right=False)
for v in (48, 49, 51, 52): disc(ax, f(v), y, 1.5, 'sujet')
disc(ax, f(50), y, 2.2, 'autre')
# one arrow per point; the label gives the distance in steps (1 step for 49 and 51, 2 for 48 and 52)
for v, lv, n in ((48, 14, 2), (52, 14, 2), (49, 8, 1), (51, 8, 1)):
    line(ax, [(f(v), y + 2), (f(v), y + lv)], 'fixe', dash=True)
    arrow(ax, (f(v), y + lv), (f(50) + (1 if v < 50 else -1) * 0.5, y + lv), 'resultat')
    lab = '%d pas' % n if n > 1 else '1 pas'
    text(ax, (f(v) + f(50)) / 2, y + lv + 2.4, lab, 'resultat', 's')
text(ax, f(50), y + 25, r'$c$ = 50', 'autre', 'm')
line(ax, [(f(50), y + 2.8), (f(50), y + 22)], 'autre', dash=True)
save(fig, '10-009')
