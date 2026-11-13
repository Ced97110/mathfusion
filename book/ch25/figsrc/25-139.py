import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$\tan x = 1$', 'sujet', 'l')
f = numberline(ax, 8, 72, 18, 0, 450, step=90, labels=False)
box(ax, f(0), 14, f(90) - f(0), 8, 'sujet', fill=True, r=0.4, lw=0.4)
for v in (0, 90, 180, 270, 360, 450): text(ax, f(v), 11.8, f'{v}°', 'fixe', 's')
for v, role in ((45, 'sujet'), (225, 'resultat'), (405, 'resultat')):
    disc(ax, f(v), 18, 1.7, role); text(ax, f(v), 25, f'{v}°', role, 's')
arrow(ax, (f(45), 28), (f(225), 28), 'varie', curve=-0.3); arrow(ax, (f(225), 28), (f(405), 28), 'varie', curve=-0.3)
text(ax, f(135), 38, '+ 180°', 'varie', 's'); text(ax, f(315), 38, '+ 180°', 'varie', 's')
text(ax, 80, 18, '…', 'resultat', 'l')
text(ax, f(45), 5, 'seul angle aigu', 'sujet', 's')
save(fig, '25-139')
