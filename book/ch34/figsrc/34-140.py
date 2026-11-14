import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 70, 50, 0, 180, step=30, every=3, arrow_right=False, size='s')
disc(ax, f(30), 50, 1.6, 'sujet'); disc(ax, f(90), 50, 1.6, 'resultat')
text(ax, f(30), 56, r'$\theta=30^\circ$', 'sujet', 's'); text(ax, f(90) + 5, 56, r'$3\theta=90^\circ$', 'resultat', 's')
arrow(ax, (f(30) + 2, 52.5), (f(90) - 2, 52.5), 'varie', curve=-0.5)
text(ax, f(60), 62.5, r'$\times 3$', 'varie', 's')
for i, (calc, known) in enumerate((('cos : 2,598 − 2,598 = 0', r'$\cos 90^\circ=0$'), ('sin : 1,5 − 0,5 = 1', r'$\sin 90^\circ=1$'))):
    y = 22 - i * 17
    box(ax, 2, y, 46, 12, 'sujet', label=calc, size='s')
    text(ax, 54, y + 6, '=', 'resultat', 'l', weight='bold')
    box(ax, 59, y, 27, 12, 'resultat', label=known, size='s')
save(fig, '34-140')
