import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$D_4$ : $8=1+1+2+2+2$', 'sujet', 'm')
x = 8; w = 9.5
sizes = [1, 1, 2, 2, 2]
x0s = []
for n in sizes:
    x0s.append(x); box(ax, x, 52, w * n - 1, 9, 'fixe' if n == 1 else 'varie', label=str(n)); x += w * n + 0
brace(ax, 8, x - 1, 52, 'encre', label='5 classes, 8 éléments')
arrow(ax, (x0s[4] + w, 46), (x0s[4] + w, 38), 'varie')
text(ax, 84, 33, r'classe de 2 : $8/2=4$', 'varie', 's', ha='right')
for i in range(8): box(ax, 8 + i * 9.5, 14, 9, 9, 'sujet' if i < 4 else 'fixe', r=0.6)
brace(ax, 8, 8 + 3 * 9.5 + 9, 14, 'sujet', label=r'$C$ : 4 éléments')
text(ax, 44, 3, r'$p=2$ divise 4 : premier cas', 'resultat', 's')
save(fig, '50-143')
