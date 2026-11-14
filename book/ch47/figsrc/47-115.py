import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
R = ['sujet', 'varie', 'resultat']
labs = [r'$\bar{0}=3\mathbb{Z}$', r'$\bar{1}=1+3\mathbb{Z}$', r'$\bar{2}=2+3\mathbb{Z}$']
els = ['…, −3, 0, 3, 6, …', '…, −2, 1, 4, 7, …', '…, −1, 2, 5, 8, …']
for k in range(3):
    y = 52 - 24 * k
    box(ax, 2, y, 36, 14, R[k], label=labs[k], size='m')
    box(ax, 42, y, 44, 14, R[k], fill=False, label=els[k], size='m')
    if k < 2:
        arrow(ax, (64, y - 0.5), (64, y - 9.5), 'varie')
        text(ax, 68, y - 5, '+1', 'varie', 'm', ha='left')
save(fig, '47-115')
