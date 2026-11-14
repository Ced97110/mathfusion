import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(46)
for i, (a, role, l1, l2) in enumerate((('30°', 'resultat', r'$\cos x\neq 0$', 'deux membres'), ('90°', 'limite', r'$\cos x=0$', 'sans sens'), ('270°', 'limite', r'$\cos x=0$', 'sans sens'))):
    x = 2 + i * 29.5
    lbox(ax, x, 6, 26, 28, role); text(ax, x + 13, 28, a, role, 'l', weight='bold'); text(ax, x + 13, 19, l1, role, 'm'); text(ax, x + 13, 11, l2, role, 's')
text(ax, 15, 40, r'$\approx 1{,}7321$ = $1{,}7321$', 'resultat', 's')
text(ax, 58, 40, 'identité sans sens ici', 'limite', 's')
save(fig, '31-132')
