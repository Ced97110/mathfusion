import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'unicité : trois questions', 'encre', 'm')
heads = [(2, 'propriété'), (31, 'critère'), (60, 'transmission')]
for x, h in heads:
    box(ax, x, 50, 26, 9, 'sujet', label=h, size='s')
qs = ['qui garantit\nl’unicité ?', 'quel test\nla vérifie ?', 'se garde-t-elle\nde ℤ à ℤ[x] ?']
for (x, h), q in zip(heads, qs):
    text(ax, x + 13, 41, q, 'encre', 's')
box(ax, 2, 20, 26, 8, 'resultat', label='ℤ : oui', size='s')
box(ax, 2, 8, 26, 8, 'limite', label='√−5 : non', size='s')
box(ax, 31, 14, 26, 9, 'varie', label='test court', size='s')
box(ax, 60, 14, 9, 9, 'sujet', label='ℤ', size='s')
box(ax, 77, 14, 9, 9, 'sujet', label='ℤ[x]', size='s')
arrow(ax, (69, 18.5), (77, 18.5), 'varie')
text(ax, 73, 25, '?', 'varie', 'm')
save(fig, '56-009')
