import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for x, t, r in ((18, 'corps', 'sujet'), (52, 'radical', 'varie'), (79, 'groupe', 'autre')):
    text(ax, x, 75, t, r, 'm', weight='bold')
rows = ((46, r'$\mathbb{Q}\subset\mathbb{Q}(j)$', r'$j=(-1+\sqrt{-3})/2$', 'racine carrée', 'degré 2', r'$\mathbb{Z}/2$'),
        (14, r'$\mathbb{Q}(j)\subset\mathbb{Q}(j,\sqrt[3]{2})$', r'$\sqrt[3]{2}$', 'racine cubique', 'degré 3', r'$\mathbb{Z}/3$'))
for y, a, b, c, d, e in rows:
    box(ax, 2, y, 33, 13, 'sujet', label=a, size='s')
    box(ax, 38, y, 29, 13, 'varie', label=b, size='s')
    box(ax, 71, y, 15, 13, 'autre', label=e)
    text(ax, 18.5, y - 4, d, 'sujet', 's')
    text(ax, 52.5, y - 4, c, 'varie', 's')
    arrow(ax, (35.5, y + 6.5), (37.5, y + 6.5), 'fixe'); arrow(ax, (67.5, y + 6.5), (70.5, y + 6.5), 'fixe')
save(fig, '64-169')
