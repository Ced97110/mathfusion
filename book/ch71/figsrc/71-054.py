import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 4, 54, 80, 12, 'sujet', label=r"règle exigée sur $y$ : $B(x,\,y+y') = B(x,y)+B(x,y')$", size='s')
text(ax, 44, 47, 'sans cette règle, un cas : $x=(1,0)$', 'encre', 's')
s = 6.0
for i in range(4): box(ax, 6 + i * (s + 1), 30, s, s, 'varie', r=0.3)
box(ax, 54, 30, s, s, 'sujet', r=0.3); box(ax, 68, 30, s, s, 'autre', r=0.3)
text(ax, 57, 39, r'$B(x,y)$', 'sujet', 's'); text(ax, 71, 39, r"$B(x,y')$", 'autre', 's')
text(ax, 64, 33, '+', 'encre', 'l')
text(ax, 20, 25, r"$B(x,\,y+y')=4$", 'varie', 's')
text(ax, 66, 25, r"$1+1=2$", 'encre', 's')
text(ax, 41, 33, r'$\neq$', 'limite', 'xl')
text(ax, 44, 12, r'les deux membres diffèrent :', 'limite', 's'); text(ax, 44, 6, r"la règle sur $y$ est nécessaire", 'limite', 's')
save(fig, '71-054')
