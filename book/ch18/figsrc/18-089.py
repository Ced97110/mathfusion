import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'carrés de nombres entiers fois x', 'fixe', 's')
for i, (a, b) in enumerate([(r'$x^2$', r'$(1x)^2$'), (r'$4x^2$', r'$(2x)^2$'), (r'$9x^2$', r'$(3x)^2$')]):
    xc = 18 + i * 26
    box(ax, xc - 11, 44, 22, 11, 'sujet', label=a)
    text(ax, xc, 38, b, 'sujet', 's')
box(ax, 28, 8, 32, 14, 'limite', label=r'$3x^2$', dash=True)
text(ax, 44, 28, 'absent de la liste', 'limite', 's')
save(fig, '18-089')
