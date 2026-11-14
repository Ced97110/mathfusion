import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
bw, g, x0 = 17.5, 2.0, 7.0
text(ax, 44, 85, r'$x$ = quart de tour', 'sujet', 'm')
for i, l in enumerate(['1', '¼', '½', '¾']):
    box(ax, x0 + i * (bw + g), 70, bw, 9, 'sujet', label=l, size='s')
brace(ax, x0, x0 + 4 * bw + 3 * g, 68.5, 'sujet', label=r'$m=4$ éléments dans $\langle x\rangle$', down=True)
text(ax, 44, 56, r'$n=8$ éléments : $8=4\times2$', 'autre', 'm')
for r in range(2):
    for i in range(4):
        box(ax, x0 + i * (bw + g), 36 - r * 11 + 6, bw, 9, 'autre' if r == 0 else 'varie', label='', size='s')
text(ax, 44, 24, r'2 paquets de $m$ : $n=m\times r$', 'varie', 's')
text(ax, 44, 12, r'$x^{8}=(x^{4})^{2}=1$', 'resultat', 'l')
save(fig, '47-083')
