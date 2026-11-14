import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 2, 25, 24, 14, 'sujet', label=r'$\mathbb{Q}(r)$')
labs = [r'$\varphi_1:\ r\mapsto r$', r'$\varphi_2:\ r\mapsto jr$', r'$\varphi_3:\ r\mapsto j^2r$']
for k, (lab, y) in enumerate(zip(labs, (50, 26, 2))):
    box(ax, 44, y, 42, 14, 'autre', label=lab, size='s')
    arrow(ax, (26.5, 32), (43.5, y + 7), 'varie')
text(ax, 44, 72, r'$\sigma(r)\in\{r,\ jr,\ j^2r\}$', 'fixe', 's')
save(fig, '63-092')
