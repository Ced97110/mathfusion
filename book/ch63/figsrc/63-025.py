import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 52, 64, r'respecte $+$', 'encre', 's')
text(ax, 74, 64, r'respecte $\times$', 'encre', 's')
rows = [(r'$a\mapsto a+1$', 'bijective, ni + ni ×', 'limite', ['non', 'non']),
        (r'$a\mapsto 2a$', 'bijective, mais pas ×', 'limite', ['oui', 'non']),
        (r'$\sigma:\sqrt{2}\mapsto-\sqrt{2}$', 'bijective, + et ×', 'resultat', ['oui', 'oui'])]
for i, (lab, tag, trole, cells) in enumerate(rows):
    y = 44 - 18 * i
    text(ax, 2, y + 10, lab, 'encre', 'm', ha='left')
    text(ax, 2, y + 3, tag, trole, 's', ha='left')
    for j, v in enumerate(cells):
        box(ax, 42 + 22 * j, y, 20, 14, 'resultat' if v == 'oui' else 'limite', label=v)
save(fig, '63-025')
