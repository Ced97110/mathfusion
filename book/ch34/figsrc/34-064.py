import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
f = lambda v: 8 + 70 * v
text(ax, 4, 64, 'A = 45°, B = 30°', 'encre', 's', ha='left')
box(ax, f(0), 50, 0.6124 * 70, 7, 'sujet', label='cos A cos B = 0,6124', size='s')
box(ax, f(0.6124), 41, 0.3536 * 70, 7, 'varie', label='+ 0,3536', size='s')
text(ax, f(0.6124) - 2, 44.5, 'sin A sin B', 'varie', 's', ha='right')
box(ax, f(0), 32, 0.9659 * 70, 7, 'resultat', label='cos 15° = 0,9659', size='s')
text(ax, 4, 25, 'A = B = 45° : A − B = 0°', 'encre', 's', ha='left')
box(ax, f(0), 13, 35, 7, 'sujet', label=r'$\cos^2 A = 0{,}5$', size='s')
box(ax, f(0.5), 13, 35, 7, 'varie', label=r'$\sin^2 A = 0{,}5$', size='s')
text(ax, f(1) + 2, 16.5, '= 1', 'resultat', 's', ha='left')
numberline(ax, f(0), f(1), 6, 0, 1, 0.25, every=2, arrow_right=False)
save(fig, '34-064')
