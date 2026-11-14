import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
cx, bw, bh = 28, 34, 10
ys = [86, 62, 38, 14]
items = [(r'$\bar{9}+\overline{100}$', 'fixe'), (r'$\bar{9}+\bar{4}$', 'sujet'),
         (r'$\overline{13}$', 'varie'), (r'$\bar{1}$', 'resultat')]
caps = [r'$100=8\times12+4$', r'$9+4=13$', r'$13=12+1$']
for (s, role), y in zip(items, ys):
    box(ax, cx - bw / 2, y - bh / 2, bw, bh, role, label=s, size='l')
for k, cap in enumerate(caps):
    arrow(ax, (cx, ys[k] - bh / 2 - 0.5), (cx, ys[k + 1] + bh / 2 + 0.5), 'encre')
    text(ax, cx + 6, (ys[k] + ys[k + 1]) / 2, cap, 'encre', 'm', ha='left')
save(fig, '43-125')
