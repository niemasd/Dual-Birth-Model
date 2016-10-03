#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of Tree Error (RF) vs. various parameters
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

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_data = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
          'RF':np.array([.897,.9525,.9272,.95995,.99815,.88575,.91898,.9547,.91822,.8837,.9115,.93532,.8977,.9765,.915855,.91843,.9247,.91111,.91415,.8968] + # r = 0.0001
                        [.66145,.667,.6911,.6876,.7166,.69355,.7735,.69375,.7215,.6688,.681,.71,.765,.68185,.66885,.798,.66965,.75175,.7865,.68265] +         # r = 0.001
                        [.37315,.39425,.3725,.3995,.479,.3756,.395,.3726,.37335,.35715,.38635,.465,.3545,.37955,.34945,.3971,.38635,.3948,.3593,.3653] +      # r = 0.01
                        [.15855,.16415,.16615,.18365,.1981,.1724,.1644,.1391,.17215,.1997,.18295,.17725,.1755,.1594,.223,.18245,.1941,.17,.18195,.177] +      # r = 0.1
                        [.12,.1193,.11625,.125,.128,.1335,.1124,.1325,.782,.948,.1223,.1173,.1114,.12385,.11125,.11785,.995,.123,.1285,.998]                  # r = 1
         ).astype(float)}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_data = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
           'RF':np.array([.794,.8324,.75215,.7813,.85645,.854,.7884,.7934,.874,.814,.8195,.7864,.7773,.7894,.823,.7994,.7934,.772,.7573,.812] +              # r = 0.0001
                         [.53135,.56625,.5725,.58325,.614,.57525,.5713,.5811,.616,.62735,.64245,.54615,.55945,.5974,.56325,.6185,.565,.58875,.56725,.5586] + # r = 0.001
                         [.37315,.39425,.3725,.3995,.479,.3756,.395,.3726,.37335,.35715,.38635,.465,.3545,.37955,.34945,.3971,.38635,.3948,.3593,.3653] +    # r = 0.01
                         [.26925,.2835,.29195,.29485,.289,.2834,.2664,.29245,.29715,.3455,.28255,.2912,.2964,.2895,.383,.3139,.2935,.31225,.28495,.28515] +  # r = 0.1
                         [.2575,.2535,.28145,.32125,.2951,.3835,.27525,.311,.26855,.2879,.335,.28135,.294,.3115,.267,.2965,.3185,.28325,.2825,.257]          # r = 1
          ).astype(float)}

# modifying lambda = lambdaA + lambdaB
l_data = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
          'RF':np.array([.3631,.318,.32665,.33285,.3579,.3499,.342,.33565,.39,.3571,.389,.3671,.34285,.321,.379,.3159,.2959,.322,.39,.32265] +           # lambda = 33.86550309051126
                        [.331,.36275,.31375,.338,.382,.3275,.31345,.281,.33665,.33755,.36145,.328,.3285,.334,.31575,.34255,.3245,.35755,.325,.324] +     # lambda = 84.66375772627816
                        [.37315,.39425,.3725,.3995,.479,.3756,.395,.3726,.37335,.35715,.38635,.465,.3545,.37955,.34945,.3971,.38635,.3948,.3593,.3653] + # lambda = 169.32751545255631
                        [.525,.539,.48125,.513,.4868,.51635,.49665,.5192,.4519,.49315,.4857,.474,.4684,.4994,.4765,.5275,.4598,.49255,.49445,.4515] +    # lambda = 338.65503090511262
                        [.65965,.66925,.6423,.64885,.68815,.651,.68,.6545,.6474,.69925,.6665,.6534,.6322,.6666,.65965,.6452,.6575,.65555,.67875,.6755]   # lambda = 846.63757726278155
         ).astype(float)}

# modifying sequence length
k_data = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
          'RF':np.array([.7745,.7954,.7778,.7763,.7989,.78115,.7745,.7914,.72955,.7962,.7691,.79815,.792,.77555,.7581,.7583,.895,.7644,.76895,.79525] +   # length = 50
                        [.6435,.621,.64675,.6294,.61235,.6452,.6555,.63375,.6375,.6575,.6253,.64825,.64485,.62945,.67165,.6381,.613,.6241,.6165,.65695] + # length = 100
                        [.458,.4718,.49245,.46975,.45675,.47835,.5194,.4673,.4594,.4745,.46545,.45465,.4382,.4952,.44265,.4987,.49975,.595,.51,.45685] +  # length = 200
                        [.37315,.39425,.3725,.3995,.479,.3756,.395,.3726,.37335,.35715,.38635,.465,.3545,.37955,.34945,.3971,.38635,.3948,.3593,.3653] +  # length = 300
                        [.2457,.24585,.2446,.24895,.2743,.25525,.2337,.251,.2695,.24525,.2845,.24735,.258,.26545,.2578,.26125,.2223,.2739,.2548,.2594] +  # length = 600
                        [.1385,.13835,.1534,.1534,.15855,.1815,.1674,.1634,.1654,.1846,.1694,.1624,.165,.1671,.1655,.1595,.1714,.1595,.1725,.1625] +      # length = 1200
                        [.1725,.1825,.163,.1625,.93,.943,.893,.93,.11225,.93,.812,.832,.9425,.953,.8525,.993,.963,.1425,.113,.752] +                      # length = 2400
                        [.6215,.615,.62,.572,.5815,.615,.632,.7415,.7315,.461,.642,.622,.682,.682,.632,.622,.622,.5515,.6115,.682]                        # length = 4800
             ).astype(float)}

# modifying deviation from ultrametricity
g_data = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
          'RF':np.array([.41725,.43145,.4223,.41265,.4316,.4441,.42755,.3845,.41855,.4183,.4445,.41245,.475,.3714,.4224,.4,.45145,.427,.41735,.396] +     # gamma = 2.95181735298926
                        [.417,.3961,.39445,.39655,.4254,.39275,.42315,.445,.478,.424,.3673,.39365,.39815,.41175,.414,.45175,.4345,.45575,.3931,.4191] +   # gamma = 5.90363470597852
                        [.37315,.39425,.3725,.3995,.479,.3756,.395,.3726,.37335,.35715,.38635,.465,.3545,.37955,.34945,.3971,.38635,.3948,.3593,.3653] +  # gamma = 29.518173529892621
                        [.3578,.3814,.36415,.331,.35295,.41345,.3951,.4149,.3967,.384,.39585,.398,.3693,.457,.3632,.3576,.38825,.429,.38875,.3983] +      # gamma = 147.590867649463
                        [.365,.3683,.38515,.35425,.3955,.3646,.33185,.38665,.39235,.374,.42215,.3831,.3638,.4885,.36685,.418,.34975,.35415,.3489,.3556] + # gamma = 295.181735298926
                        [.41,.37855,.36955,.424,.37725,.38615,.35245,.3933,.3942,.3745,.38445,.3762,.3925,.37115,.46,.38395,.38695,.368,.38755,.36195]    # gamma = infinity
             ).astype(float)}

# plot tree error (RF) vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='RF',data=pd.DataFrame(r_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-exp-branch-length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. r (with constant lambda = lambdaA + lambdaB)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='RF',data=pd.DataFrame(r2_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. lambda
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
ax = sns.violinplot(x='lambda',y='RF',data=pd.DataFrame(l_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. length
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
ax = sns.violinplot(x='length',y='RF',data=pd.DataFrame(k_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. gamma rate
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
ax = sns.violinplot(x='gammarate',y='RF',data=pd.DataFrame(g_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_gammarate.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()