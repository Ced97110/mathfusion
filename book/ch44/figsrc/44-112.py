import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def pair(y, a, b, role, lab):
    text(ax, 2, y + 4, lab, role, 's', ha='left')
    box(ax, 50, y, 15, 8, role, label=a)
    box(ax, 70, y, 15, 8, role, label=b)
    arrow(ax, (65, y + 4), (70, y + 4), role)
pair(40, r'$\tau_1$', r'$\sigma$', 'varie', r'on fait : $\tau_1$ puis $\sigma$')
pair(22, r'$\sigma^{-1}$', r'$\tau_1^{-1}$', 'resultat', 'on défait : ordre inversé')
pair(4, r'$\tau_1^{-1}$', r'$\sigma^{-1}$', 'limite', 'même ordre : faux')
save(fig, '44-112')
