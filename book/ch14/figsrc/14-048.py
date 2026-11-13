import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
xs = [22, 44, 66]; labs = ['3', r'$a$', r'$b$']; res = [r'$3^2 = 9$', r'$a^2$', r'$b^2$']; roles = ['varie', 'sujet', 'sujet']
for x, l, r, ro in zip(xs, labs, res, roles):
    box(ax, x - 7, 59, 14, 10, ro, label=l, size='l')
    arrow(ax, (x, 58.5), (x, 44.5), ro)
    text(ax, x + 2, 51.5, 'exposant 2', ro, 's', ha='left')
    box(ax, x - 9, 33, 18, 10, ro, label=r)
brace(ax, 15, 73, 70, 'fixe', label=r'$(3ab)^2$ : 3 facteurs', down=False)
brace(ax, 13, 75, 32, 'fixe')
box(ax, 12, 8, 64, 12, 'resultat', label=r'$(3ab)^2 = 9a^2b^2$', size='l')
save(fig, '14-048')
