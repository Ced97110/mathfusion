import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 12, 14, 7
for i in range(7):
    for j in range(8):
        disc(ax, ox + i * u, oy + j * u, 0.6, 'fixe')
arrow(ax, (ox, oy), (ox + 3 * u, oy), 'varie', lw=1.2)
arrow(ax, (ox + 3 * u, oy), (ox + 3 * u, oy + 5 * u), 'varie', lw=1.2)
arrow(ax, (ox, oy), (ox + 3 * u, oy + 5 * u), 'resultat', lw=1.2)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=2.0)
arrow(ax, (ox, oy), (ox, oy + u), 'sujet', lw=2.0)
disc(ax, ox + 3 * u, oy + 5 * u, 1.5, 'resultat')
text(ax, ox + 3.5, oy + 3.4, r'$e_1$', 'sujet', 'm')
text(ax, ox - 4, oy + 3.5, r'$e_2$', 'sujet', 'm')
brace(ax, ox, ox + 3 * u, oy - 2.5, 'varie', label=r'$3\,e_1$', size='m')
text(ax, ox + 3 * u + 6, oy + 2.5 * u, r'$5\,e_2$', 'varie', 'm')
text(ax, ox + 3 * u, oy + 5 * u + 4.5, '(3 ; 5)', 'resultat', 'm', weight='bold')
text(ax, 72, 44, r'$(3;5)=3\,e_1+5\,e_2$', 'resultat', 'm')
text(ax, 72, 37, 'une seule écriture', 'resultat', 's')
save(fig, '57-215')
