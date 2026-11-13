import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$\frac{3}{x}+\frac{4x}{x-1}=\frac{4x^2+x+5}{x^2-x}$', 'sujet', 'm')
steps = ['valeurs interdites', 'PPCM', 'multiplier chaque terme', 'résoudre', 'vérifier']
y0 = 4
ys = [y0 + (4 - i) * 11.5 for i in range(5)]
for i, (s, y) in enumerate(zip(steps, ys)):
    box(ax, 4, y, 44, 8, 'resultat' if i == 4 else 'sujet', label=s, size='s')
    if i < 4: arrow(ax, (26, y), (26, ys[i + 1] + 8), 'varie')
text(ax, 68, ys[3] + 4, r'$x=4$', 'varie', 'm')
text(ax, 68, ys[4] + 4, r'$\frac{73}{12}=\frac{73}{12}$', 'resultat', 'm')
save(fig, '21-118')
