import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 20, 80, 48, 11, 'sujet', label=r'$-2x < 6$', size='l')
for cx, role, step, res, test, tag in [
        (22, 'limite', r'÷ (−2), on garde $<$', r'$x < -3$', r'0 : $0 < -3$ faux', 'erreur'),
        (66, 'resultat', r'÷ (−2), on renverse $>$', r'$x > -3$', r'0 : $0 > -3$ vrai', 'juste')]:
    arrow(ax, (30 if cx < 44 else 58, 79.5), (cx, 66.5), role)
    box(ax, cx - 20, 55, 40, 11, 'varie', label=step, size='s')
    arrow(ax, (cx, 54.5), (cx, 42.5), role)
    box(ax, cx - 20, 31, 40, 11, role, label=res)
    text(ax, cx, 22, test, role, 's')
    text(ax, cx, 12, tag, role, 'm', weight='bold')
text(ax, 44, 3, 'le geste à surveiller : le nombre est négatif', 'varie', 's')
save(fig, '17-064')
