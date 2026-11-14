import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
bw = 18; xs = [4 + i * (bw + 2) for i in range(4)]
text(ax, 4, 92, r'$x=a+bi+cj+dk$', 'sujet', 'm', ha='left')
for i, l in enumerate([r'$1$', r'$2i$', r'$3j$', r'$4k$']):
    box(ax, xs[i], 74, bw, 10, 'sujet', label=l)
for i in range(4):
    arrow(ax, (xs[i] + bw / 2, 72.5), (xs[i] + bw / 2, 60), 'fixe' if i == 0 else 'varie', lw=1.4)
for i, l in enumerate([r'$1$', r'$-2i$', r'$-3j$', r'$-4k$']):
    box(ax, xs[i], 46, bw, 10, 'fixe' if i == 0 else 'varie', label=l)
brace(ax, xs[0], xs[0] + bw, 44, 'fixe', 'ne change pas')
brace(ax, xs[1], xs[3] + bw, 44, 'varie', 'signes changés')
text(ax, 4, 31, r'$\bar{x}=a-bi-cj-dk$', 'varie', 'm', ha='left')
box(ax, 3, 6, 40, 14, 'resultat', label=r'$x+\bar{x}=2$')
box(ax, 47, 6, 38, 14, 'resultat', label=r'$x\bar{x}=30$')
save(fig, '78-084')
