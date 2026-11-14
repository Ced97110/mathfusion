import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'Lagrange : l’ordre divise 4 → 1, 2 ou 4', 'encre', 's')
box(ax, 30, 46, 28, 10, role='sujet', label='G : ordre 4')
mids = [(15, '⟨σ⟩ : ordre 2'), (44, '⟨τ⟩ : ordre 2'), (73, '⟨στ⟩ : ordre 2')]
for cx, t in mids:
    box(ax, cx - 13, 26, 26, 10, role='varie', label=t)
    line(ax, [(44, 45.2), (cx, 37.2)], 'fixe')
    line(ax, [(cx, 25.2), (44, 17.2)], 'fixe')
box(ax, 30, 7, 28, 10, role='sujet', label='{1} : ordre 1')
text(ax, 44, 2.5, 'cinq sous-groupes : 1 + 3 + 1', 'resultat', 'm', weight='bold')
save(fig, '63-136')
