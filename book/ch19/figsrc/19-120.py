import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
fig, ax = canvas(56)
text(ax, 44, 51, 'montée ÷ avancée', 'encre', 'm', weight='bold')
cs = (15, 44, 73)
line(ax, [(cs[0] - 10, 34), (cs[0] + 10, 34)], 'resultat', lw=1.5)
line(ax, [(cs[1] - 8, 28), (cs[1] + 8, 40)], 'resultat', lw=1.5)
line(ax, [(cs[2], 26), (cs[2], 42)], 'limite', lw=1.5)
for c, s, r in zip(cs, (r'$0 \div 4 = 0$', r'$2 \div 1 = 2$', r'$-4 \div 0$'), ('resultat', 'resultat', 'limite')):
    text(ax, c, 17, s, r, 's', weight='bold')
text(ax, cs[0], 8, 'un nombre', 'resultat', 's'); text(ax, cs[1], 8, 'un nombre', 'resultat', 's')
text(ax, cs[2], 8, 'pas un nombre', 'limite', 's')
save(fig, '19-120')
