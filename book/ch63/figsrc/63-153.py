import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, 'S₃/⟨σ⟩ (2 éléments)', 'sujet', 's')
text(ax, 66, 56, 'Gal(ℚ(j)/ℚ)', 'autre', 's')
rows = [(36, '⟨σ⟩ = {1, σ, σ²}', 'j ↦ j'), (18, 'τ⟨σ⟩ = {τ, στ, σ²τ}', 'j ↦ j²')]
for y, a, b in rows:
    box(ax, 2, y, 40, 11, role='sujet', label=a)
    box(ax, 50, y, 36, 11, role='autre', label=b)
    arrow(ax, (42.8, y + 5.5), (49.2, y + 5.5), 'resultat', both=True)
    text(ax, 46, y + 9, '≅', 'resultat', 'm')
text(ax, 44, 7, 'x² + x + 1 : racines j et j²', 'encre', 's')
save(fig, '63-153')
