import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
roles = ['sujet', 'varie', 'autre']; labs = [r'$H$', r'$1+H$', r'$2+H$']
c = 16
for r_ in range(3):
    y = 34 - r_ * 14
    text(ax, 14, y + 5, labs[r_], roles[r_], 'm', ha='right')
    for i in range(4):
        box(ax, 18 + i * c, y, c, 10, roles[r_], label=str(3 * i + r_), size='l', r=0.3)
text(ax, 50, 3, '3 lignes × 4 colonnes = 12 cases', 'encre', 's')
save(fig, '47-010')
