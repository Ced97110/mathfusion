import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
steps = [(r'$t=3$', 'varie'), (r'$3-2=1$', 'sujet'), (r'$\frac{\pi}{4}\times 1=\frac{\pi}{4}$', 'sujet'),
         (r'$\sin(\frac{\pi}{4})\approx 0{,}7071$', 'sujet'), (r'$20\times 0{,}7071\approx 14{,}14$', 'sujet'),
         (r'$14{,}14+22=36{,}14$', 'resultat')]
for i, (s, ro) in enumerate(steps):
    y = 70 - i * 13
    box(ax, 14, y - 4.5, 60, 9, ro, label=s, size='m')
    if i: arrow(ax, (44, y + 8.5), (44, y + 4.7), 'fixe')
save(fig, '30-138')
