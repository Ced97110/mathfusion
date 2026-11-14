import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 22, 54, 44, 10, role='sujet', label='G commutatif : στ = τσ')
text(ax, 44, 48, 'tous les sous-groupes sont normaux', 'resultat', 's')
subs = ['{1}', '⟨σ⟩', '⟨τ⟩', '⟨στ⟩', 'G']
cx = [10 + 17 * i for i in range(5)]
for c, t in zip(cx, subs):
    box(ax, c - 7.5, 32, 15, 9, role='resultat', label=t)
fields = {1: 'ℚ(√3)', 2: 'ℚ(√2)', 3: 'ℚ(√6)'}
for i, t in fields.items():
    arrow(ax, (cx[i], 31.2), (cx[i], 17.8), 'varie')
    box(ax, cx[i] - 8, 8, 16, 9.5, role='resultat', label=t)
text(ax, 80, 25, '(γ)', 'varie', 's')
text(ax, 44, 2.5, '3 corps galoisiens sur ℚ', 'resultat', 's')
save(fig, '63-143')
