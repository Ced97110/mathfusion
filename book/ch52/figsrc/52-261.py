import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 54, '1 multiplication', 'encre', 's', ha='left')
for x, role, s in [(4, 'sujet', '8 divisions'), (24, 'varie', '4 produits'), (44, 'resultat', '3 fusions')]:
    box(ax, x, 40, 18, 9, role, label=s, size='s')
text(ax, 4, 30, '1000 multiplications', 'encre', 's', ha='left')
box(ax, 4, 16, 18, 9, 'sujet', label='8 divisions', size='s')
box(ax, 24, 16, 38, 9, 'varie', label='4000 petits produits', size='s')
box(ax, 64, 16, 18, 9, 'resultat', label='3 fusions', size='s')
text(ax, 13, 11, 'une fois', 'fixe', 's'); text(ax, 73, 11, 'une fois', 'fixe', 's')
text(ax, 43, 11, 'répétés', 'varie', 's')
save(fig, '52-261')
