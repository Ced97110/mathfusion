import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'exposant e = 3 : le chiffré est m³', 'encre', 'm')
xs = [14, 44, 74]
msg = ['0', '1', '2']
chi = ['0', '1', '8']
text(ax, 3, 42, 'm', 'sujet', 'm', ha='left')
text(ax, 3, 22, 'c', 'autre', 'm', ha='left')
for x, a, b in zip(xs, msg, chi):
    same = a == b
    box(ax, x - 7, 37, 14, 10, 'fixe' if same else 'sujet', label=a, size='l')
    arrow(ax, (x, 37), (x, 29), 'fixe' if same else 'varie')
    box(ax, x - 7, 19, 14, 10, 'fixe' if same else 'varie', label=b, size='l')
brace(ax, 7, 51, 16, 'fixe', 'ne bougent pas', size='s')
brace(ax, 67, 81, 16, 'varie', 'change', size='s')
text(ax, 44, 3, 'l’espion lit 0 ou 1 : c’est m', 'encre', 's')
save(fig, '53-174')
