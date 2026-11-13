import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
data = [(10, {1, 3, 7, 9}, r'10 heures : $\varphi(10)=4$'), (7, set(range(1, 7)), r'7 heures : $\varphi(7)=6$'),
        (12, {1, 5, 7, 11}, r'12 heures : $\varphi(12)=4$')]
for r, (n, inv, lab) in enumerate(data):
    y = 50 - r * 20
    text(ax, 6, y + 12, lab, 'encre', 'm', ha='left')
    for k in range(n):
        box(ax, 6.2 + k * 6.3, y, 6, 6, 'sujet' if k in inv else 'fixe', r=0.5)
text(ax, 44, 3, 'bleu : case avec inverse', 'sujet', 's')
save(fig, '47-187')
