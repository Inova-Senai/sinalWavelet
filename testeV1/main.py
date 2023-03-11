import ply as ply
import pywt #biblioteca  para wavelets (top)
import numpy as np
import matplotlib.pyplot as plt #lib para plotagem de gráficos

# array unidimensional para sinmular o sinal EEG
sinalEeg = np.array([0.1, 0.5, 0.2, 0.4, 0.8, 0.3, 0.6, 0.9, 0.2, 0.5])

# definindo a wavelet daubechies ordem 4  (tem outros tipos na lib pywt)
wavelet = 'db4' # escolha da wavelet

# aplicando a transformada no sinal (função pywt.wavedec())
coef = pywt.wavedec(sinalEeg, wavelet) #decompoe o sinal em diferentes níveis e coeficientes de detalhe

# visualizando os coeficientes de detalhe em diferentes escalas (função pywt.plotting.plot_wavelets())
figm, ax = ply.subplots(figsize=(12,6))
pywt.plotting.plot_wavelets(coef[:-1], ax=ax)

#a figura vai mostrar os coeficientes de detalhes em diferentes níveis/escalas ao longo do tempo.
