import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
groups = [(2, 1, r'$x+2$', 'autre', 'simple\n$k=1$'), (19, 2, r'$x-1$', 'sujet', 'double\n$k=2$'), (48, 3, r'$x-1$', 'sujet', 'triple\n$k=3$')]
w, gap = 11.0, 1.5
for x0, n, lab, role, cap in groups:
    for i in range(n):
        box(ax, x0 + i * (w + gap), 28, w, 9, role, label=lab, size='s')
    text(ax, x0 + (n * w + (n - 1) * gap) / 2, 16, cap, role, 's')
brace(ax, 19, 48 + 3 * w + 2 * gap, 38, 'sujet', label=r'racine multiple ($k>1$)', down=False)
save(fig, '62-088')
