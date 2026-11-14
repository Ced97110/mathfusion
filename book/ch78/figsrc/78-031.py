import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
sy = ['ℝ', 'ℂ', 'ℍ', '𝕆', '?']
dims = [1, 2, 4, 8, 16]
for i in range(5):
    role = 'resultat' if i < 4 else 'limite'
    box(ax, 4 + 17 * i, 38, 15, 14, role, label=str(dims[i]), size='l')
    text(ax, 4 + 17 * i + 7.5, 57, sy[i] if i < 4 else '5e étage', role, 'm' if i < 4 else 's')
brace(ax, 4, 70, 36, 'resultat', label=r'$|xy| = |x||y|$ conservée')
brace(ax, 72, 87, 36, 'limite', label='perdue')
text(ax, 44, 16, r'ex. dans ℂ : $5 \times 13 = 65$', 'fixe', 's')
text(ax, 44, 10, 'carrés des longueurs', 'fixe', 's')
save(fig, '78-031')
