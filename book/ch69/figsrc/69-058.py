import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
w, pitch, x0, y = 17, 21, 4, 18
subs = [r'$f_0$', r'$f_1$', r'$f_2$', r'$f_3$']
caps = ['départ', 'dérivée', 'division', 'division']
for k in range(4):
    x = x0 + k * pitch
    box(ax, x, y, w, 12, 'sujet', label=subs[k])
    text(ax, x + w / 2, y - 5, caps[k], 'fixe', 's')
    if k < 3:
        arrow(ax, (x + w + 0.3, y + 6), (x + pitch - 0.3, y + 6), 'varie')
brace(ax, x0, x0 + 3 * pitch + w, y + 13, 'sujet', label=r'$f_0,\ldots,f_s$ avec $s=3$', down=False)
save(fig, '69-058')
