import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cols = [(16, [r'ℤ/5 : 5', r'$\{e\}$ : 1'], 'un pas', 'résoluble', 'resultat'),
        (44, [r'$S_3$ : 6', r'$A_3$ : 3', r'$\{e\}$ : 1'], 'deux pas', 'résoluble', 'resultat'),
        (72, [r'$A_5$ : 60', 'aucune suite'], 'impossible', 'non résoluble', 'limite')]
for cx, boxes, cap, tag, role in cols:
    for i, lab in enumerate(boxes):
        y = 62 - 14 * i
        bad = role == 'limite' and i == 1
        box(ax, cx - 12, y, 24, 9, 'limite' if bad else 'sujet', label=lab, size='s', dash=bad)
        if i > 0: arrow(ax, (cx, y + 14 - 0.5), (cx, y + 9.5), 'limite' if bad else 'sujet')
    text(ax, cx, 22, cap, 'fixe', 's')
    text(ax, cx, 12, tag, role, 'm', weight='bold')
save(fig, '64-029')
