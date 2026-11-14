import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'ordres possibles : diviseurs de 6', 'encre', 's')
rows = [(50, 'ordre 1', ['{1}'], 'sujet'),
        (36, 'ordre 2', ['⟨τ⟩', '⟨στ⟩', '⟨σ²τ⟩'], 'varie'),
        (22, 'ordre 3', ['⟨σ⟩'], 'resultat'),
        (8, 'ordre 6', ['S₃'], 'sujet')]
for y, lab, items, r in rows:
    text(ax, 2, y + 5, lab, 'encre', 's', ha='left')
    for i, t in enumerate(items):
        box(ax, 28 + 19 * i, y, 16, 10, role=r, label=t)
text(ax, 44, 3.5, '1 + 3 + 1 + 1 = 6 sous-groupes, 6 corps', 'resultat', 's')
save(fig, '63-146')
