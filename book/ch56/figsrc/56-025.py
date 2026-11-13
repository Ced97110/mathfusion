import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0, cs = 10, 26, 5
text(ax, 20, 46, 'a = 12', 'resultat', 's')
for r in range(3):
    for c in range(4):
        box(ax, x0 + c * cs, y0 + r * cs, cs, cs, 'resultat', lw=0.5, r=0.3)
brace(ax, x0, x0 + 4 * cs, y0, 'varie', label='c = 4')
text(ax, 6, y0 + 7.5, 'b = 3', 'sujet', 's', rot=90)
text(ax, 22, 11, '3 divise 12 : 12 = 3 × 4', 'resultat', 's')
x1 = 50
text(ax, 66, 46, '5 ne divise pas 12', 'limite', 's')
cells = [(0, 2)] * 0
for r in range(3):
    for c in range(5):
        k = (2 - r) * 5 + c
        if k < 12:
            role = 'limite' if r == 0 else 'fixe'
            box(ax, x1 + c * cs, y0 + r * cs, cs, cs, role, lw=0.5, r=0.3)
        else:
            box(ax, x1 + c * cs, y0 + r * cs, cs, cs, 'fixe', fill=False, lw=0.5, r=0.3, dash=True)
text(ax, x1 + 5 * cs + 2, y0 + 2.5, 'reste 2', 'limite', 's', ha='left')
text(ax, 66, 11, '5 × 2 = 10, 5 × 3 = 15', 'fixe', 's')
save(fig, '56-025')
