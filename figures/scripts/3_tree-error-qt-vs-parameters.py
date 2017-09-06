#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate plots of Tree Error (QT) vs. various parameters
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'simulated':'#597DBE', 'fasttree':'#FF9980', 'raxml':'#A2B7C3'}
handles = [Patch(color=pal['fasttree'],label='FastTree'),Patch(color=pal['raxml'],label='RAxML')]
axisY = np.asarray([i/10.0 for i in range(0,11,2)])

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'QT':np.array([1.79053e+09,3.80976e+09,1.83636e+09,2.84427e+09,1.42561e+09,1.89373e+09,1.51494e+09,2.6491e+09,2.32669e+09,2.55929e+09,1.46655e+09,2.02914e+09,1.27333e+09,2.55523e+09,1.63125e+09,1.65773e+09,2.44189e+09,1.41325e+09,1.30001e+09,1.5285e+09] +  # r = 0.0001
                            [1.06183e+09,1.86437e+09,7.32155e+08,7.13346e+08,2.46094e+09,1.71253e+09,2.26165e+09,9.36453e+08,1.70713e+09,8.24366e+09,3.47073e+09,2.26165e+09,6.31153e+08,2.63276e+09,6.68875e+08,1.63025e+09,6.80528e+08,2.32102e+09,7.3549e+08,2.57141e+09] + # r = 0.001
                            [3.67167e+08,1.01615e+09,1.46156e+09,1.46879e+09,1.13029e+09,3.18877e+08,1.15705e+09,6.85903e+08,3.85894e+09,1.49264e+09,7.16531e+08,6.87688e+08,2.57622e+09,1.68901e+09,3.41722e+08,5.35329e+08,7.48677e+08,2.21776e+09,9.436e+08,4.59586e+08] +  # r = 0.01
                            [1.39403e+08,8.77392e+08,5.41484e+08,9.0418e+08,1.16767e+09,1.83343e+09,4.74924e+08,1.03914e+09,1.06824e+09,2.82274e+09,3.60609e+09,2.59511e+09,5.2443e+08,1.47871e+09,2.78047e+09,1.16571e+09,2.28354e+09,1.31498e+09,4.12853e+08,2.11089e+09] +  # r = 0.1
                            [4.04287e+08,3.76898e+08,1.76061e+07,8.97424e+08,4.81108e+08,4.30823e+09,1.57355e+09,5.34668e+08,1.92729e+09,6.12559e+08,3.38377e+09,1.9624e+09,4.03631e+08,8.47513e+08,2.26902e+08,1.83791e+09,1.87898e+09,2.28578e+09,2.72834e+09,2.58292e+09]   # r = 1
             ).astype(float)}
