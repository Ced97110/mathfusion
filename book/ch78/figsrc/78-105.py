import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(4, 'ℍ\nassociatif', 'resultat', '𝕆\nalternatif', 'resultat'), (48, '𝕆\nnon associatif', 'limite', 'dimension 16\nnon alternatif', 'limite')]
for x, a, ra, d, rd in cols:
    box(ax, x, 46, 36, 16, 'sujet', label=a)
    arrow(ax, (x + 18, 45), (x + 18, 30), 'varie')
    text(ax, x + 28, 37.5, 'double', 'varie', 's')
    box(ax, x, 12, 36, 16, rd, label=d)
save(fig, '78-105')
