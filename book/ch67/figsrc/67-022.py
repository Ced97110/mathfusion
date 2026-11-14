import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 92, 'corps $\\mathbb{F}_4$ : ordre $4=2^2$\npuissance d’un premier', 'resultat', 's')
for i, l in enumerate(['0', '1', r'$\alpha$', r'$\alpha+1$']):
    box(ax, 8 + i * 19.5, 68, 16, 12, 'resultat', label=l)
text(ax, 44, 57, 'ℤ/6ℤ : ordre $6=2\\times3$\npas une puissance d’un premier', 'limite', 's')
for i in range(6):
    box(ax, 6 + i * 13.2, 38, 11, 12, 'varie' if i in (2, 3) else 'fixe', label=str(i), size='m')
arrow(ax, (44, 35), (44, 27), 'limite')
box(ax, 8, 8, 72, 18, 'limite', label='$2\\times3=0$ : produit nul\npas un corps', size='s')
save(fig, '67-022')
