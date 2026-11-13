import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# colonnes : gauche (x^2+y^2)^2, droite x^3-3xy^2
text(ax, 25, 76, r'$(x^2+y^2)^2$', 'sujet', 'm')
text(ax, 65, 76, r'$x^3-3xy^2$', 'varie', 'm')
rows = [
    (58, r'point $(1\,;\,0)$', r'$(1^2+0^2)^2=1$', r'$1^3-3\cdot1\cdot0^2=1$', 'resultat', '$1=1$ : sur la courbe'),
    (28, r'point $(0\,;\,1)$', r'$(0^2+1^2)^2=1$', r'$0^3-3\cdot0\cdot1^2=0$', 'limite', r'$1\neq0$ : hors courbe'),
]
for y, lab, L, R, role, verdict in rows:
    text(ax, 12, y + 15, lab, 'encre', 's')
    box(ax, 4, y + 3, 40, 8, 'sujet', label=L, size='s')
    box(ax, 46, y + 3, 40, 8, 'varie', label=R, size='s')
    arrow(ax, (24, y + 3), (36, y - 2), role)
    arrow(ax, (66, y + 3), (54, y - 2), role)
    box(ax, 24, y - 9, 40, 8, role, label=verdict, size='s')
text(ax, 44, 6, r'$x^2\cdot x^2=x^4$ : $2+2=4$, degré 4', 'encre', 's')
save(fig, '40-004')
