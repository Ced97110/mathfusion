import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, tag, t, role in ((54, 'avant', r'$50\times50\approx2\,500$', 'varie'), (34, 'pendant', r'$48\times52=2\,496$', 'sujet')):
    text(ax, 4, y + 5, tag, role, 'm', ha='left', weight='bold')
    box(ax, 28, y, 56, 10, role, label=t, size='m')
arrow(ax, (56, 53), (56, 45.6), 'fixe'); arrow(ax, (56, 33), (56, 26), 'fixe')
text(ax, 4, 17, 'après', 'resultat', 'm', ha='left', weight='bold')
line(ax, [(30, 17), (84, 17)], 'fixe')
x1, x2 = 52, 62
disc(ax, x1, 17, 1.5, 'sujet'); disc(ax, x2, 17, 1.5, 'varie')
text(ax, x1 - 2, 23, '2 496', 'sujet', 's', ha='right'); text(ax, x2 + 2, 23, '2 500', 'varie', 's', ha='left')
brace(ax, x1, x2, 14, 'resultat', 'proches', down=True)
save(fig, '10-100')
