import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X0, BW, GAP = 24, 19, 1.5
def row(y, items, name, role_name):
    text(ax, 2, y + 4.5, name, role_name, 's', ha='left')
    for k, (s, role) in enumerate(items):
        box(ax, X0 + k * (BW + GAP), y, BW, 9, role, label=s, size='s', r=0.5)
r1 = [('y − 2', 'sujet'), ('y − 1', 'fixe'), ('y + 1', 'autre')]
row(44, r1, r'$f\,g_1$', 'encre')
row(22, r1[::-1], r'$g\,f_1$', 'encre')
for k, s in enumerate([r'$f_1$', r'$h$', r'$g_1$']):
    text(ax, X0 + k * (BW + GAP) + BW / 2, 57, s, r1[k][1], 'm')
text(ax, 54, 35, '=', 'resultat', 'xl')
text(ax, 44, 11, r'$f\,g_1-g\,f_1=0$', 'resultat', 'm')
save(fig, '70-045')
