import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'G = S₃ : 6 éléments, σ garde j', 'encre', 's')
for i in range(3):
    disc(ax, 10 + 10 * i, 47, 4, role='sujet')
    disc(ax, 54 + 10 * i, 47, 4, role='autre')
brace(ax, 5, 35, 41, role='sujet', label='H = ⟨σ⟩ : 3 éléments')
brace(ax, 49, 79, 41, role='autre', label='l’autre moitié : 3')
text(ax, 44, 26, 'indice [G:H] = 6/3 = 2', 'varie', 'm')
text(ax, 44, 18, '= [ℚ(j):ℚ] = 2', 'varie', 'm')
text(ax, 44, 8, 'Inv⟨σ⟩ = ℚ(j)', 'resultat', 'l', weight='bold')
save(fig, '63-148')
