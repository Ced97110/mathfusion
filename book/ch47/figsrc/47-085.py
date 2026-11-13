import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 62, r'classe $gH$', 'sujet', 'm')
text(ax, 68, 62, r'inverses : $Hg^{-1}$', 'resultat', 'm')
box(ax, 3, 36, 34, 22, 'sujet'); box(ax, 51, 36, 34, 22, 'resultat')
for i, (a, b) in enumerate([('(1 3)', '(1 3)'), ('(1 2 3)', '(1 3 2)')]):
    y = 50 - i * 10
    text(ax, 20, y, a, 'sujet', 'm'); text(ax, 68, y, b, 'resultat', 'm')
    arrow(ax, (37.5, y), (50.5, y), 'varie')
text(ax, 44, 55.5, 'inverse', 'varie', 's')
box(ax, 8, 6, 72, 18, 'varie', label=r'$(gh)^{-1}=h^{-1}g^{-1}$', size='l')
text(ax, 44, 29, 'le renversement', 'varie', 's')
save(fig, '47-085')
