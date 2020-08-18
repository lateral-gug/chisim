import numpy as np
import matplotlib.pyplot as plt

gdl = 50  #degrees of freedom
campione = 10**7  #generated points
colonne = 1000  #number columns of the plotted histogram

x = np.random.chisquare(gdl,campione)
plt.hist(x, colonne, color='red', density=True, histtype='step', label='$\chi^2$ a %.0f g.d.l.'%(gdl))

y = np.random.normal(gdl,np.sqrt(2*gdl),campione)
plt.hist(y, colonne, color='black', density=True, histtype='step', label='Gaussiana associata')

plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.grid(linestyle=':')
plt.legend(loc='upper right', shadow=True)

print('\n Chi quadro: %.3f +- %.3f'%(np.mean(x),np.std(x)))
print('\n Variabile Gaussiana: %.3f +- %.3f'%(np.mean(y),np.std(y)))

plt.show()
