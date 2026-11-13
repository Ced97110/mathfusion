import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, 'lettres grecques = scalaires', 'varie', 'm')
for i, g in enumerate([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$']):
    box(ax, 4 + 20.5 * i, 50, 17, 13, 'varie', label=g, size='xl')
text(ax, 44, 43, 'lettres latines = vecteurs', 'sujet', 'm')
for i, g in enumerate(['$u$', '$v$', '$w$']):
    box(ax, 14 + 24 * i, 25, 17, 13, 'sujet', label=g, size='xl')
text(ax, 44, 14, r'$\alpha u$ : scalaire × vecteur', 'encre', 'm')
text(ax, 44, 6, r'$\alpha\beta$ : deux scalaires', 'encre', 'm')
save(fig, '58-086')
