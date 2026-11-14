import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x = [2, 1, 4]
names = ['riz pur', 'lentilles pur', 'sel pur']
comps = ['(2, 0, 0)', '(0, 1, 0)', '(0, 0, 4)']
assert [(x[0], 0, 0), (0, x[1], 0), (0, 0, x[2])] == [(2, 0, 0), (0, 1, 0), (0, 0, 4)]
roles = ['sujet', 'sujet', 'sujet']
for k in range(3):
    xc = 4 + k * 28
    box(ax, xc, 44, 22, 10, roles[k], label=r'$M_%d$' % (k + 1))
    text(ax, xc + 11, 58, names[k], roles[k], 's')
    arrow(ax, (xc + 11, 44), (xc + 11, 36), 'fixe', lw=0.8)
    box(ax, xc, 25, 22, 10, roles[k], label=comps[k], size='s')
    arrow(ax, (xc + 11, 25), (34 + 10 * k, 13.3), 'resultat', lw=0.9)
    if k < 2: text(ax, xc + 25, 49, r'$\oplus$', 'encre', 'xl')
box(ax, 30, 3, 28, 10, 'resultat', label='(2, 1, 4)', size='s')
text(ax, 62, 8, 'une seule façon', 'resultat', 's', ha='left')
save(fig, '58-057')
