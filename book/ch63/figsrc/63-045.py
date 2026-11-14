import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$\mathrm{Aut}(E)$ , $E=\mathbb{Q}(\sqrt{2},\sqrt{3})$', 'sujet', 'm')
names = ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']
im2 = [r'$\sqrt{2}\mapsto\sqrt{2}$', r'$\sqrt{2}\mapsto-\sqrt{2}$', r'$\sqrt{2}\mapsto\sqrt{2}$', r'$\sqrt{2}\mapsto-\sqrt{2}$']
im3 = [r'$\sqrt{3}\mapsto\sqrt{3}$', r'$\sqrt{3}\mapsto\sqrt{3}$', r'$\sqrt{3}\mapsto-\sqrt{3}$', r'$\sqrt{3}\mapsto-\sqrt{3}$']
ch2 = [False, True, False, True]
ch3 = [False, False, True, True]
for i in range(4):
    x = 2 + 21.5 * i
    box(ax, x, 40, 20, 10, 'sujet', label=names[i])
    box(ax, x, 26, 20, 10, 'varie' if ch2[i] else 'fixe', label=im2[i], size='s')
    box(ax, x, 12, 20, 10, 'varie' if ch3[i] else 'fixe', label=im3[i], size='s')
save(fig, '63-045')
