# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:06:59 2021

@author: richa
"""

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import date


bure = pd.read_csv('2021-12-08_bure_pris_historik.csv')
bure = bure['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
bure = bure.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
bure = bure.set_index("Date")


cred = pd.read_csv('2021-12-08_cred a_pris_historik.csv')
cred = cred['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
cred = cred.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
cred = cred.set_index("Date")



induc = pd.read_csv('2021-12-08_indu c_pris_historik.csv')
induc = induc['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
induc = induc.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
induc = induc.set_index("Date")



inveb = pd.read_csv('2021-12-08_inve b_pris_historik.csv')
inveb = inveb['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
inveb = inveb.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
inveb = inveb.set_index("Date")


kinvb = pd.read_csv('2021-12-08_kinv b_pris_historik.csv')
kinvb = kinvb['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
kinvb = kinvb.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
kinvb = kinvb.set_index("Date")



latob = pd.read_csv('2021-12-08_lato b_pris_historik.csv')
latob = latob['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
latob = latob.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
latob = latob.set_index("Date")


lundb = pd.read_csv('2021-12-08_lund b_pris_historik.csv')
lundb = lundb['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
lundb = lundb.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
lundb = lundb.set_index("Date")


svolb = pd.read_csv('2021-12-08_svol b_pris_historik.csv')
svolb = svolb['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
svolb = svolb.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
svolb = svolb.set_index("Date")


vef= pd.read_csv('2021-12-08_vef_pris_historik.csv')
vef = vef['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
vef = vef.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
vef = vef.set_index("Date")



vnv= pd.read_csv('2021-12-08_vnv_pris_historik.csv')
vnv = vnv['DATUM;PRIS;SUBSTANSVÄRDE;BERÄKNAT_SUBSTANSVÄRDE'].str.split(";",expand=True)
vnv = vnv.rename(columns={0:"Date", 1:"Close", 2:"Last NAV", 3:"Calc NAV"})
vnv = vnv.set_index("Date")



bure_close = bure["Close"].astype(float, errors = 'raise')
bure_last_reported_nav = bure["Last NAV"].astype(float, errors = 'raise')
bure_calc_nav = bure["Calc NAV"].astype(float, errors = 'raise')

bure_disc_reported_nav = bure_close/bure_last_reported_nav-1
bure_disc_calc_nav = bure_close/bure_calc_nav-1
bure_disc_reported_nav.name = "bure reported nav discount"
#bure_dates = pd.to_datetime(bure[0])
#bure_data = pd.concat([bure_dates, bure_close, bure_disc_reported_nav, bure_disc_calc_nav],axis=1)
#bure_data.set_index('0')


cred_close = cred["Close"].astype(float, errors = 'raise')
cred_last_reported_nav = cred["Last NAV"].astype(float, errors = 'raise')
cred_calc_nav = cred["Calc NAV"].astype(float, errors = 'raise')

cred_disc_reported_nav = cred_close/cred_last_reported_nav-1
cred_disc_calc_nav = cred_close/cred_calc_nav-1
cred_disc_reported_nav.name = "creades reported nav discount"


induc_close = induc["Close"].astype(float, errors = 'raise')
induc_last_reported_nav = induc["Last NAV"].astype(float, errors = 'raise')
induc_calc_nav = induc["Calc NAV"].astype(float, errors = 'raise')

induc_disc_reported_nav = induc_close/induc_last_reported_nav-1
induc_disc_calc_nav = induc_close/induc_calc_nav-1
induc_disc_reported_nav.name = "industrivärden reported nav discount"


inveb_close = inveb["Close"].astype(float, errors = 'raise')
inveb_last_reported_nav = inveb["Last NAV"].astype(float, errors = 'raise')
inveb_calc_nav = inveb["Calc NAV"].astype(float, errors = 'raise')

inveb_disc_reported_nav = inveb_close/inveb_last_reported_nav-1
inveb_disc_calc_nav = inveb_close/inveb_calc_nav-1
inveb_disc_reported_nav.name = "investor reported nav discount"


kinvb_close = kinvb["Close"].astype(float, errors = 'raise')
kinvb_last_reported_nav = kinvb["Last NAV"].astype(float, errors = 'raise')
kinvb_calc_nav = kinvb["Calc NAV"].astype(float, errors = 'raise')

kinvb_disc_reported_nav = kinvb_close/kinvb_last_reported_nav-1
kinvb_disc_calc_nav = kinvb_close/kinvb_calc_nav-1
kinvb_disc_reported_nav.name = "kinnevik reported nav discount"




latob_close = latob["Close"].astype(float, errors = 'raise')
latob_last_reported_nav = latob["Last NAV"].astype(float, errors = 'raise')
latob_calc_nav = latob["Calc NAV"].astype(float, errors = 'raise')

latob_disc_reported_nav = latob_close/latob_last_reported_nav-1
latob_disc_calc_nav = latob_close/latob_calc_nav-1
latob_disc_reported_nav.name = "latour reported nav discount"




lundb_close = lundb["Close"].astype(float, errors = 'raise')
lundb_last_reported_nav = lundb["Last NAV"].astype(float, errors = 'raise')
lundb_calc_nav = lundb["Calc NAV"].astype(float, errors = 'raise')

lundb_disc_reported_nav = lundb_close/lundb_last_reported_nav-1
lundb_disc_calc_nav = lundb_close/lundb_calc_nav-1
lundb_disc_reported_nav.name = "lundbergsföretagen reported nav discount"

svolb_close = svolb["Close"].astype(float, errors = 'raise')
svolb_last_reported_nav = svolb["Last NAV"].astype(float, errors = 'raise')
svolb_calc_nav = svolb["Calc NAV"].astype(float, errors = 'raise')

svolb_disc_reported_nav = svolb_close/svolb_last_reported_nav-1
svolb_disc_calc_nav = svolb_close/svolb_calc_nav-1
svolb_disc_reported_nav.name = "svolder reported nav discount"



vef_close = vef["Close"].astype(float, errors = 'raise')
vef_last_reported_nav = vef["Last NAV"].astype(float, errors = 'raise')
vef_calc_nav = vef["Calc NAV"].astype(float, errors = 'raise')

vef_disc_reported_nav = vef_close/vef_last_reported_nav-1
vef_disc_calc_nav = vef_close/vef_calc_nav-1
vef_disc_reported_nav.name = "VEF reported nav discount"


vnv_close = vnv["Close"].astype(float, errors = 'raise')
vnv_last_reported_nav = vnv["Last NAV"].astype(float, errors = 'raise')
vnv_calc_nav = vnv["Calc NAV"].astype(float, errors = 'raise')

vnv_disc_reported_nav = vnv_close/vnv_last_reported_nav-1
vnv_disc_calc_nav = vnv_close/vnv_calc_nav-1
vnv_disc_reported_nav.name = "vnv reported nav discount"


disc_reported_navs = pd.merge(bure_disc_reported_nav,cred_disc_reported_nav, on='Date',how='outer')
disc_reported_navs.name = 'discount to navs'

disc_reported_navs = pd.merge(disc_reported_navs,induc_disc_reported_nav, on='Date',how='outer')
disc_reported_navs.name = 'discount to navs'
# disc_reported_navs = pd.merge(disc_reported_navs,inveb_disc_reported_nav, on='Date',how='outer')
# disc_reported_navs = pd.merge(disc_reported_navs,kinvb_disc_reported_nav, on='Date',how='outer')
# disc_reported_navs = pd.merge(disc_reported_navs,latob_disc_reported_nav, on='Date',how='outer')
# disc_reported_navs = pd.merge(disc_reported_navs,svolb_disc_reported_nav, on='Date',how='outer')
# disc_reported_navs = pd.merge(disc_reported_navs,vef_disc_reported_nav, on='Date',how='outer')
# disc_reported_navs = pd.merge(disc_reported_navs,vnv_disc_reported_nav, on='Date',how='outer')

#disc_reported_navs = pd.concat([bure_disc_reported_nav, cred_disc_reported_nav, induc_disc_reported_nav,inveb_disc_reported_nav,kinvb_disc_reported_nav, latob_disc_reported_nav, lundb_disc_reported_nav, svolb_disc_reported_nav, vef_disc_reported_nav, vnv_disc_reported_nav],axis=1)
#closes =  pd.concat([bure_close, cred_close, induc_close,inveb_close,kinvb_close, latob_close, lundb_close, svolb_close, vef_close, vnv_close],axis=1)
#
#
##nav discount 5 day changes
#disc_changes = disc_reported_navs - disc_reported_navs.shift(5)
#
##calculate daily returns
#ret_daily = closes.pct_change()
#volatility=ret_daily.rolling(20).std().shift(1)
#
##calculate 5 day returns
#ret_5d = bure_close.pct_change(5)
#
#
#n_std_ret5d =ret_5d/(volatility*math.sqrt(5))
#
## =============================================================================
## #generate position indicator bottom 20% = +1 top 25% = -1, exclude stocks with short sale restrictions from top 20%
## short_sale_restrict = ["FPAR-A.ST", "KFAST-B.ST", "DIOS.ST", "HEBA-B.ST", "TRIAN-B.ST", "CIBUS.ST", "AMAST.ST"]
## ret_5d_shortable = ret_5d.drop(short_sale_restrict, axis=1)
## ret_daily_shortable = ret_daily.drop(short_sale_restrict, axis=1)
## percentile80_shortable = ret_5d_shortable.quantile(0.75,axis=1)
## short_ind = ret_5d_shortable.ge(percentile80_shortable,axis=0)
## #replace false with NaN to get the right average
## short_ind = short_ind.replace(False, np.nan)
## short_returns_daily = -ret_daily_shortable*short_ind.shift(1)
## 
## =============================================================================
#
#
#
#percentile20 = ret_5d.quantile(0.2,axis=1)
#percentile80 = ret_5d.quantile(0.8,axis=1)
#spread = percentile80-percentile20
#
##create binary dataframe to exclude stocks with big move large volume days in the last n sessions
##significant_days = (r_vol > 5) & (ret_daily < -0.05)
# 
##not_excluded = significant_days.rolling(5).sum() < 1
##create position indicator df
#long_ind = (ret_5d.le(percentile20,axis=0))# & not_excluded 
#
##long_ind = (ret_5d < 0) 
##replace false with NaN to avoid 0s impacting the mean
#long_ind = long_ind.replace(False, np.nan)
#long_returns_daily = ret_daily*long_ind.shift(1)
#
#
##calc transaction cost
#trans = long_ind-long_ind.shift(1)
#n_trans = trans.count().sum()
#
#trans_value = n_trans*75000
#total_trans_cost = n_trans*29
#
#trans_proc_fee = total_trans_cost/trans_value
#
##daily returns of long short strategy
##avg_long_ret = starting_capital*long_returns_daily.mean(axis=1)-transaction_cost
#avg_long_ret = long_returns_daily.mean(axis=1)-trans_proc_fee
##avg_short_ret = short_returns_daily.mean(axis=1)-trans_proc_fee
#daily_returns_strat = avg_long_ret.dropna(how='all').fillna(0) #+avg_short_ret
#
##avg_daily_rets  = daily_returns_strat.mean(axis=1)
#
##Cumulative returns 
##cum_ret =starting_capital +  np.cumsum(daily_returns_strat) #
#cum_ret =(1 + daily_returns_strat).cumprod()
##cum_long_ret =  (1 + avg_long_ret).cumprod()
##cum_short_ret =  (1 + avg_short_ret).cumprod()
#
#
############################################
##stats for basic strategy
###########################################
#
#print("   ")
#print('Short term reversal REAL ESTATE')
#mean_ret = cum_ret.tail(1)**(1/7)-1
#print("CAGR " + str(mean_ret[0]))
#vol = (daily_returns_strat.std()*math.sqrt(252))
#sharpe = mean_ret/vol
#kelly_f = mean_ret/vol**2
#print("Volatility " + str(vol))
#print("Sharpe " + str(sharpe[0]))
#print("Kelly fraction " + str(kelly_f[0]))
##maxiumum drawdown
#Roll_Max = cum_ret.cummax()
#Daily_Drawdown = cum_ret/Roll_Max - 1.0
#Max_Daily_Drawdown = Daily_Drawdown.cummin()
#print("Max drawdown " + str(Max_Daily_Drawdown.tail(1)[0]))
#
##plots
#plt.plot(cum_ret)
##plt.plot(cum_long_ret)
##plt.plot(cum_short_ret)
##plt.plot(Daily_Drawdown)
#
#
####################################################
##modified strategy considering factor momentum
#####################################################
#mom_cum_ret = (1+daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0]).cumprod()
##mom_cum_ret = starting_capital + np.cumsum(daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0])
#mom_daily_ret_RE = mom_cum_ret.pct_change()
#
#
#mom_mean_ret = mom_cum_ret.tail(1)**(1/7)-1
#
#mom_vol = (daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0].std()*math.sqrt(mom_cum_ret.count()/7))
#mom_sharpe = mom_mean_ret/mom_vol
#mom_kelly_f = mom_mean_ret/mom_vol**2
#
##maxiumum drawdown
#mom_Roll_Max = mom_cum_ret.cummax()
#mom_Daily_Drawdown = mom_cum_ret/mom_Roll_Max - 1.0
#mom_Max_Daily_Drawdown = mom_Daily_Drawdown.cummin()
#print("   ")
#print('Short term reversal with factor momentum')
#print("CAGR " + str(mom_mean_ret[0]))
#print("Volatility " + str(mom_vol))
#
#print("Sharpe " + str(mom_sharpe[0]))
#print("Kelly fraction " + str(mom_kelly_f[0]))
##maxiumum drawdown
#Roll_Max = cum_ret.cummax()
#Daily_Drawdown = cum_ret/Roll_Max - 1.0
#Max_Daily_Drawdown = Daily_Drawdown.cummin()
#print("Max drawdown " + str(mom_Max_Daily_Drawdown.tail(1)[0]))
#
##calculate log returns st reversal momentum strategy and print returns per year
#mom_log_ret_RE = np.log(mom_cum_ret)-np.log(mom_cum_ret.shift(1))
#per = mom_log_ret_RE.index.to_period("Y")
#g = mom_log_ret_RE.groupby(per)
#ret_per_year = g.sum()
#print("   ")
#print("st reversal Real Estate with factor momentum returns per year")
#print(ret_per_year)
#
#
#per_M = mom_log_ret_RE.index.to_period("M")
#grouping_month = mom_log_ret_RE.groupby(per_M)
#ret_per_month = grouping_month.sum()
##stats for monthly returns
#percent_positive = ret_per_month[ret_per_month>0].count()/ret_per_month.count()
#print("")
#print("percent positive months " + str(percent_positive))
#
#
#plt.plot(mom_cum_ret)
#
#################
##buy and hold
##################
#
#avg_ret_boh= ret_daily.mean(axis=1)
#cum_ret_boh =  (1 + avg_ret_boh).cumprod()
##avg_ret_boh= starting_capital*ret_daily.mean(axis=1)
##cum_ret_boh =  starting_capital + np.cumsum(avg_ret_boh)
#plt.plot(cum_ret_boh)
#
##stats buy and hold
#print("   ")
#print('Buy and hold stats')
#boh_mean_ret = cum_ret_boh.tail(1)**(1/7)-1
#boh_vol = (avg_ret_boh.std()*math.sqrt(252))
#boh_sharpe = boh_mean_ret/boh_vol
#boh_kelly_f = boh_mean_ret/boh_vol**2
#
##maxiumum drawdown
#boh_Roll_Max = cum_ret_boh.cummax()
#boh_Daily_Drawdown = cum_ret_boh/boh_Roll_Max - 1.0
#boh_Max_Daily_Drawdown = boh_Daily_Drawdown.cummin()
#
#
#
#print("CAGR " + str(boh_mean_ret[0]))
#print("Volatility " + str(boh_vol))
#
#print("Sharpe " + str(boh_sharpe[0]))
#print("Kelly fraction " + str(boh_kelly_f[0]))
#
#print("Max drawdown " + str(boh_Max_Daily_Drawdown.tail(1)[0]))
#
#
#
#
#
#print("   ")
#print('20-day momentum of short term reversal REAL ESTATE strategy')
#print(cum_ret.pct_change(20).tail(1))
#
#

