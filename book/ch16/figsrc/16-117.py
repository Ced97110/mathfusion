import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for cx, head, a, b, lab, tag in [(23, 'avec des nombres', r'20 = 2$l$ + 6', r'14 = 2$l$', 'retire 6', '6 est connu'),
                                 (65, 'avec des lettres', r'$P = 2l + 2w$', r'$P - 2w = 2l$', r'retire 2$w$', r'2$w$ est un nombre')]:
    text(ax, cx, 61, head, 'sujet', 'm', weight='bold')
    box(ax, cx - 19, 42, 38, 11, 'sujet', label=a, size='m')
    arrow(ax, (cx, 42), (cx, 28), 'varie')
    text(ax, cx + 2, 35, lab, 'varie', 's', ha='left')
    box(ax, cx - 19, 15, 38, 11, 'resultat', label=b, size='m')
    text(ax, cx, 7, tag, 'fixe', 's')
line(ax, [(44, 8), (44, 58)], 'fixe', dash=True)
save(fig, '16-117')
