import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 48, r'un quaternion $\in \mathbb{H}$', 'sujet', 'm', weight='bold')
vals = ['2', '3', r'$-1$', '4']; base = ['1', r'$i$', r'$j$', r'$k$']
for k in range(4):
    x = 6 + k * 20
    box(ax, x, 28, 14, 9, 'varie', label=vals[k], size='l')
    text(ax, x + 7, 24, 'devant', 'fixe', 's')
    box(ax, x, 11, 14, 9, 'sujet', label=base[k], size='l')
brace(ax, 6, 74, 9, 'sujet', '4 nombres réels : dimension 4', depth=1.6)
save(fig, '76-027')
