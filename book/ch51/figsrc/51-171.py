import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'quatre réels, dans cet ordre', 'sujet', 's')
cx = [13, 33, 53, 73]
top = ['2', '5', '0', '3']
terms = [r'$2$', r'$5i$', r'$0j$', r'$3k$']
for i in range(4):
    box(ax, cx[i] - 7, 48, 14, 10, 'sujet', label=top[i], size='l')
    gone = i == 2
    box(ax, cx[i] - 7, 28, 14, 10, 'fixe' if gone else 'varie', label=terms[i], size='l', dash=gone)
    arrow(ax, (cx[i], 48), (cx[i], 38.8), 'fixe' if gone else 'varie')
for i, tx in [(0, 24), (1, 36), (3, 64)]:
    arrow(ax, (cx[i], 28), (tx, 14.8), 'resultat')
text(ax, 53, 22, 'disparaît', 'fixe', 's')
box(ax, 18, 4, 52, 10, 'resultat', label=r'$2+5i+3k$', size='l')
save(fig, '51-171')
