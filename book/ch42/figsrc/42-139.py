import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'même rôle : répéter une opération', 'encre', 'm')
rows = [(43, 'autre', r'$1 + 2 + 3 + 4$', r'$\sum_{i=1}^{4} i$', 'on répète +'),
        (19, 'sujet', r'$A_1 \cup A_2 \cup A_3 \cup A_4$', r'$\bigcup_{i=1}^{4} A_i$', 'on répète $\\cup$')]
for y, role, chain, sym, lab in rows:
    text(ax, 26, y, chain, role, 'l')
    arrow(ax, (50, y), (60, y), 'varie')
    text(ax, 72, y, sym, role, 'l')
    text(ax, 26, y - 9, lab, 'varie', 's')
    text(ax, 72, y - 11, 'i va de 1 à 4', role, 's')
save(fig, '42-139')