r_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'QT':np.array([1.0315e+09,4.56082e+09,1.17467e+09,1.5546e+09,1.34809e+09,1.20959e+09,1.0879e+09,2.21965e+09,2.05189e+09,2.67901e+09,1.10126e+09,1.50677e+09,1.02945e+09,1.0832e+09,1.59643e+09,1.24311e+09,1.89813e+09,1.11509e+09,1.03458e+09,8.69079e+08] +    # r = 0.0001
                            [6.19839e+08,1.21634e+09,2.54581e+08,5.96716e+08,8.00749e+08,7.45378e+08,1.25807e+09,6.40254e+08,4.58688e+08,1.81476e+09,3.14823e+09,4.85341e+08,5.07887e+08,2.58069e+09,7.15563e+08,1.59531e+09,5.51067e+08,1.50894e+09,6.20656e+08,1.3485e+09] + # r = 0.001
                            [1.89113e+08,1.29143e+08,8.7954e+08,1.45783e+09,7.79799e+08,2.10437e+08,6.97677e+08,4.18859e+08,2.73687e+09,1.16053e+09,6.34035e+08,1.00927e+09,4.75301e+09,3.01964e+08,1.59558e+08,1.85973e+08,2.03543e+08,8.42899e+08,2.42488e+08,5.12518e+08] + # r = 0.01
                            [1.48141e+08,9.00718e+08,5.25937e+08,5.89127e+08,1.9081e+08,2.39013e+08,4.66698e+08,8.92177e+08,1.03543e+09,2.36474e+09,3.59478e+09,3.01501e+09,4.26118e+08,1.46935e+09,2.75171e+09,1.10815e+09,2.27864e+09,1.8933e+09,4.10968e+08,2.40848e+09] +  # r = 0.1
                            [3.89334e+07,3.52854e+08,1.97252e+07,8.85704e+08,4.77228e+08,4.28479e+09,1.57327e+09,4.7132e+08,1.92729e+09,5.98281e+08,3.40107e+09,1.96029e+09,1.60892e+07,8.48855e+08,2.36e+08,1.77749e+09,1.8769e+09,2.27922e+09,2.73029e+09,2.56554e+09]       # r = 1
             ).astype(float)}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'QT':np.array([2.15228e+09,3.66921e+09,4.00033e+09,8.37739e+09,5.76543e+09,4.14567e+09,2.33799e+09,2.24583e+09,6.35992e+09,2.83622e+09,2.59451e+09,2.25527e+09,2.52908e+09,1.67112e+09,5.67818e+09,4.80068e+09,4.95439e+09,2.92582e+09,2.08323e+09,2.52409e+09] + # r = 0.0001
                             [9.71041e+08,8.16039e+08,9.1941e+08,4.52282e+09,2.87482e+09,3.58061e+09,5.04784e+09,1.35716e+09,2.61764e+09,1.67076e+09,4.28275e+09,7.5748e+08,1.07696e+09,2.42278e+09,2.08434e+09,3.00288e+09,8.80774e+08,7.81225e+09,6.62654e+08,1.72971e+09] +   # r = 0.001
                             [3.67167e+08,1.01615e+09,1.46156e+09,1.46879e+09,1.13029e+09,3.18877e+08,1.15705e+09,6.85903e+08,3.85894e+09,1.49264e+09,7.16531e+08,6.87688e+08,2.57622e+09,1.68901e+09,3.41722e+08,5.35329e+08,7.48677e+08,2.21776e+09,9.436e+08,4.59586e+08] +   # r = 0.01
                             [2.09654e+08,3.22957e+09,3.27475e+08,3.62616e+09,6.68102e+08,6.09558e+08,3.03515e+09,4.27171e+08,2.95235e+09,1.23226e+09,8.93836e+08,2.68287e+09,1.55466e+09,2.5456e+09,2.40989e+09,3.61922e+09,3.45392e+09,2.56554e+09,4.3738e+08,4.98405e+08] +   # r = 0.1
                             [6.10968e+09,1.82205e+09,6.47817e+08,2.45629e+09,2.49623e+09,1.20172e+09,4.02877e+09,7.1023e+08,4.18362e+09,5.3606e+09,6.35922e+09,4.60268e+08,5.97759e+09,4.7803e+09,4.78906e+09,2.82918e+09,2.99822e+09,3.26173e+09,2.55982e+09,2.94127e+09]      # r = 1
              ).astype(float)}
r2_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'QT':np.array([1.49183e+09,1.09433e+09,3.64234e+09,4.15274e+09,2.01163e+09,2.90213e+09,1.11465e+09,8.50848e+08,1.4259e+09,1.76374e+09,2.07044e+09,1.05116e+09,1.33332e+09,7.39376e+08,2.86252e+09,2.38776e+09,1.65011e+09,4.17819e+09,1.05513e+09,1.25183e+09] +  # r = 0.0001
                             [7.4009e+08,7.86752e+08,2.1274e+09,1.18407e+09,5.33809e+08,4.25259e+08,9.76576e+08,1.32285e+09,4.80525e+08,8.30795e+08,3.23499e+09,6.15476e+08,6.76825e+08,1.11115e+09,5.41232e+08,2.38237e+09,4.08703e+08,9.19208e+08,9.38858e+08,3.72932e+08] +   # r = 0.001
                             [1.89113e+08,1.29143e+08,8.7954e+08,1.45783e+09,7.79799e+08,2.10437e+08,6.97677e+08,4.18859e+08,2.73687e+09,1.16053e+09,6.34035e+08,1.00927e+09,4.75301e+09,3.01964e+08,1.59558e+08,1.85973e+08,2.03543e+08,8.42899e+08,2.42488e+08,5.12518e+08] +  # r = 0.01
                             [2.45072e+08,2.7542e+09,3.04313e+08,3.76541e+09,3.83119e+08,6.45475e+08,3.281e+09,4.14388e+08,2.68332e+09,1.29168e+09,3.95727e+08,2.86851e+09,2.22348e+09,2.49111e+09,2.56691e+09,3.15348e+09,3.09956e+09,2.55273e+09,3.24755e+08,4.86305e+08] +    # r = 0.1
                             [3.69644e+09,6.51633e+08,5.84062e+08,1.43767e+09,1.41012e+09,1.15713e+09,3.7145e+09,7.11449e+08,3.92688e+09,6.30835e+09,6.3539e+09,1.76667e+09,2.90731e+09,3.76982e+09,4.40546e+09,2.71041e+09,2.9025e+09,2.97605e+09,5.59967e+09,1.97347e+09]      # r = 1
              ).astype(float)}

