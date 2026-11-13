import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = 9; x0 = 26
def row(y, vals, role, lab, res):
    text(ax, 12, y + c/2, lab, role, 'm')
    for k, v in enumerate(vals):
        r = role if v else 'fixe'
        box(ax, x0 + k*c, y, c, c, r, fill=bool(v), label=str(v), size='m', r=0.5)
    text(ax, x0 + 4*c + 9, y + c/2, res, role, 'm')
row(34, [1, 0, 0, 0], 'sujet', r'$e_1$', '')
row(20, [0, 0, 1, 0], 'resultat', r'$e_2$', r'$B = 0$')
row(6, [0, 1, 1, 0], 'limite', r'$e_2$', r'$B = 1$')
brace(ax, x0, x0 + 2*c, 46, 'sujet', down=False, depth=1.6)
brace(ax, x0 + 2*c, x0 + 4*c, 46, 'autre', down=False, depth=1.6)
text(ax, x0 + c, 53, r'$P_1$', 'sujet', 'm'); text(ax, x0 + 3*c, 53, r'$P_1^{\perp}$', 'autre', 'm')
save(fig, '75-036')
