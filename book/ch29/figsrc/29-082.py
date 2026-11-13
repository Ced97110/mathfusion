import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 49, r'$A=\frac{1}{2}\,r^2\theta$', 'encre', 'xl')
xs = [3, 32, 61]
labs = ['3 × 3 = 9', '½ × 9 = 4,5', '4,5 × 2 = 9']
roles = ['sujet', 'varie', 'resultat']
caps = ['r au carré', 'la moitié', 'fois θ = 2']
for i in range(3):
    box(ax, xs[i], 26, 24, 10, roles[i], label=labs[i], size='s')
    text(ax, xs[i] + 12, 22, caps[i], roles[i], 's')
for i in range(2):
    arrow(ax, (xs[i] + 24.3, 31), (xs[i + 1] - 0.3, 31), 'encre')
text(ax, 44, 10, 'aire du secteur : 9 cm²', 'resultat', 'm')
save(fig, '29-082')
