import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def frac(ax, x, w, num, den, role_num, role_den, size='l'):
    text(ax, x + w / 2, 41, num, role_num, size)
    line(ax, [(x, 36), (x + w, 36)], role_num, lw=0.9)
    box(ax, x, 24, w, 10, role_den, label=den, size=size)

fig, ax = canvas(56)
text(ax, 44, 51, r'on multiplie haut et bas par $\sqrt{6}$', 'varie', 's')
frac(ax, 3, 32, '3', r'$4+\sqrt{6}$', 'fixe', 'sujet')
frac(ax, 53, 32, r'$3\sqrt{6}$', r'$4\sqrt{6}+6$', 'fixe', 'fixe')
arrow(ax, (38, 29), (50, 29), 'varie')
text(ax, 44, 34, r'$\times\sqrt{6}$', 'varie', 's')
brace(ax, 53, 85, 22, 'varie', label='le bas a encore un radical')
text(ax, 44, 8, 'une somme : ça ne suffit pas', 'varie', 's')
save(fig, '22-088')
