import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
full = 50
box(ax, 2, 56, full, 10, 'sujet', label=r'$GL_2(\mathbb{F}_5)$ : 480 matrices', size='s')
box(ax, 2, 34, full / 4, 10, 'varie', label='120', size='s')
box(ax, 2, 12, full / 8, 10, 'resultat', label='60', size='s')
text(ax, 18, 39, 'noyau du déterminant', 'varie', 's', ha='left')
text(ax, 11, 17, 'quotient par le centre :\nsimple', 'resultat', 's', ha='left')
for y, ro, lab in [(56, 'sujet', 'ch. 44, 51, 58 :\ngroupes, matrices'), (34, 'varie', 'ch. 47, 48 :\nnormaux, quotients'), (12, 'resultat', 'ch. 64 :\ngroupes simples')]:
    box(ax, 56, y - 1, 30, 12, ro, label=lab, size='s')
arrow(ax, (8, 55.5), (8, 45.5), 'encre'); arrow(ax, (8, 33.5), (8, 23.5), 'encre')
text(ax, 44, 4, 'et ch. 71, 72 : formes quadratiques', 'fixe', 's')
save(fig, '73-250')
