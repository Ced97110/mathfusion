import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

EM = ' '
def pitch(size='m'):
    return 1.636 * SIZE[size] * 25.4 / 72
def rowstr(vals):
    return EM.join(vals)
def brk(ax, cx, cy, hw, hh, role='encre'):
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.3, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.3, cy - hh)], role, lw=0.8)
def mat2(ax, cx, cy, r1, r2, role='encre', size='m'):
    text(ax, cx, cy + 3.2, rowstr(r1), role, size); text(ax, cx, cy - 3.2, rowstr(r2), role, size)
    brk(ax, cx, cy, 4.8, 5.4, role)

fig, ax = canvas(72)
for x, y, l in [(33, 59, '$A$'), (44, 59, '$B$'), (33, 50, '$C$'), (44, 50, '$D$')]:
    box(ax, x, y, 11, 9, 'sujet', label=l)
text(ax, 25, 54.5, '$M$', 'sujet', 'l')
box(ax, 2, 6, 41, 38, 'resultat')
box(ax, 45, 6, 41, 38, 'limite')
arrow(ax, (36, 48.5), (24, 45), 'fixe'); arrow(ax, (52, 48.5), (64, 45), 'fixe')
text(ax, 22.5, 39, 'blocs qui commutent', 'resultat', 's')
text(ax, 22.5, 31, r'$CD=DC$', 'resultat', 'm')
text(ax, 22.5, 22, r'$\det M=\det(AD-BC)$', 'resultat', 's')
text(ax, 22.5, 11, 'formule vraie', 'resultat', 's', weight='bold')
text(ax, 65.5, 39, 'blocs qui ne commutent pas', 'limite', 's')
text(ax, 65.5, 32, r'$CD\neq DC$', 'limite', 'm')
text(ax, 65.5, 25, r'$\det M=0$', 'limite', 'm')
text(ax, 65.5, 18, r'$\det(AD-BC)=-1$', 'limite', 's')
text(ax, 65.5, 11, 'formule fausse', 'limite', 's', weight='bold')
save(fig, '77-119')
