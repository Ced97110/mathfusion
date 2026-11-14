import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = lambda v: 8 + 100 * v
box(ax, f(0), 46, 61.24, 7, 'sujet', label='sin A cos B = 0,6124', size='s')
box(ax, f(0.2588), 35, 35.36, 7, 'varie', label='− 0,3536', size='s')
text(ax, f(0.2588) - 2, 38.5, 'cos A sin B', 'varie', 's', ha='right')
box(ax, f(0), 24, 25.88, 7, 'resultat', label='0,2588', size='s')
text(ax, f(0.2588) + 2, 27.5, '= sin 15°', 'resultat', 's', ha='left')
numberline(ax, f(0), f(0.7), 14, 0, 0.7, 0.1, every=2)
save(fig, '34-063')
