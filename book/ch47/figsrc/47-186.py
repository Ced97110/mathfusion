import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 48, 'on garde les cases à inverse', 'sujet', 'm')
keep = {1, 3, 7, 9}
for k in range(10):
    x = 6 + k * 7.8
    if k in keep:
        box(ax, x, 30, 7.6, 8, 'sujet', label=str(k), size='s')
        arrow(ax, (x + 3.8, 29.5), (x + 3.8, 17), 'sujet')
    else:
        box(ax, x, 30, 7.6, 8, 'fixe', fill=False, dash=True, label=str(k), size='s')
box(ax, 10, 4, 76, 13, 'sujet', label=r'$U(10)=\{1,\,3,\,7,\,9\}$')
save(fig, '47-186')
