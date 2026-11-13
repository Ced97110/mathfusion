import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 59, r'$\sin A=3/5$     $\cos A=4/5$', 'sujet', 'l')
forms = [r'$\cos^2A-\sin^2A$', r'$2\cos^2A-1$', r'$1-2\sin^2A$']
nums = [r'$16/25-9/25$', r'$32/25-1$', r'$1-18/25$']
for i, (f, n) in enumerate(zip(forms, nums)):
    y = 38 - i * 16
    box(ax, 2, y, 32, 12, 'sujet', label=f, size='s')
    arrow(ax, (34.5, y + 6), (40.5, y + 6), 'varie')
    box(ax, 41, y, 26, 12, 'fixe', label=n, size='s')
    arrow(ax, (67.5, y + 6), (72.5, y + 6), 'varie')
    box(ax, 73, y, 13, 12, 'resultat', label=r'$7/25$', size='s')
save(fig, '34-129')
