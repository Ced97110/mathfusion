import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s, ox, oy = 9.0, 10, 8
for i in range(5):
    for j in range(7):
        disc(ax, ox + i * s, oy + j * s, 0.6, 'fixe')
# chemin vers (3, 5)
line(ax, [(ox, oy), (ox + 3 * s, oy), (ox + 3 * s, oy + 5 * s)], 'varie', dash=True)
arrow(ax, (ox, oy), (ox + s, oy), 'sujet', lw=1.4)
arrow(ax, (ox, oy), (ox, oy + s), 'sujet', lw=1.4)
disc(ax, ox + 3 * s, oy + 5 * s, 1.3, 'resultat')
text(ax, ox + s / 2, oy - 3.2, r'$e_1$', 'sujet', 'm')
text(ax, ox - 3.2, oy + s / 2, r'$e_2$', 'sujet', 'm')
text(ax, 62, 66, r'$(3,\,5)$', 'resultat', 'l')
text(ax, 62, 58, r'$=3e_1+5e_2$', 'resultat', 'l')
text(ax, 62, 42, r'$e_1=(1,\,0)$', 'sujet', 'm')
text(ax, 62, 34, r'$e_2=(0,\,1)$', 'sujet', 'm')
text(ax, 68, 22, 'somme de deux points', 'fixe', 's')
text(ax, 68, 17, 'multiple entier d’un point', 'fixe', 's')
save(fig, '59-001')
