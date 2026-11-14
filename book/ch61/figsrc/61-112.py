import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 1, 14, 42, 54, 'sujet', fill=False, lw=1.0); box(ax, 45, 14, 42, 54, 'autre', fill=False, lw=1.0)
text(ax, 22, 62, 'algébrique', 'sujet', 'l', weight='bold'); text(ax, 66, 62, 'finie', 'autre', 'l', weight='bold')
for y, e in zip([48, 37, 26], [r'$3+\sqrt{2}$', r'$\sqrt{2}$', '…']):
    box(ax, 3, y - 4.5, 16, 9, 'sujet', label=e, size='s')
    arrow(ax, (19.5, y), (24.5, y), 'varie')
    box(ax, 25, y - 4.5, 17, 9, 'resultat', label='polynôme', size='s')
box(ax, 49, 24, 34, 28, 'autre', label=r'$1,\ \sqrt{2}$', size='l')
text(ax, 66, 19, 'une seule liste', 'autre', 's')
text(ax, 22, 11, 'un test par élément', 'sujet', 's'); text(ax, 66, 11, 'un seul test', 'autre', 's')
arrow(ax, (66, 6.5), (24, 6.5), 'resultat', lw=1.2); text(ax, 46, 2.5, 'finie ⇒ algébrique', 'resultat', 's')
save(fig, '61-112')
