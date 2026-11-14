import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
s = 14

def scene(o, down, k_role):
    I = lambda p: iso(p[0], p[1], p[2], o, s)
    arrow(ax, I((0, 0, 0)), I((1, 0, 0)), 'sujet', lw=1.4)
    arrow(ax, I((0, 0, 0)), I((0, 1, 0)), 'autre', lw=1.4)
    arrow(ax, I((0, 0, 0)), I((0, 0, -1 if down else 1)), k_role, lw=1.8)
    text(ax, I((1, 0, 0))[0] + 1.5, I((1, 0, 0))[1] + 2.5, r'$i$', 'sujet', 'm', ha='left')
    text(ax, I((0, 1, 0))[0] - 3, I((0, 1, 0))[1] + 2.5, r'$j$', 'autre', 'm')
    return I

I1 = scene((24, 24), False, 'resultat')
text(ax, 24, 46, 'pouce : $k$', 'resultat', 's')
I2 = scene((66, 24), True, 'resultat')
text(ax, 69, 11, 'pouce : $-k$', 'resultat', 's', ha='left')
text(ax, 24, 55, 'main droite', 'encre', 'm', weight='bold')
text(ax, 66, 55, 'main gauche', 'encre', 'm', weight='bold')
text(ax, 24, 3.5, r'$i\times j=k$', 'resultat', 'm')
text(ax, 66, 3.5, r'$i\times j=-k$', 'limite', 'm')
text(ax, 44, 62, 'index sur $i$ (bleu), majeur sur $j$ (violet)', 'encre', 's')
save(fig, '41-107')
