import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$\varphi$ : $a+bi\ \mapsto\ a-bi$', 'varie', 'l')
rows = {0: [r'$0$', r'$1$', r'$2$'],
        1: [r'$i$', r'$1+i$', r'$2+i$'],
        2: [r'$2i$', r'$1+2i$', r'$2+2i$']}
ys = {0: 14, 1: 34, 2: 53}
for b, labs in rows.items():
    for a, s in enumerate(labs):
        role = 'resultat' if b == 0 else 'sujet'
        if b > 0 and a == 1: role = 'varie'
        box(ax, 18 + a * 17.5, ys[b], 16, 11, role, label=s)
for a in range(3):
    cx = 18 + a * 17.5 + 8
    arrow(ax, (cx, 45.4), (cx, 52.6), 'varie', both=True)
text(ax, 9, 19.5, 'fixés', 'resultat', 's')
text(ax, 9, 49, 'échangés', 'varie', 's')
text(ax, 44, 6, r'$(1+i)^3=1-i=1+2i$', 'varie')
save(fig, '67-164')
