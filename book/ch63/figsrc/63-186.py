import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# corps à 4 éléments sur le corps à 2 éléments : degré 2 ; groupe de Galois : 2 éléments
cw, x0 = 16, 8
text(ax, 44, 78, 'corps à 4 éléments : 0, 1, $a$, $a + 1$', 'sujet', 's')
text(ax, 4, 62, 'degré', 'sujet', 'm', ha='left')
box(ax, 40, 57, cw, 10, 'sujet', label='1')
box(ax, 40 + cw, 57, cw, 10, 'sujet', label=r'$a$')
text(ax, 40 + 2 * cw + 3, 62, '= 2', 'sujet', 'm', ha='left')
text(ax, 4, 38, 'groupe', 'varie', 'm', ha='left')
box(ax, 40, 33, cw, 10, 'varie', label=r'$x \mapsto x$', size='s')
box(ax, 40 + cw, 33, cw, 10, 'varie', label=r'$x \mapsto x^2$', size='s')
text(ax, 40 + 2 * cw + 3, 38, '= 2', 'varie', 'm', ha='left')
text(ax, 44, 22, r'$|G| = [E : F]$', 'resultat', 'l')
arrow(ax, (40 + cw * 1.5, 31), (40 + cw * 1.5, 24), 'fixe', lw=0.01) if False else None
text(ax, 44, 11, r'$x \mapsto x^2$ engendre $G$ : $G$ cyclique', 'resultat', 's')
save(fig, '63-186')
