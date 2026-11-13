import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
ys = [88, 62, 36, 10]
GREEN = 'resultat'
def tower(cx, names, role, labs):
    for y, n in zip(ys, names):
        box(ax, cx - 11, y - 5, 22, 10, role, label=n, size='s')
    for i, (lab, simple) in enumerate(labs):
        y0, y1 = ys[i] - 5, ys[i + 1] + 5
        if simple:
            ax.add_patch(Rectangle((cx - 3, y1), 6, y0 - y1, ec=COL['resultat'], fc=FILL['resultat'], lw=1.0, zorder=2))
        else:
            line(ax, [(cx, y0), (cx, y1)], 'fixe', lw=1.0)
        text(ax, cx + 5 if simple else cx + 2, (y0 + y1) / 2, lab, 'resultat' if simple else 'fixe', 's', ha='left', weight='bold' if simple else 'normal')
tower(14, [r'$GL_n$', r'$SL_n$', r'$C$', r'$\{1\}$'], 'sujet',
      [('4 : commutatif', False), ('60 : simple', True), ('2 : commutatif', False)])
tower(60, [r'$O$', r'$SO$', r'$\Omega$', r'$\{1\}$'], 'autre',
      [('{±1} : commutatif', False), ('abélien = commutatif', False), ('simple*\n(simple après ±1)', True)])
save(fig, '73-207')
