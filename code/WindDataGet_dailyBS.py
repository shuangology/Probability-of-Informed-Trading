import pandas as pd
import numpy as np
from WindPy import *
from tqdm import tqdm
w.start()
res = pd.DataFrame()
codelist = pd.read_table('../data/codelist.txt')
for code in tqdm(codelist.code):
	error,data1 = w.wsd(code, "mfd_buyamt_a,mfd_sellamt_a","2017-03-17","2019-07-10", "unit=1;traderType=1",usedf=True)
	data1.rename(columns = {'MFD_BUYAMT_A':'MFD_BUYAMT_A_1','MFD_SELLAMT_A':'MFD_SELLAMT_A_1'},inplace = True)
	error,data2 = w.wsd(code, "mfd_buyamt_a,mfd_sellamt_a","2017-03-17","2019-07-10", "unit=1;traderType=2",usedf=True)
	data2.rename(columns = {'MFD_BUYAMT_A':'MFD_BUYAMT_A_2','MFD_SELLAMT_A':'MFD_SELLAMT_A_2'},inplace = True)
	error,data3 = w.wsd(code, "mfd_buyamt_a,mfd_sellamt_a","2017-03-17","2019-07-10", "unit=1;traderType=3",usedf=True)
	data3.rename(columns = {'MFD_BUYAMT_A':'MFD_BUYAMT_A_3','MFD_SELLAMT_A':'MFD_SELLAMT_A_3'},inplace = True)
	error,data4 = w.wsd(code, "mfd_buyamt_a,mfd_sellamt_a","2017-03-17","2019-07-10", "unit=1;traderType=3",usedf=True)
	data4.rename(columns = {'MFD_BUYAMT_A':'MFD_BUYAMT_A_4','MFD_SELLAMT_A':'MFD_SELLAMT_A_4'},inplace = True)
	data = data1.join(data2,how = 'outer')
	data = data.join(data3,how ='outer')
	data =data.join(data4,how ='outer')
	data['code'] = code
	res = res.append(data)
    

res.to_table('../data/buy_sell_amt.txt')
w.stop()
