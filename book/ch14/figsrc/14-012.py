import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
bw, gap = 12, 5.5
A = ['8', '4', '2', '1', r'$\frac{1}{2}$']; B = ['8', '4', '2', '0', '0']
text(ax, 3, 57, 'choix 1 : la règle tient', 'resultat', 'm', ha='left')
text(ax, 3, 29, 'choix 0 : la règle casse', 'limite', 'm', ha='left')
for i in range(5):
    x = 3 + i * (bw + gap)
    box(ax, x, 40, bw, 11, 'sujet' if i < 3 else 'resultat', label=A[i], size='l')
    box(ax, x, 12, bw, 11, 'sujet' if i < 3 else 'limite', label=B[i], size='l')
text(ax, 62, 5.5, '2 ÷ 2 = 1, pas 0', 'limite', 's')
arrow(ax, (3 + 3 * (bw + gap) + 6, 8.5), (3 + 3 * (bw + gap) + 6, 11.5), 'limite') if False else None
save(fig, '14-012')
