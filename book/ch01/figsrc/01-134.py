import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 10, 62, 30, 0, 4, arrow_right=False)
line(ax, [(6, 30), (10, 30)], 'fixe'); line(ax, [(62, 30), (68, 30)], 'fixe')
for x, s in zip([4, 17, 30], ['1 > 4', '2 > 5', '4 > 6']):
    box(ax, x, 34, 12, 8, 'limite', label=s, size='s')
for x, s in zip([43, 56], ['8 > 7', '16 > 8']):
    box(ax, x, 34, 12, 8, 'resultat', label=s, size='s')
brace(ax, 4, 42, 44, 'limite', label='faux', down=False)
brace(ax, 43, 68, 44, 'resultat', label='vrai', down=False)
arrow(ax, (49, 15), (49, 25.5), 'varie')
text(ax, 49, 11, 'départ : 3', 'varie', 'm')
line(ax, [(68, 30), (85, 30)], 'fixe', dash=True)
box(ax, 71, 34, 15, 8, 'fixe', fill=False, label='5, 6… ?', size='s', dash=True)
save(fig, '01-134')
