import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ly = 50
f = numberline(ax, 8, 56, ly, 0, 3, arrow_right=False)
disc(ax, f(1), ly + 5, 2.8, 'sujet', label=r'$r_1$', size='s')
disc(ax, f(2), ly + 5, 2.8, 'sujet', label=r'$r_2$', size='s')
arrow(ax, (f(2), ly + 11), (f(1), ly + 11), 'varie')
text(ax, (f(1) + f(2)) / 2, ly + 15, r'$r_1-r_2=-1$', 'varie', 's')
u = f(1) - f(0)
poly(ax, [(f(1), ly - 8 - u), (f(2), ly - 8 - u), (f(2), ly - 8), (f(1), ly - 8)], 'sujet')
text(ax, (f(1) + f(2)) / 2, ly - 8 - u / 2, '$(r_1-r_2)^2$\n$=1$', 'sujet', 's')
for k, (y, role, s) in enumerate([(36, 'resultat', r'$b^2-4ac=1$'), (24, 'autre', r'$Res(f,f′)=-1$'),
                                  (12, 'fixe', r'$-a\times1=-1$ ($a=1$)')]):
    box(ax, 48, y, 38, 9, role, label=s, size='s')
arrow(ax, (f(2) + 1, ly - 8 - u / 2), (47, 40.5), 'resultat')
save(fig, '70-058')
