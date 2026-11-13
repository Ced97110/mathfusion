import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, x1 = 24, 80
f = numberline(ax, x0, x1, 7, -1, 5, arrow_right=False)
for v in (0, 2, 3, 4):
    line(ax, [(f(v), 7), (f(v), 64)], 'fixe', lw=0.4, dash=True)
def pt(v, y, role, closed):
    ax.add_patch(Circle((f(v), y), 1.4, ec=COL[role], fc=FILL[role] if False else (COL[role] if closed else 'white'), lw=0.9, zorder=6))
def bar(a, b, y, role, ca, cb):
    line(ax, [(f(a), y), (f(b), y)], role, lw=3)
    if ca is not None: pt(a, y, role, ca)
    if cb is not None: pt(b, y, role, cb)
rows = [(61, r'$A$', 'sujet'), (52, r'$B$', 'autre'), (43, r'$A \cap B$', 'resultat'),
        (34, r'$A \cup B$', 'resultat'), (25, r'$A \setminus B$', 'resultat'), (16, r"$A'$", 'resultat')]
for y, lab, role in rows:
    text(ax, 3, y, lab, role, 'm', ha='left')
bar(0, 3, 61, 'sujet', False, True)
bar(2, 4, 52, 'autre', True, False)
bar(2, 3, 43, 'resultat', True, True)
bar(0, 4, 34, 'resultat', False, False)
bar(0, 2, 25, 'resultat', False, False)
bar(-1, 0, 16, 'resultat', None, True)
bar(3, 5, 16, 'resultat', False, None)
arrow(ax, (f(-0.7), 16), (f(-1), 16), 'resultat', lw=1.2)
arrow(ax, (f(4.7), 16), (f(5), 16), 'resultat', lw=1.2)
save(fig, '42-136')
