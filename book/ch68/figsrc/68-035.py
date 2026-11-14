import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# l'ensemble C : les deux mots permis
box(ax, 3, 18, 40, 38, 'sujet')
text(ax, 23, 51, r'$C$', 'sujet', 'xl', weight='bold')
box(ax, 9, 34, 28, 8, 'encre', label='000')
box(ax, 9, 22, 28, 8, 'encre', label='111')
text(ax, 23, 12, 'mots permis', 'sujet', 'm')
# mot reçu hors de C
box(ax, 58, 34, 24, 8, 'limite', label='101')
arrow(ax, (57, 38), (44.5, 38), 'limite', curve=0.0)
text(ax, 70, 48, 'mot reçu', 'limite', 'm')
text(ax, 70, 26, r'$101 \notin C$', 'limite', 'l', weight='bold')
text(ax, 23, 3, r'$000 \in C$', 'resultat', 'm', weight='bold')
save(fig, '68-035')
