import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 8, 28, 'det', 'encre', 'l')
vals = [['2', '1'], ['0', '2']]
roles = [['sujet', 'autre'], ['autre', 'sujet']]
for i in range(2):
    for j in range(2):
        box(ax, 18 + 12 * j, 28 - 11 * i - 4, 11, 10, roles[i][j], label=vals[i][j], size='l', r=0.4)
for xe, d in ((15.5, 1), (44.5, -1)):
    line(ax, [(xe + d * 1.5, 12), (xe, 12), (xe, 35), (xe + d * 1.5, 35)], 'encre', lw=0.8)
text(ax, 68, 40, '2 × 2 = 4', 'sujet', 'm')
text(ax, 68, 28, '1 × 0 = 0', 'autre', 'm')
text(ax, 68, 14, '4 − 0 = 4', 'resultat', 'l', weight='bold')
save(fig, '60-085')
