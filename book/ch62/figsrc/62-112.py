import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# (1+1)^2 = a^2 + 2ab + b^2 with a = b = 1 ; real numbers 1+2+1 = 4 ; in F2 : 1+0+1 = 0
def panel(x0, role, head, vals, total, other, verdict, vrole):
    text(ax, x0 + 20, 68, head, role, 'm', weight='bold')
    names = [r'$a^2$', r'$2ab$', r'$b^2$']
    for i in range(3):
        r = role if (i != 1) else ('varie' if vals[1] != '0' else 'fixe')
        box(ax, x0 + 1 + i * 13, 46, 12, 15, r, label=names[i] + '\n' + vals[i], size='s')
    text(ax, x0 + 20, 39, total, 'encre', 's')
    text(ax, x0 + 20, 31, other, 'encre', 's')
    box(ax, x0 + 4, 8, 32, 13, vrole, label=verdict, size='m')
panel(2, 'sujet', 'dans ℝ', ['1', '2', '1'], r'$(1+1)^2=1+2+1=4$', r'$1^2+1^2=1+1=2$', r'$4\neq2$', 'limite')
panel(46, 'autre', r'dans $\mathbb{F}_2$', ['1', '0', '1'], r'$(1+1)^2=1+0+1=0$', r'$1^2+1^2=1+1=0$', r'$0=0$', 'resultat')
save(fig, '62-112')
