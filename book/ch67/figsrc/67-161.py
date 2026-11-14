import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$x\in\mathbb{F}_3=\{0,1,2\}$', 'sujet')
vals = [(0, r'$0^2+1=1$'), (1, r'$1^2+1=2$'), (2, r'$2^2+1=5=2$')]
for i, (x, form) in enumerate(vals):
    cx = 16 + i * 28
    disc(ax, cx, 50, 5.5, 'sujet', label=str(x))
    arrow(ax, (cx, 44.5), (cx, 36.8), 'varie')
    text(ax, cx + 2.5, 40.7, r'$x^2+1$', 'varie', 's', ha='left')
    box(ax, cx - 13, 25, 26, 11, 'fixe', label=form)
box(ax, 14, 6, 60, 11, 'resultat', label='aucune valeur nulle')
save(fig, '67-161')
