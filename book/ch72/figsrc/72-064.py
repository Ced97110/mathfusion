import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
s = 16; oy = 38
def panel(ox, a, b, lu, lv):
    arrow(ax, (ox, oy), (ox + a * s, oy), 'sujet', lw=2.0); arrow(ax, (ox, oy), (ox, oy + b * s), 'autre', lw=2.0)
    text(ax, ox + a * s / 2, oy - 4, lu, 'sujet', 'm')
    text(ax, ox + 3, oy + b * s + (1.5 if b > 0.6 else 2.5), lv, 'autre', 'm', ha='left')
panel(6, 1, 1, r'$u$', r'$v$')
panel(52, 2, 0.5, r'$2u$', r'$\frac{1}{2}v$')
arrow(ax, (28, 52), (44, 52), 'varie', lw=1.4); text(ax, 36, 56, r'$\eta$', 'varie', 'm')
text(ax, 22, 68, r'$B(u,v)=1$', 'resultat', 's'); text(ax, 62, 68, r'$B(2u,\frac{1}{2}v)=2\times\frac{1}{2}\times1$', 'resultat', 's')
text(ax, 62, 62, '= 1, comme avant', 'resultat', 's')
text(ax, 44, 22, 'carrés nuls : encore nuls', 'resultat', 's')
line(ax, [(8, 14), (80, 14)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 8, 'un exemple seulement :', 'encre', 's'); text(ax, 44, 2.5, 'pas toutes les isométries', 'encre', 's')
save(fig, '72-064')
