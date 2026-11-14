import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, 'sur ℝ : aucune racine', 'limite', 's')
text(ax, 66, 64, 'sur ℂ : deux racines', 'resultat', 's')
ay = 34
arrow(ax, (4, ay), (40, ay), 'fixe', lw=0.8)
text(ax, 41.5, ay + 3, 'ℝ', 'fixe', 's')
pts = [(22 + x * 8, ay + (x * x + 1) * 4) for x in [i / 20 * 4 - 2 for i in range(21)]]
line(ax, pts, 'sujet', lw=1.1)
arrow(ax, (48, 36), (85, 36), 'fixe', lw=0.8)
arrow(ax, (66, 18), (66, 56), 'fixe', lw=0.8)
disc(ax, 66, 46, 1.5, 'resultat'); disc(ax, 66, 26, 1.5, 'resultat')
text(ax, 71, 46, 'i', 'resultat', 's'); text(ax, 72, 26, '−i', 'resultat', 's')
box(ax, 4, 4, 80, 11, 'resultat', label=r'$\lambda^2+1=(\lambda-i)(\lambda+i)$')
save(fig, '60-260')
