import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'G = S₃ : 6 éléments, τ garde r', 'encre', 's')
starts = [9, 39, 69]
for k, s in enumerate(starts):
    r = 'sujet' if k == 0 else 'autre'
    disc(ax, s, 47, 4, role=r)
    disc(ax, s + 9, 47, 4, role=r)
    brace(ax, s - 5, s + 14, 41, role=r, label=('H = ⟨τ⟩ : 2' if k == 0 else '2'))
text(ax, 44, 26, 'indice [G:H] = 6/2 = 3', 'varie', 'm')
text(ax, 44, 18, '= [ℚ(r):ℚ] = 3', 'varie', 'm')
text(ax, 44, 8, 'Inv⟨τ⟩ = ℚ(r)', 'resultat', 'l', weight='bold')
save(fig, '63-149')
