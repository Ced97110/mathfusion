import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$T_{E/F}(1)=1+1+1+1$', 'encre', 'm')
xs = [8, 28, 48, 68]
for x in xs:
    box(ax, x, 36, 12, 9, 'sujet', label='1')
for x in [24, 44, 64]:
    text(ax, x, 40.5, '+', 'encre', 'm')
brace(ax, 8, 40, 34, 'varie', label=r'$1+1=0$')
brace(ax, 48, 80, 34, 'varie', label=r'$1+1=0$')
box(ax, 10, 8, 68, 11, 'resultat', label=r'$4=0$ car $p=2$ divise 4')
save(fig, '67-220')
