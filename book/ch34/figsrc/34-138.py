import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$\theta=60^\circ,\ \cos\theta=0{,}5$', 'sujet', 'm')
f = numberline(ax, 12, 70, 10, -1, 2, step=1, arrow_right=False, size='s')
def bar(x0v, x1v, y, role):
    a, b = sorted((f(x0v), f(x1v)))
    box(ax, a, y, b - a, 8, role)
bar(0, 0.5, 40, 'varie'); text(ax, f(0.5) + 2, 44, r'$4\cos^3\theta=0{,}5$', 'varie', 's', ha='left')
bar(0, 1.5, 28, 'fixe'); text(ax, f(0.75), 32, r'$3\cos\theta=1{,}5$', 'fixe', 's')
bar(0, -1, 16, 'resultat'); text(ax, f(0) + 2, 20, r'$0{,}5-1{,}5=-1=\cos 180^\circ$', 'resultat', 's', ha='left')
save(fig, '34-138')
