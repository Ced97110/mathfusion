import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(46)
vals = ['5,67', '57,29', '572,96', '5 729,58']; angs = ['80°', '89°', '89,9°', '89,99°', '90°']
for i in range(5):
    x = 4 + i * 16.8
    if i < 4: box(ax, x, 16, 14, 9, 'resultat', label=vals[i], size='s')
    else: box(ax, x, 16, 14, 9, 'limite', fill=False, label='rien', size='s', dash=True)
    text(ax, x + 7, 11, angs[i], 'fixe', 's')
brace(ax, 4, 4 + 3 * 16.8 + 14, 29, 'resultat', label='des nombres : on les écrit', down=False)
brace(ax, 4 + 4 * 16.8, 4 + 4 * 16.8 + 14, 29, 'limite', label='aucun nombre', down=False)
save(fig, '25-127')