# modifying lambda = lambdaA + lambdaB
l_fasttree = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'QT':np.array([4.77398e+09,5.5522e+09,2.5147e+09,1.52492e+09,4.05024e+09,2.02463e+09,3.36308e+09,1.22124e+09,1.14479e+09,1.63296e+09,4.097e+09,1.75206e+09,4.71629e+09,4.69639e+09,3.45656e+09,2.63782e+09,5.6776e+08,4.39783e+09,2.38643e+09,8.1282e+08] +      # lambda = 33.86550309051126
                            [1.37224e+09,3.6844e+09,1.19533e+09,2.65936e+09,7.12997e+08,2.37682e+09,3.81608e+08,2.01479e+09,2.5652e+09,1.77938e+09,5.14539e+08,3.14975e+09,4.06621e+09,7.60845e+08,4.07322e+09,3.39831e+08,5.72783e+08,4.17846e+09,4.86075e+09,1.04743e+09] +  # lambda = 84.66375772627816
                            [3.67167e+08,1.01615e+09,1.46156e+09,1.46879e+09,1.13029e+09,3.18877e+08,1.15705e+09,6.85903e+08,3.85894e+09,1.49264e+09,7.16531e+08,6.87688e+08,2.57622e+09,1.68901e+09,3.41722e+08,5.35329e+08,7.48677e+08,2.21776e+09,9.436e+08,4.59586e+08] +  # lambda = 169.32751545255631
                            [3.69941e+09,2.70288e+09,2.00377e+09,8.09516e+08,2.09692e+09,1.91467e+09,1.16487e+09,5.04296e+08,2.5933e+09,2.15205e+09,9.12176e+08,3.01428e+09,6.36285e+09,3.03813e+09,3.19066e+09,3.87563e+09,6.77762e+08,1.26673e+09,1.13714e+09,1.86439e+09] + # lambda = 338.65503090511262
                            [1.42489e+09,9.57535e+09,1.24608e+09,1.02088e+09,2.18965e+09,2.73187e+09,2.55531e+09,2.32069e+09,3.05526e+09,3.61459e+09,1.67255e+09,9.52687e+09,3.44588e+09,6.62713e+09,2.57612e+09,4.97241e+09,4.78134e+09,2.02195e+09,2.01075e+09,6.9952e+09]   # lambda = 846.63757726278155
             ).astype(float)}
