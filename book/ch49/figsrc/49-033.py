import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$\eta$ : un seul signe pour la traduction', 'sujet', 'm')
for x, a, b in [(18, r'$a$', r'$\eta(a)$'), (44, r'$b$', r'$\eta(b)$'), (70, r'$ab$', r'$\eta(ab)$')]:
    box(ax, x - 8, 36, 16, 9, 'sujet', label=a)
    box(ax, x - 8, 16, 16, 9, 'resultat', label=b)
    arrow(ax, (x, 36), (x, 25.5), 'varie')
    text(ax, x + 3.5, 30.7, r'$\eta$', 'varie', 's', ha='left')
text(ax, 44, 8, r'$\eta(ab)=\eta(a)\,\eta(b)$', 'resultat', 'l')
text(ax, 44, 50, 'mots', 'sujet', 's')
text(ax, 44, 2.8, r'ex. : $xy\mapsto 2\times3=6$', 'fixe', 's')
save(fig, '49-033')
