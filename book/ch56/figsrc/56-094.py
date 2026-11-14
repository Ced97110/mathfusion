import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
f = lambda v: 48 + v * 2.7
mult3 = range(-12, 13, 3)
# bloc 1 : 3 | 12
text(ax, 44, 104, '3 ∣ 12 : (12) ⊆ (3)', 'encre', 'm')
text(ax, 2, 95, '(3)', 'autre', 's', ha='left')
text(ax, 2, 85, '(12)', 'sujet', 's', ha='left')
for v in mult3:
    disc(ax, f(v), 95, 1.0, 'autre')
    if v % 12 == 0:
        disc(ax, f(v), 85, 1.0, 'sujet')
        line(ax, [(f(v), 86.2), (f(v), 93.8)], 'fixe', lw=0.6, dash=True)
# bloc 2 : 3 ~ -3
text(ax, 44, 70, '3 ∼ −3 : (3) = (−3)', 'encre', 'm')
text(ax, 2, 61, '(3)', 'autre', 's', ha='left')
text(ax, 2, 51, '(−3)', 'sujet', 's', ha='left')
for v in mult3:
    disc(ax, f(v), 61, 1.0, 'autre')
    disc(ax, f(v), 51, 1.0, 'sujet')
    line(ax, [(f(v), 52.2), (f(v), 59.8)], 'resultat', lw=0.8)
# bloc 3 : -1 unité
text(ax, 44, 36, '−1 est une unité : (−1) = ℤ', 'encre', 'm')
text(ax, 2, 26, '(−1)', 'resultat', 's', ha='left')
for v in range(-12, 13):
    disc(ax, f(v), 26, 0.8, 'resultat')
save(fig, '56-094')