l_raxml    = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'QT':np.array([1.93564e+09,2.83851e+09,2.03887e+09,1.50056e+09,2.62873e+09,1.57673e+09,4.87325e+08,3.5217e+09,1.14432e+09,1.48749e+09,4.67828e+09,1.17106e+09,2.69945e+09,3.03639e+09,1.6915e+09,1.69905e+09,4.4893e+08,4.44095e+09,2.68599e+09,7.88652e+08] +   # lambda = 33.86550309051126
                            [1.06241e+09,2.18522e+09,9.0807e+08,9.31585e+08,7.02365e+08,2.24862e+09,2.70907e+08,1.77538e+09,2.51395e+09,3.62482e+08,3.11039e+08,3.25174e+09,4.95992e+09,6.67224e+08,3.18924e+09,4.25568e+08,9.30314e+08,9.50762e+08,1.49666e+09,1.71848e+09] + # lambda = 84.66375772627816
                            [1.89113e+08,1.29143e+08,8.7954e+08,1.45783e+09,7.79799e+08,2.10437e+08,6.97677e+08,4.18859e+08,2.73687e+09,1.16053e+09,6.34035e+08,1.00927e+09,4.75301e+09,3.01964e+08,1.59558e+08,1.85973e+08,2.03543e+08,8.42899e+08,2.42488e+08,5.12518e+08] + # lambda = 169.32751545255631
                            [1.84989e+09,1.95174e+09,1.83386e+09,6.17942e+08,1.91329e+09,1.0359e+09,1.45853e+09,4.88287e+08,2.4927e+09,2.15597e+09,5.28421e+08,2.79503e+09,6.32731e+09,7.11981e+09,5.60122e+09,3.17735e+09,1.51663e+09,1.2182e+09,1.12007e+09,1.09497e+09] +   # lambda = 338.65503090511262
                            [1.34714e+09,1.23503e+10,1.10332e+09,7.4209e+08,1.75068e+09,1.21938e+09,2.81369e+09,2.10753e+09,1.02091e+09,2.87515e+09,2.91953e+09,1.05794e+10,3.66446e+09,6.50113e+09,2.39422e+09,4.45667e+09,4.13894e+09,2.03553e+09,4.98188e+09,8.53072e+09]   # lambda = 846.63757726278155
             ).astype(float)}

# modifying sequence length
k_fasttree = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'QT':np.array([7.6568e+09,7.92823e+09,8.43668e+09,4.51357e+09,1.01434e+10,6.07431e+09,1.23015e+10,1.07037e+10,7.33965e+09,9.12831e+09,1.44565e+10,2.43332e+09,7.90613e+09,8.91846e+09,5.59415e+09,1.92788e+10,4.61347e+09,1.18139e+10,7.11839e+09,5.03465e+09] + # length = 50
                            [5.28498e+09,2.92626e+09,3.49467e+09,7.7705e+09,6.45052e+09,8.45933e+09,3.40518e+09,2.72048e+09,3.14366e+09,4.08223e+09,5.47913e+09,2.37981e+09,1.66417e+09,8.8532e+09,6.39509e+09,3.51998e+09,1.88546e+09,6.4617e+09,7.32539e+09,5.09359e+09] +   # length = 100
                            [9.88851e+08,3.45799e+09,1.93322e+09,1.97175e+09,1.0952e+09,5.06889e+08,4.51727e+09,8.3575e+08,1.06684e+09,2.48838e+09,6.8142e+09,2.29188e+09,7.17893e+09,1.5109e+09,2.64e+08,6.58949e+09,1.06153e+09,2.94547e+09,9.5973e+09,3.54774e+09] +        # length = 200
                            [3.67167e+08,1.01615e+09,1.46156e+09,1.46879e+09,1.13029e+09,3.18877e+08,1.15705e+09,6.85903e+08,3.85894e+09,1.49264e+09,7.16531e+08,6.87688e+08,2.57622e+09,1.68901e+09,3.41722e+08,5.35329e+08,7.48677e+08,2.21776e+09,9.436e+08,4.59586e+08] +  # length = 300
                            [2.83865e+08,2.46907e+08,1.04855e+08,2.17503e+08,7.97887e+08,8.85843e+08,1.92415e+09,4.09349e+09,4.85861e+08,7.2282e+08,1.10484e+09,1.89242e+08,4.10362e+08,4.05358e+08,5.20328e+08,1.86792e+08,1.84698e+08,1.04364e+09,6.28735e+08,1.80873e+08] + # length = 600
                            [4.01312e+08,6.04023e+07,9.16639e+07,7.82516e+07,3.07365e+07,3.88472e+07,8.86556e+08,5.66018e+07,1.03205e+09,5.06269e+08,3.48985e+08,1.25564e+09,3.68432e+08,4.05894e+08,2.08001e+09,6.21501e+07,7.572e+07,7.25435e+07,8.63286e+08,2.35637e+09] +  # length = 1200
                            [8.14449e+07,1.2403e+08,1.51937e+09,1.28449e+08,3.94661e+07,1.65604e+08,4.22358e+07,6.38784e+07,6.77141e+07,6.35419e+07,1.13264e+08,3.91976e+07,7.9134e+07,5.31725e+08,7.36502e+07,2.8473e+08,3.80985e+07,1.07586e+08,2.1094e+09,2.81037e+08] +    # length = 2400
                            [2.78826e+07,1.3341e+07,1.7743e+08,6.77117e+07,3.45342e+07,1.90964e+09,4.37058e+07,2.47058e+08,4.66504e+07,5.41751e+07,1.99015e+07,2.57282e+07,2.76884e+07,2.37716e+08,7.75998e+07,8.44234e+06,1.77922e+07,1.30419e+07,2.37445e+07,3.55208e+07]    # length = 4800
             ).astype(float)}
