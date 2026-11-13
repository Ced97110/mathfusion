import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cols = [['∅'], ['1', '2', '3'], ['12', '13', '23'], ['123']]
cxs = [12, 32, 52, 72]
for cx, items in zip(cxs, cols):
    for k, it in enumerate(items):
        box(ax, cx - 9, 45 - k * 11, 18, 9, 'sujet', label=it)
    text(ax, cx, 17, str(len(items)), 'resultat', 'l', weight='bold')
text(ax, 44, 7, r'$1+3+3+1=8=2^3$', 'resultat', 'l')
save(fig, '76-068')
