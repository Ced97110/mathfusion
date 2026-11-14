import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$s\mapsto a_0+a_1s+\cdots+a_ns^n$', 'sujet', 'm')
text(ax, 44, 66, r'$s=2$ ; coefficients $1,2,1$', 'varie', 's')
top = [r'$a_0$', r'$a_1s$', r'$a_2s^2$']
low = ['1', r'$2\times2=4$', r'$1\times4=4$']
for x, a, b in zip((4, 32, 60), top, low):
    box(ax, x, 48, 24, 11, 'sujet', label=a)
    box(ax, x, 26, 24, 11, 'fixe', label=b, size='s')
    arrow(ax, (x + 12, 48), (x + 12, 37), 'varie')
box(ax, 14, 4, 60, 13, 'resultat', label=r'$1+4+4=9=0$')
for x0, x1 in ((16, 30), (44, 44), (72, 58)):
    arrow(ax, (x0, 26), (x1, 17), 'resultat')
save(fig, '55-027')