k_raxml    = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'QT':np.array([8.45179e+09,6.50528e+09,8.29341e+09,5.38486e+09,1.22999e+10,5.21442e+09,7.94843e+09,1.07263e+10,7.4984e+09,7.6263e+09,1.38011e+10,7.03283e+09,8.53033e+09,4.44993e+09,7.43241e+09,1.64853e+10,4.78286e+09,1.2775e+10,8.41751e+09,3.50708e+09] +   # length = 50
                            [4.63277e+09,1.6581e+09,3.96166e+09,3.42275e+09,3.49638e+09,6.83746e+09,5.58331e+09,8.65063e+08,3.83373e+09,5.00455e+09,3.28395e+09,2.38956e+09,3.06599e+09,6.87189e+09,6.09903e+09,8.97912e+08,1.05055e+09,6.34746e+09,4.51451e+09,4.73097e+09] + # length = 100
                            [9.35471e+08,2.11079e+09,7.25383e+08,2.03509e+09,5.64958e+08,3.95536e+08,1.89451e+09,7.03623e+08,9.74641e+08,2.3935e+09,3.96317e+09,2.04523e+09,3.35172e+09,1.80781e+09,2.23775e+08,7.85369e+09,4.10663e+08,3.9314e+08,7.39707e+09,3.37359e+09] +  # length = 200
                            [1.89113e+08,1.29143e+08,8.7954e+08,1.45783e+09,7.79799e+08,2.10437e+08,6.97677e+08,4.18859e+08,2.73687e+09,1.16053e+09,6.34035e+08,1.00927e+09,4.75301e+09,3.01964e+08,1.59558e+08,1.85973e+08,2.03543e+08,8.42899e+08,2.42488e+08,5.12518e+08] + # length = 300
                            [1.66969e+08,1.43552e+08,9.9046e+07,9.65646e+07,1.63747e+09,7.91862e+08,5.63205e+07,3.60546e+09,4.94665e+08,7.04654e+08,1.10812e+09,1.0465e+08,4.08182e+08,3.07623e+08,4.61031e+08,1.7723e+08,7.30507e+07,9.34149e+08,2.77635e+08,1.64835e+08] +   # length = 600
                            [2.54197e+07,6.23943e+07,8.87208e+07,3.0423e+07,3.62904e+07,3.05726e+07,1.19432e+08,5.99155e+07,1.08076e+09,4.54102e+08,3.3901e+08,1.44812e+09,1.72039e+08,2.58249e+08,2.05597e+09,3.69711e+07,8.95334e+07,1.08721e+08,8.48956e+08,1.02905e+08] +  # length = 1200
                            [5.98673e+07,1.34874e+08,1.51331e+09,1.29502e+08,3.79328e+07,2.0497e+08,4.26478e+07,6.20921e+07,7.00239e+07,3.49774e+07,1.31622e+08,3.90404e+07,3.06962e+07,5.11688e+08,7.25795e+07,4.83732e+07,8.70453e+08,1.073e+08,2.12012e+09,2.57955e+08] +   # length = 2400
                            [3.28866e+07,1.22418e+07,1.76934e+08,1.59206e+07,3.45254e+07,1.90948e+09,4.38355e+07,2.42333e+08,2.62219e+07,5.42174e+07,1.67998e+07,2.5604e+07,2.87054e+07,1.96472e+08,7.20215e+07,8.11018e+06,1.08857e+07,3.77266e+06,2.3873e+07,3.45213e+07]    # length = 4800
             ).astype(float)}

