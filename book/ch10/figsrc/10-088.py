import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
base, k = 50, 4.5
line(ax, [(4, base), (84, base)], 'fixe'); text(ax, 85, base, '0', 'fixe', 's', ha='left') if False else None
data = [(r'$87\to 90$', 3.4, '+3,4 %', 'varie'), (r'$4\,316\to 4\,000$', -7.3, '−7,3 %', 'varie'), ('produit', -4.1, '−4,1 %', 'resultat')]
for i, (t, v, lab, role) in enumerate(data):
    x = 8 + 26 * i
    text(ax, x + 7, 86, t, role, 's')
    box(ax, x, base if v > 0 else base + v * k, 14, abs(v) * k, role, r=0.3)
    text(ax, x + 7, base + v * k + (2.5 if v > 0 else -2.5), lab, role, 's')
text(ax, 44, 8, 'une hausse ne compense pas la baisse', 'encre', 's')
save(fig, '10-088')
