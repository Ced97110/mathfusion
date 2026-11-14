import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$G^{\prime}$ : engendré par les commutateurs', 'encre', 's')
x0, W = 6, 76
data = [(48, r'$G$ abélien : $G^{\prime}=\{e\}$', 1 / 24 * 0 + 0.012),
        (30, r'$S_3$ (6) : $G^{\prime}=A_3$ (3)', 3 / 6),
        (12, r'très peu commutatif : $G^{\prime}=G$', 1.0)]
for y, lab, frac in data:
    text(ax, 44, y + 12.5, lab, 'encre', 's')
    box(ax, x0, y, W, 8, 'fixe', fill=False)
    box(ax, x0, y, max(W * frac, 1.6), 8, 'sujet', r=0.5)
text(ax, 44, 4, r'bleu : part de $G$ couverte par $G^{\prime}$', 'sujet', 's')
save(fig, '64-063')
