import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 8, 46, r'$\mathbb{Z}$', 'sujet', 'xl')
f = numberline(ax, 8, 76, 30, -6, 6, labels=True, arrow_right=True, every=2)
for v in range(-6, 7):
    if v == 0: disc(ax, f(v), 30, 2.6, 'sujet')
    else: disc(ax, f(v), 30, 1.3, 'fixe')
text(ax, f(0), 45, '0 au centre', 'sujet', 's')
arrow(ax, (f(0), 42.5), (f(0), 34), 'sujet')
brace(ax, f(0) + 0.5, f(6), 22, 'varie', '6 pas à droite')
brace(ax, f(-6), f(0) - 0.5, 22, 'varie', '6 pas à gauche')
save(fig, '52-018')
