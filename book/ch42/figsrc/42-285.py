import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
rows = [('départ', 'sujet', r"$(A\setminus B)\cap(B\setminus A)$"),
        (r"1. définition de $\setminus$", 'sujet', r"$(A\cap B')\cap(B\cap A')$"),
        ('2. on range les termes', 'sujet', r"$(A\cap A')\cap(B\cap B')$"),
        (r"3. $A\cap A'=\varnothing$", 'sujet', r"$\varnothing\cap(B\cap B')$"),
        (r"4. $\varnothing$ absorbe $\cap$", 'resultat', r"$\varnothing$")]
for i, (tag, role, ex) in enumerate(rows):
    y = 72 - 15 * i
    box(ax, 40, y, 46, 10, role, label=ex, size='m')
    text(ax, 2, y + 5, tag, 'varie', 's', ha='left')
    if i < 4: arrow(ax, (63, y), (63, y - 5), 'varie')
text(ax, 44, 5, 'aucun élément examiné', 'fixe', 's')
save(fig, '42-285')
