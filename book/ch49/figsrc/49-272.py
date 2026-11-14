import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, h = 17, 34, 10
poly(ax, [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)], 'sujet')
for (dx,dy),l in zip([(-h,h),(h,h),(h,-h),(-h,-h)], 'abcd'):
    disc(ax, cx+dx, cy+dy, 2.6, 'sujet', label=l, size='s')
text(ax, cx, cy, '4 fils', 'sujet', 'm')
text(ax, cx, 16, '8 symétries', 'sujet', 'm')
text(ax, cx, 11, 'sur 24 possibles', 'fixe', 's')
text(ax, 62, 53, 'nombres de cycles', 'varie', 'm')
for i, v in enumerate(['16','12','6','10']):
    box(ax, 38+i*12.5, 40, 11, 9, 'varie', label=v)
arrow(ax, (62,39), (62,33), 'fixe')
box(ax, 40, 23, 44, 9, 'sujet', label='total : 76 928')
arrow(ax, (62,22), (62,16), 'varie')
text(ax, 72, 19, r'$\div$ 8', 'varie', 'm')
box(ax, 40, 6, 44, 9, 'resultat', label='9 616 circuits', weight='bold')
save(fig, '49-272')