# modifying deviation from ultrametricity
g_fasttree = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'QT':np.array([8.45447e+08,2.00543e+09,5.71083e+09,2.8501e+09,2.12871e+09,3.24525e+09,3.84638e+09,2.47696e+09,7.83444e+08,2.67104e+09,2.46595e+09,5.30081e+09,3.09249e+09,1.85118e+09,1.5394e+09,2.29666e+09,2.13609e+09,2.91081e+09,5.44677e+09,3.78277e+09] +   # gamma = 2.95181735298926
                            [1.16741e+09,4.8521e+08,2.64061e+08,7.56617e+08,3.92332e+09,1.42643e+09,2.68101e+09,1.25551e+09,8.56464e+08,9.64197e+08,1.67399e+09,4.95919e+09,1.61507e+09,2.7269e+09,3.66779e+09,1.25685e+09,1.07548e+09,2.42397e+09,2.26893e+09,2.6505e+09] +    # gamma = 5.90363470597852
                            [3.67167e+08,1.01615e+09,1.46156e+09,1.46879e+09,1.13029e+09,3.18877e+08,1.15705e+09,6.85903e+08,3.85894e+09,1.49264e+09,7.16531e+08,6.87688e+08,2.57622e+09,1.68901e+09,3.41722e+08,5.35329e+08,7.48677e+08,2.21776e+09,9.436e+08,4.59586e+08] +   # gamma = 29.518173529892621
                            [6.61753e+08,2.07665e+09,9.67794e+08,5.05916e+08,3.28534e+09,4.24426e+08,1.25547e+09,2.51729e+09,3.04138e+09,7.92748e+08,3.47112e+09,4.24837e+08,3.35074e+09,2.0193e+09,1.39575e+09,1.45514e+09,9.59248e+08,7.12711e+09,7.93843e+08,2.85686e+09] +  # gamma = 147.590867649463
                            [3.30376e+08,5.27523e+09,1.44049e+09,2.32076e+08,6.40591e+08,2.58958e+09,1.36067e+09,2.56894e+09,1.30833e+09,6.95312e+08,2.39624e+09,2.31196e+08,2.93216e+09,2.87129e+08,1.93976e+09,3.23232e+09,1.04387e+09,1.97534e+09,2.12298e+08,1.56798e+09] + # gamma = 295.181735298926
                            [2.87693e+09,2.8153e+08,2.73535e+08,9.81163e+08,4.11408e+09,9.51726e+08,1.28594e+09,2.31702e+09,6.32148e+09,8.44278e+08,6.28133e+08,1.21496e+09,1.12087e+09,2.45305e+08,4.86072e+09,4.24843e+08,3.84434e+08,2.25258e+09,1.62584e+09,1.82887e+09]    # gamma = infinity
             ).astype(float)}
g_raxml    = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'QT':np.array([9.17101e+08,1.67942e+09,5.62596e+09,1.56791e+09,2.07237e+09,3.12878e+09,2.75037e+09,3.75904e+08,6.24709e+08,2.63087e+09,2.43783e+09,1.96744e+09,2.8736e+09,1.47084e+09,3.7695e+08,2.3749e+09,2.34274e+09,4.34352e+08,6.91175e+08,3.78868e+09] +    # gamma = 2.95181735298926
                            [8.74471e+08,3.01203e+08,2.12243e+08,4.96785e+08,3.85651e+09,1.21031e+09,2.68063e+09,1.12216e+09,2.14205e+09,7.80825e+08,5.62146e+08,4.36545e+09,1.63749e+09,2.42865e+09,2.72945e+09,9.89936e+08,2.00704e+08,1.22396e+09,2.31728e+09,1.5352e+09] +  # gamma = 5.90363470597852
                            [1.89113e+08,1.29143e+08,8.7954e+08,1.45783e+09,7.79799e+08,2.10437e+08,6.97677e+08,4.18859e+08,2.73687e+09,1.16053e+09,6.34035e+08,1.00927e+09,4.75301e+09,3.01964e+08,1.59558e+08,1.85973e+08,2.03543e+08,8.42899e+08,2.42488e+08,5.12518e+08] +  # gamma = 29.518173529892621
                            [9.44141e+08,1.44664e+09,2.83858e+08,4.93377e+08,3.24106e+09,9.85988e+08,1.09147e+09,2.47221e+09,1.33799e+09,1.79903e+09,3.33738e+09,4.70969e+08,3.30797e+09,1.92821e+09,1.85062e+09,1.22832e+09,5.42622e+08,2.23158e+09,7.24801e+08,4.00896e+08] + # gamma = 147.590867649463
                            [1.73059e+08,1.22923e+09,8.30755e+08,1.62164e+08,7.0132e+08,2.34355e+09,1.18204e+09,8.42288e+08,6.73129e+08,6.92019e+08,1.52667e+09,2.77887e+08,2.73253e+09,2.21733e+08,3.67384e+09,1.47461e+09,5.73411e+08,4.1e+09,1.98326e+08,1.67492e+09] +      # gamma = 295.181735298926
                            [1.42095e+09,8.32676e+07,2.16758e+08,1.01188e+09,2.15698e+09,1.11143e+09,1.25363e+09,4.06945e+08,5.8033e+08,7.40418e+08,6.1181e+08,6.70852e+08,1.14541e+09,2.94968e+08,3.2585e+09,4.08587e+08,2.2671e+08,2.64632e+09,1.2167e+09,1.19926e+09]        # gamma = infinity
             ).astype(float)}

