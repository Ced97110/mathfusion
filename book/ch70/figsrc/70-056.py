import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 14, 62, 16, -2, 2, arrow_right=False)
y = 25
arrow(ax, (f(0), y), (f(1), y), 'sujet', lw=1.6)
arrow(ax, (f(0), y), (f(-1), y), 'autre', lw=1.6)
text(ax, f(0) + 1, y + 4, r'$b^2-4ac=1$', 'sujet', 's', ha='left')
text(ax, f(0) - 1, y + 4, r'$Res(f,f′)=-1$', 'autre', 's', ha='right')
arrow(ax, (f(1), y + 12), (f(-1), y + 12), 'varie', curve=0.35)
text(ax, f(0), 46, r'on multiplie par $-a=-1$', 'varie', 's')
text(ax, f(0), 6, r'nuls en même temps', 'resultat', 's')
save(fig, '70-056')
