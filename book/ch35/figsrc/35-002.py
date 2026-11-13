import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
base, k = 14, 5
def bar(x, h, role):
    poly(ax, [(x - 7, base), (x + 7, base), (x + 7, base + h), (x - 7, base + h)], role)
bar(20, 4 * k, 'varie'); bar(44, 4.95 * k, 'resultat'); bar(68, 3 * k, 'sujet')
text(ax, 20, base + 4 * k + 3, '0 + 4 = 4', 'encre', 's')
text(ax, 44, base + 4.95 * k + 3, '≈ 4,95', 'encre', 's')
text(ax, 68, base + 3 * k + 3, '3 + 0 = 3', 'encre', 's')
for x, s in ((20, '0°'), (44, '45°'), (68, '90°')): text(ax, x, 10, s, 'fixe', 's')
line(ax, [(6, base + 7 * k), (82, base + 7 * k)], 'limite', 1.0, True)
text(ax, 44, base + 7 * k + 4, '7 = 3 + 4 : jamais atteint', 'limite', 's')
line(ax, [(6, base), (82, base)], 'fixe', 0.8)
text(ax, 18, 4, 'premier son', 'sujet', 's'); text(ax, 46, 4, 'second son', 'varie', 's'); text(ax, 73, 4, 'total', 'resultat', 's')
save(fig, '35-002')
