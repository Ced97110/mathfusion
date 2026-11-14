import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
bw = 16.5; x0 = (W - 4 * bw) / 2
def bar(y, a, b, role, lab):
    for i in range(a, b):
        box(ax, x0 + i * bw, y - 4.5, bw, 9, role, label='2', size='m')
    text(ax, x0, y + 8, lab, role, 's', ha='left')
bar(48, 0, 4, 'sujet', r'$|G|$ = 8')
bar(30, 0, 3, 'varie', 'somme des termes = 6')
bar(12, 3, 4, 'resultat', r'$|C|$ = 8 − 6 = 2')
save(fig, '49-188')
