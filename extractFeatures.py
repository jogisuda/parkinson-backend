import hfda
import pywt
import numpy as np


def ShannonEntropySignal(s):
  square = np.square(s)/np.sum(np.square(s))
  return np.sum(-square*np.log2(square))

def RenyiEntropySignal(s, alpha):
  if alpha == 0:
    return np.log2(len(s))
  elif alpha == 1:
    return ShannonEntropySignal(s)
  elif alpha == 2:
    p = np.square(s)/np.sum(np.square(s))
    return np.log2(np.sum(p)**2)

def katz_fd(x):
    """Katz Fractal Dimension.

    Parameters
    ----------
    x : list or np.array
        One dimensional time series.

    Returns
    -------
    kfd : float
        Katz fractal dimension.

    Notes
    -----
    The Katz fractal dimension is defined by:

    .. math:: K = \\frac{\\log_{10}(n)}{\\log_{10}(d/L)+\\log_{10}(n)}

    where :math:`L` is the total length of the time series and :math:`d`
    is the
    `Euclidean distance <https://en.wikipedia.org/wiki/Euclidean_distance>`_
    between the first point in the series and the point that provides the
    furthest distance with respect to the first point.

    Original code from the `mne-features <https://mne.tools/mne-features/>`_
    package by Jean-Baptiste Schiratti and Alexandre Gramfort.

    References
    ----------
    * Esteller, R. et al. (2001). A comparison of waveform fractal
      dimension algorithms. IEEE Transactions on Circuits and Systems I:
      Fundamental Theory and Applications, 48(2), 177-183.

    * Goh, Cindy, et al. "Comparison of fractal dimension algorithms for
      the computation of EEG biomarkers for dementia." 2nd International
      Conference on Computational Intelligence in Medicine and Healthcare
      (CIMED2005). 2005.

    Examples
    --------
    >>> import numpy as np
    >>> from entropy import katz_fd
    >>> np.random.seed(123)
    >>> x = np.random.rand(100)
    >>> print(katz_fd(x))
    5.121395665678078
    """
    x = np.array(x)
    dists = np.abs(np.ediff1d(x))
    ll = dists.sum()
    ln = np.log10(np.divide(ll, dists.mean()))
    aux_d = x - x[0]
    d = np.max(np.abs(aux_d[1:]))
    return np.divide(ln, np.add(ln, np.log10(np.divide(d, ll))))

def extractFeatures(signal):
    '''feature1 = signal[:, 0]
    feature2 = signal[:, 1]
    feature3 = signal[:, 2]'''
    feature4 = signal[:, 0]
    feature5 = signal[:, 1]
    feature6 = signal[:, 2]
    
    '''wp1 = pywt.WaveletPacket(data=feature1, wavelet='db4', mode='smooth')
    wp2 = pywt.WaveletPacket(data=feature2, wavelet='db4', mode='smooth')
    wp3 = pywt.WaveletPacket(data=feature3, wavelet='db4', mode='smooth')'''
    wp4 = pywt.WaveletPacket(data=feature4, wavelet=waveletType, mode='smooth')
    wp5 = pywt.WaveletPacket(data=feature5, wavelet=waveletType, mode='smooth')
    wp6 = pywt.WaveletPacket(data=feature5, wavelet=waveletType, mode='smooth')

    '''entropies = [RenyiEntropySignal(feature1, 1), RenyiEntropySignal(feature2, 1), RenyiEntropySignal(feature3, 1), 
                RenyiEntropySignal(feature4, 1), RenyiEntropySignal(feature5, 1), RenyiEntropySignal(feature6, 1) ]'''
    #entropies = [RenyiEntropySignal(feature4, 0), RenyiEntropySignal(feature5, 0), RenyiEntropySignal(feature6, 0) ]
    entropies = [RenyiEntropySignal(feature4, 1), RenyiEntropySignal(feature5, 1), RenyiEntropySignal(feature6, 1) ]
    #entropies = [RenyiEntropySignal(feature4, 2), RenyiEntropySignal(feature5, 2), RenyiEntropySignal(feature6, 2) ]

    WaveletPacket = []
    #WaveletPacket.extend([wp1])
    '''WaveletPacket.extend([wp1, wp2, wp3, wp4, wp5, wp6])'''

    WaveletPacket.extend([wp4, wp5, wp6])
    
    row = np.array([label], np.float64) #cada vetor de carac., primeiro 0 é a classe (saud)
    row = np.hstack([row, entropies])
    '''
    row = np.append(row, firstMoment)
    row = np.append(row, secondMoment)
    row = np.append(row, thirdMoment)'''

    Nodes = np.empty(0, np.float64) #vetor de nós temporário (para cada nível da tree).

    for level in range(1, levels + 1): #for each DTWPT tree level at most 5, starts from 1 (0 is original signal)
      for wp in WaveletPacket: #for each wavelet packet
        for node in wp.get_level(level, 'natural'): #get nodes in level in natural order(left->right leaves)
          Nodes = np.hstack([Nodes, node.data]) #cuidado não confundir os nomes pfv
        fd =  katz_fd(Nodes) if (fdType == 'katz') else hfda.measure(Nodes, 6) #Pegamos a FD do canal associado
        #fd = hfda.measure(Nodes, 6) #HIGUCHI
        row = np.append(row, fd) #concatenamos a FD do canal a row, que representa as info. da pessoa atual
        Nodes = np.empty(0, np.float64) #reseta Nodes
    #print(row.shape)
    feature_vector = np.vstack([feature_vector, row])
    return feature_vector
