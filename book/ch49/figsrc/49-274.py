import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
groups = [(['1'],'resultat'), ([r'$r^2$'],'resultat'), ([r'$r$',r'$r^3$'],'sujet'), ([r'$s$',r'$r^2s$'],'sujet'), ([r'$rs$',r'$r^3s$'],'sujet')]
x = 2.0
for els, role in groups:
    w = 10 if len(els)==1 else 18
    box(ax, x, 18, w, 12, role)
    for i, l in enumerate(els):
        disc(ax, x + (w/2 if len(els)==1 else 5.2+i*7.6), 24, 3.3, role, label=l, size='s')
    text(ax, x+w/2, 14, str(len(els)), role, 'm')
    x += w + 2.5
brace(ax, 2, 22.5, 36, 'resultat', label='centre', down=False)
text(ax, 44, 6, '8 = 1 + 1 + 2 + 2 + 2', 'sujet', 'l')
save(fig, '49-274')
