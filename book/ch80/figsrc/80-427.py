import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
box(ax, 12, 50, 30, 9, 'sujet', label='axiome', size='m')
box(ax, 56, 50, 30, 9, 'autre', label='jumeau', size='m')
R = [('A1', r"$a\vee b=b\vee a$", r"$a\wedge b=b\wedge a$"), ('A4', r"$a\vee O=a$", r"$a\wedge I=a$"), ('A5', r"$a\vee a'=I$", r"$a\wedge a'=O$")]
for i, (n, l, r) in enumerate(R):
    y = 36 - 13 * i
    text(ax, 6, y + 5, n, 'fixe', 's')
    box(ax, 12, y, 30, 10, 'sujet', label=l, size='s'); box(ax, 56, y, 30, 10, 'autre', label=r, size='s')
    arrow(ax, (42.5, y + 5), (55.5, y + 5), 'varie', both=True)
text(ax, 44, 4, r"échange $\vee\leftrightarrow\wedge$, $O\leftrightarrow I$", 'varie', 's')
save(fig, '80-427')
