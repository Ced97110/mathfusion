import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
ys = [72, 57, 42, 27]
left = [r'$-1$', r'$9$', r'$-5$', r'$9/4$']
right = [r'$3$', r'$9$', r'$3$', r'$9/4$']
for k, y in enumerate(ys):
    box(ax, 13, y, 22, 9, 'sujet', label=left[k])
    box(ax, 55, y, 22, 9, 'sujet', label=right[k])
    text(ax, 45, y + 4.5, r'$f_%d$' % k, 'encre', 'm')
for k in range(3):
    arrow(ax, (24, ys[k]), (24, ys[k + 1] + 9.5), 'varie')
text(ax, 24, 16, r'en $-2$ : $V=3$', 'resultat', 'm')
text(ax, 66, 16, r'en $2$ : $V=0$', 'resultat', 'm')
save(fig, '69-087')
