import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
vs = [['2', '0', '0'], ['0', '6', '0'], ['0', '0', '0']]
rs = [['sujet', 'fixe', 'fixe'], ['fixe', 'sujet', 'fixe'], ['fixe', 'fixe', 'fixe']]
mat(vs, rs, 28, 8)
for k, lab, role in [(0, 'non nul', 'sujet'), (1, 'non nul', 'sujet'), (2, 'nul', 'fixe')]:
    text(ax, 33 + 11 * k, 46, lab, role, 's')
brace(ax, 28, 49, 50, 'resultat', label=r'$r=2$', down=False, size='m')
save(fig, '59-068')
