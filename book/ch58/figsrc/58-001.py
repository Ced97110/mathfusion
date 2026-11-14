import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# deux clients : (riz, lentilles) = (2, 1) puis (5, 4)
sales = [('Client 1', 2, 1, 46), ('Client 2', 5, 4, 20)]
u, gap, x0 = 6.0, 1.2, 36
for name, nr, nl, y in sales:
    text(ax, 2, y + 6, name, 'encre', 'm', ha='left', weight='bold')
    text(ax, x0 - 2, y + 11, 'riz', 'sujet', 's', ha='right')
    text(ax, x0 - 2, y + 2.5, 'lentilles', 'autre', 's', ha='right')
    for i in range(nr):
        box(ax, x0 + i * (u + gap), y + 8, u, u, 'sujet', r=0.5)
    for i in range(nl):
        box(ax, x0 + i * (u + gap), y - 0.5, u, u, 'autre', r=0.5)
    text(ax, x0 + 5 * (u + gap) + 1, y + 11, f'{nr} kg', 'sujet', 's', ha='left')
    text(ax, x0 + 5 * (u + gap) + 1, y + 2.5, f'{nl} kg', 'autre', 's', ha='left')
text(ax, 44, 6, 'une vente = deux quantités', 'encre', 'm')
save(fig, '58-001')
