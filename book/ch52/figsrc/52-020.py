import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(62)
for i, (a, b, s, role, note) in enumerate([(11, 3, r'$11-3=8=2\times4$', 'resultat', 'même couleur'),
                                      (10, 3, r'$10-3=7$', 'limite', 'couleurs différentes')]):
    y = 46 - 26 * i
    disc(ax, 10, y, 4, CL[a % 4], label=str(a), size='m')
    disc(ax, 28, y, 4, CL[b % 4], label=str(b), size='m')
    line(ax, [(14.5, y), (23.5, y)], role, lw=1.2)
    text(ax, 19, y - 8, note, role, 's')
    box(ax, 40, y - 6, 46, 12, role, label=s, size='m')
    text(ax, 63, y + 10, 'multiple de 4' if i == 0 else 'pas un multiple de 4', role, 's')
save(fig, '52-020')
