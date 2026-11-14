import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
f=numberline(ax,14,74,16,-2,2,arrow_right=False)
for a in (-2,-1,1,2):
    h=2*3*a*a; role='varie' if abs(a)==1 else 'sujet'
    poly(ax,[(f(a)-4,16),(f(a)+4,16),(f(a)+4,16+h),(f(a)-4,16+h)],role)
    text(ax,f(a),16+h+3,str(3*a*a),role,'s')
disc(ax,f(0),16,1.8,'resultat'); text(ax,f(0),21,'0','resultat','s')
text(ax,44,32,'seul carré nul','resultat','s')
text(ax,44,52,'isométries : a = 1 ou −1','varie','s')
text(ax,44,61,r'carré de $a\,u$ (c = 3)','encre','m')
save(fig,'72-110')
