import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$B(2e+f,\ e+f)$', 'sujet', 'l')
terms = [(r'$2B(e,e)$', 'fixe', '0'), (r'$2B(e,f)$', 'sujet', '2'), (r'$B(f,e)$', 'sujet', r'$-1$'), (r'$B(f,f)$', 'fixe', '0')]
w, g = 19, 3
for i, (lab, role, val) in enumerate(terms):
    x = 2 + i * (w + g)
    box(ax, x, 44, w, 10, role, label=lab, size='s')
    arrow(ax, (x + w / 2, 43.5), (x + w / 2, 33), role)
    box(ax, x + 3, 22, w - 6, 10, role, label=val)
    arrow(ax, (44, 63), (x + w / 2, 55), 'sujet')
text(ax, 44, 68, 'on développe', 'sujet', 's')
text(ax, 22, 38.5, r'$B$ alternée', 'fixe', 's')
box(ax, 22, 3, 44, 11, 'resultat', label=r'$0+2-1+0=1$')
for i in range(4):
    x = 2 + i * (w + g)
    arrow(ax, (x + w / 2, 21.5), (44, 14.5), 'resultat', lw=0.6)
save(fig, '75-067')
