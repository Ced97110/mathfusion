import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$(a+b)^{4}=(a+b)\times(a+b)^{3}$', 'encre', 'm')
cx = [14, 30, 46, 62, 78]
def cell(c, y, s, role, bold=False):
    t = r'$\mathbf{%s}$' % s if bold else r'$%s$' % s
    box(ax, cx[c] - 7.5, y, 15, 7, role, label=t, size='m')
for c, s in enumerate(['a^{4}', '3a^{3}b', '3a^{2}b^{2}', 'ab^{3}']):
    cell(c, 40, s, 'sujet')
for c, s in enumerate(['a^{3}b', '3a^{2}b^{2}', '3ab^{3}', 'b^{4}']):
    cell(c + 1, 30, s, 'autre')
box(ax, 22, 29, 16, 19, 'varie', fill=False, dash=True, lw=1.3, r=0.5)
box(ax, 38.5, 29, 15.5, 19, 'varie', fill=False, dash=True, lw=1.3, r=0.5)
line(ax, [(6, 26), (86, 26)], 'fixe')
for c, s in enumerate(['a^{4}', '4a^{3}b', '6a^{2}b^{2}', '4ab^{3}', 'b^{4}']):
    cell(c, 16, s, 'resultat', bold=c in (1, 2))
save(fig, '01-171')
