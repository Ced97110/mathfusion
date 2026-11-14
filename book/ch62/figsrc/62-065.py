import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$f=x^2-2$ sur ℚ, $n=2$', 'encre', 'm')
X0, CW = 3, 13.5
def bar(y, n):
    for i in range(n):
        role = 'sujet' if i < 2 else 'limite'
        box(ax, X0 + i * CW, y, CW - 1, 11, role, label=str(i + 1))
bar(48, 2)
bar(20, 4)
text(ax, 3, 63, 'ℚ(√2) : fabriqué avec les racines seules', 'sujet', 's', ha='left')
text(ax, 3, 43, r'degré 2 $\leq$ $2!=2$ : sous la borne', 'resultat', 's', ha='left')
text(ax, 3, 35, 'ℚ(⁴√2) : plus gros que les racines seules', 'sujet', 's', ha='left')
text(ax, 3, 14, r'degré 4 $>$ $2!$ : la borne tombe', 'limite', 's', ha='left')
text(ax, 60, 53.5, '1 case = 1 de degré', 'fixe', 's', ha='left')
x = X0 + 2 * CW - 0.5
line(ax, [(x, 19), (x, 32)], 'fixe', dash=True)
line(ax, [(x, 47), (x, 60)], 'fixe', dash=True)
text(ax, x, 70, r'borne $2!=2$ (traits pointillés)', 'fixe', 's')
save(fig, '62-065')
