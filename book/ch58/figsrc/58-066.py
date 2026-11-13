import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, 'trois bases, même nombre', 'encre', 'm')
U = 8.0
panels = [(15, [((1, 0), 'sujet'), ((0, 1), 'autre')]),
          (44, [((2, 1), 'sujet'), ((1, 1), 'autre')]),
          (73, [((1, 0), 'sujet'), ((1, 1), 'autre')])]
for cx, vecs in panels:
    ox, oy = cx - 10, 24
    line(ax, [(ox, oy), (ox + 21, oy)], 'fixe', lw=0.5)
    line(ax, [(ox, oy), (ox, oy + 18)], 'fixe', lw=0.5)
    for (a, b), role in vecs:
        tip = (ox + a * U, oy + b * U)
        arrow(ax, (ox, oy), tip, role, lw=1.2)
        lab = f'({a}, {b})'
        if (a, b) == (1, 0):
            text(ax, tip[0] + 1, tip[1] - 3.2, lab, role, 's')
        elif (a, b) == (0, 1):
            text(ax, tip[0] + 1.5, tip[1] + 3.2, lab, role, 's', ha='left')
        elif (a, b) == (2, 1):
            text(ax, tip[0] + 1.5, tip[1] + 3.2, lab, role, 's')
        else:
            text(ax, tip[0] - 2.5, tip[1] + 5.2, lab, role, 's')
    text(ax, cx, 8, '2 éléments', 'resultat', 's')
save(fig, '58-066')
