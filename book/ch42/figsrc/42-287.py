import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
def panel(x0, title, before, after, roles):
    text(ax, x0 + 20, 52, title, 'encre', 'm')
    for k, (b, a) in enumerate(zip(before, after)):
        pass
    for k, lab in enumerate(before):
        box(ax, x0 + 14 * k, 33, 12, 9, roles[lab], label=lab, size='m')
    for k, lab in enumerate(after):
        box(ax, x0 + 14 * k, 8, 12, 9, roles[lab], label=lab, size='m')
    arrow(ax, (x0 + 20, 31), (x0 + 20, 19), 'fixe', 1.4)
r1 = {r'$2x$': 'varie', r'$+3$': 'fixe', r'$+4x$': 'varie'}
panel(2, 'polynômes (ch. 15)', [r'$2x$', r'$+3$', r'$+4x$'], [r'$2x$', r'$+4x$', r'$+3$'], r1)
r2 = {r'$A$': 'varie', r'$\cap B$': 'fixe', r"$\cap A'$": 'varie'}
panel(46, 'ensembles', [r'$A$', r'$\cap B$', r"$\cap A'$"], [r'$A$', r"$\cap A'$", r'$\cap B$'], r2)
save(fig, '42-287')
