import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx = [14, 34, 54, 74]
hrs = ['11 h', '12 h', '13 h', '14 h']
val = [r'$\frac{1}{2}$', '1', '2', '4']
ex = [r'$2^{?}$', r'$2^{?}$', r'$2^{1}$', r'$2^{2}$']
for i, x in enumerate(cx):
    known = i >= 2
    text(ax, x, 53, hrs[i], 'fixe', 'm')
    box(ax, x - 7, 33, 14, 12, 'sujet', label=val[i], size='l')
    box(ax, x - 7, 12, 14, 12, 'sujet' if known else 'varie', label=ex[i], size='l', dash=not known)
    arrow(ax, (x, 33), (x, 24.5), 'fixe')
text(ax, 24, 4.5, 'à nommer', 'varie', 's')
text(ax, 64, 4.5, 'déjà écrit', 'sujet', 's')
text(ax, 44, 29, 'valeur', 'fixe', 's') if False else None
save(fig, '14-003')