# plot tree error (QT) vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'QT':{},'category':{}}
for i in range(len(r_fasttree['QT'])):
    currNum = len(df['r'])
    df['r'][currNum] = r_fasttree['r'][i]
    df['QT'][currNum] = r_fasttree['QT'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r_raxml['r'][i]
    df['QT'][currNum] = r_raxml['QT'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='QT',hue='category',data=df,order=x,palette=pal)
plt.ylim(-0.2e10,2.5e10)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (QT)',fontsize=14)
sns.plt.title(r'Tree Error (QT) vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-qt_vs_r_const-exp-branch-length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (QT) vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'QT':{},'category':{}}
for i in range(len(r2_fasttree['QT'])):
    currNum = len(df['r'])
    df['r'][currNum] = r2_fasttree['r'][i]
    df['QT'][currNum] = r2_fasttree['QT'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r2_raxml['r'][i]
    df['QT'][currNum] = r2_raxml['QT'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='QT',hue='category',data=df,order=x,palette=pal)
plt.ylim(-0.2e10,2.5e10)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (QT)',fontsize=14)
sns.plt.title(r'Tree Error (QT) vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-qt_vs_r_const-lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (QT) vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
df = {'lambda':{},'QT':{},'category':{}}
for i in range(len(l_fasttree['QT'])):
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_fasttree['lambda'][i]
    df['QT'][currNum] = l_fasttree['QT'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_raxml['lambda'][i]
    df['QT'][currNum] = l_raxml['QT'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='lambda',y='QT',hue='category',data=df,order=x,palette=pal)
plt.ylim(-0.2e10,2.5e10)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Tree Error (QT)',fontsize=14)
sns.plt.title(r'Tree Error (QT) vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-qt_vs_lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (QT) vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
df = {'length':{},'QT':{},'category':{}}
for i in range(len(k_fasttree['QT'])):
    currNum = len(df['length'])
    df['length'][currNum] = k_fasttree['length'][i]
    df['QT'][currNum] = k_fasttree['QT'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['length'])
    df['length'][currNum] = k_raxml['length'][i]
    df['QT'][currNum] = k_raxml['QT'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='length',y='QT',hue='category',data=df,order=x,palette=pal)
plt.ylim(-0.2e10,2.5e10)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Tree Error (QT)',fontsize=14)
sns.plt.title('Tree Error (QT) vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-qt_vs_length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (QT) vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
df = {'gammarate':{},'QT':{},'category':{}}
for i in range(len(g_fasttree['QT'])):
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_fasttree['gammarate'][i]
    df['QT'][currNum] = g_fasttree['QT'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_fasttree['gammarate'][i]
    df['QT'][currNum] = g_fasttree['QT'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='gammarate',y='QT',hue='category',data=df,order=x,palette=pal)
plt.ylim(-0.2e10,2.5e10)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (QT)',fontsize=14)
sns.plt.title('Tree Error (QT) vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-qt_vs_gammarate.pdf', format='pdf', bbox_inches='tight')
plt.close()