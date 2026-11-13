import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
c = 11; x0 = 22
def row(y, vals, lab):
    text(ax, 12, y + c/2, lab, 'encre', 'l')
    for k, v in enumerate(vals):
        r = 'sujet' if k < 2 else 'autre'
        box(ax, x0 + k*c + (4 if k >= 2 else 0), y, c, c, r, label=str(v), r=0.5)
row(40, [3, 2, 5, 2], r'$x$')
row(26, [1, 4, 2, 1], r'$y$')
brace(ax, x0, x0 + 2*c, 24, 'sujet', '10', down=True, depth=1.8)
brace(ax, x0 + 2*c + 4, x0 + 4*c + 4, 24, 'autre', '1', down=True, depth=1.8)
arrow(ax, (x0 + c, 12), (x0 + 2*c + 2, 7.5), 'varie', lw=1.0); arrow(ax, (x0 + 3*c + 4, 12), (x0 + 2*c + 2, 7.5), 'varie', lw=1.0)
text(ax, x0 + 2*c + 2, 3.2, r'$B(x,y) = 10 + 1 = 11$', 'resultat', 'm')
save(fig, '75-037')
