import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
S = [(r'$\frac{-4+\sqrt{136}}{2}$','sujet'), (r'$\sqrt{136}=2\sqrt{34}$','fixe'), (r'$\frac{-4+2\sqrt{34}}{2}$','fixe'), (r'$-2+\sqrt{34}$','resultat')]
ys = [80, 56, 32, 8]
for (t, r), y in zip(S, ys): box(ax, 8, y, 46, 14, r, label=t, size='l')
labs = ['136 = 4 × 34', 'on remplace', 'on divise par 2']
for i in range(3):
    arrow(ax, (31, ys[i]-0.5), (31, ys[i+1]+14.5), 'varie')
    text(ax, 35, (ys[i]+ys[i+1]+14)/2, labs[i], 'varie', 's', ha='left')
box(ax, 58, 8, 28, 14, 'fixe', label=r'$\approx3{,}83$', size='m'); text(ax, 72, 26, 'approximation', 'fixe', 's')
text(ax, 72, 4, '', 'fixe', 's')
save(fig, '23-060')
