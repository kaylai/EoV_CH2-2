# Python 3.5
# Script for MetalSilicate python library
# Copyright Kayla Iacovino
"""
This script contains optical basicity values from Table 4 of Leboutellier A, Courtine P (1998) 
Improvement of a bulk optical basicity table for oxidic systems. J Solid State Chem 137:94–103. 
https://doi.org/10.1006/jssc.1997.7722
"""
import pandas as pd

# These hard-coded pandas DataFrames are generated from an Excel Spreadsheet and hardcoded for 
# easier access.
"""
The code to generate these:
import pandas as pd
import numpy as np
optical_basicity = pd.read_excel('optical_basicity.xlsx',)
optical_basicity.fillna("No Data")

import math
f= open("opticalbasicity.py","w+")
cols = ['Phase', 'Coordination', 'Lambda']

f.write("\n")
f.write("optical_basicity = pd.DataFrame({ \n")
for col in cols:
	iterno = 1
	f.write("'" + (str(col)+"': ["))
	for index, row in optical_basicity.iterrows():
		try:
			value = float(row[col])
			if str(value) == 'nan':
				f.write("'No Data'")
			else:
				f.write(str(value))
		except:
			f.write("'" + str(row[col]) + "'")
		if iterno < len(optical_basicity.index):
			f.write(",")
		iterno += 1
	f.write("], \n")
f.write(" }).set_index('Phase') \n")


##NOTE! Delete the final comma at the end of the final column.

##Reminder: to look up a value, use syntax: optical_basicity.loc['P2O5']['Lambda']
"""

optical_basicity = pd.DataFrame({ 
'Phase': ['CO2','P2O5','H2O','B2O3','Mg2P2O7','SiO2','Li2O','BeO','VOPO4','VPO4.75','(VO)2P2O7',
		  'FePO4','Ni2P2O7','H4PVMo11O40','Mn2P2O7','WO3','Co2P2O7','MoO3','Fe2P2O7','GeO2',
		  'Mo16V4Nb2O63','Cu2P2O7','Zn2P2O7','CuO','NiMoO4 + MoO3','NiMoO4 + MoO3',
		  'NiMoO4 + 0.25 MoO3','Al2O3','Fe2(MoO4)3','Nb2O5','NiMoO4 + 0.25 MoO3','NiMoO4 b.t',
		  'V2O5','CoMoO4','NiMoO4 h.t','Mo2O5/4MoO3/2V2O5/Nb2O5','Mo18O52','CeO2','BiPO4','CoMoO4',
		  'La2O3','VO2','V6O13','Bi2Mo3O12','1V2O5/1TiO2','CrVO4','Cr2O3','MgCr2O4','MnCr2O4',
		  'ZrO2','Mg2V2O7','CoCr2O4','Y2O3','Mg3V2O8','0.1V2O5 + 0.9TiO2','Bi2Mo2O9','Mo5O14',
		  '0.0234V2O5','0.0234V6O13','TiO2','CuCr2O4','Ni2V2O7','Ce2O3','NiFe2O4','Mn2V2O7','Fe2O3',
		  'Co2V2O7','RhVO4','MgO','CoFe2O4','FeAsO4','La2CuO4','Fe3O4','BiMoO4','CoMn2O4','Cu2V2O7',
		  'Zn2V2O7','Mn2O3','CuFe2O4','BiVO4/1.9MgO','Zn3V2O8','PdO','Bi2MoO6','SnO2','BiVO4',
		  'MnO2','FeSbO4','Fe4Bi2O9','NiO','ZnO','MnO','Sb2O4 + SnO2','MoO2','USb3O10','Cu2O',
		  'Sb2O5','CoO','CaO','FeO','Tl2O3 + epDy2O3','alphSb2O4','SrO','CdO','Na2O','Bi2O3','BaO',
		  'Ag2O','K2O','Rb2O','Cs2O'], 
'Coordination': ['No Data','P_4^5+','No Data','B_4^3+','Mg_6^2+, P_4^5+','Si^4+ 4','Li^+ 4',
				 'Be^2+ 6','V_6^5+, P_4^5+','0.5V^4+ 0.5V^5+','V_6^4+, P_4^5+','Fe_6^3+, P_4^5+',
				 'Ni_6^2+, P_4^5+','P_4^5+, V^5+, Mo_6^6+','Mn_6^2+, P_4^5+','W_6^6+',
				 'Co_6^2+,P_4^5+','Mo_6^6+','Fe_6^2+, P_4^5+','Ge_6^4+','Mo_6, V_6, Nb_6',
				 'Cu_6^2+, P_4^5+','Zn_6^2+, P_4^5+','Cu_4^2+ s.q','NiMoO4 l.t','NiMoO4 h.t.',
				 'NiMoO4 l.t.','Al_6^3+','Fe_6^3+, Mo_4^6+','Nb_6^5+','NiMoO4 h.t.',
				 'Ni_6^2+, Mo_6^5+','V_6^5+','Co_6^2+, Mo_6^6+','Ni_6^2+, Mo_4^6+',
				 'Mo_6^5+, Mo_6^6+, V_6^4+, Nb_6^5+','14Mo_6^6+, 4Mo_6^5+','Ce_8^4+',
				 'Bi_6^3+, P_4^5+','Co_6^2+, Mo_4^6+','La_7^3+','V_6^4+','4V_6^4+, 2V_6^5+',
				 'Bi_6^3+, Mo_6^6+','TiO2 rutile','Cr_6^3+, V_4^5+','Cr_6^3+, V_4^5+',
				 'Mg_4^2+, Cr_6^3+','Mn_4^2+, Cr_6^3+',
				 'Zr_8^4+ (monoclinic) or Zr_7^4+ (tetragonal)','Mg_6^2+, V_4^5+',
				 'Co_4^2+, Cr_6^3+','Y_6^3+','Mg_6^2+, V_4^5+','No Data','Bi_6^3+, Mo_6^6+',
				 'Mo_6, 7, or 8^6+','+ 0.976TiO2','+ 0.976TiO2','Ti_6^4+','Cu_4^2+, Cr_6^3+',
				 'Ni_6^2+, V_4^5+','Ce_7^3+','Ni_6^2+, Fe_4/6^3+','Mn_6^2+, V_4^5+','Fe_6^3+',
				 'Co_6^2+, V_4^5+','Rh_6^3+, V_4^5+','Mg_6^2+','Co_6^2+, Fe_4/6^3+',
				 'Fe_6^3+, As_4^5+','La_8^3+, Cu_6^2+','Fe_4/6^3+, 1Fe_6^2+',
				 'Bi_6^3+, Mo_4^5+','Co_4^2+, Mn_6^3+','Cu_6^2+, V_4^5+','Cu_6^2+, V_4^5+',
				 'Mn_6^3+','Cu_6^2+, Fe_4/6^3+','No Data','Zn_6^2+, V_4^5+','Pd_4^2+ p.c.',
				 'Bi_4^3+, Mo_6^6+','Sn_6^2+','Bi_6^3+, V_4^5+','Mn_6^4+','Fe_6^3+, Sb_6^5+',
				 'Bi_6^3+, Fe_6^3+','Ni_6^2+','Zn_4^2+','Mn_6^2+','No Data','Mo_6^4+','U^5+, Sb^5+',
				 'Cu_2^+','Sb_6^5+','Co_6^2+','Ca_6^2+','Fe_6^2+','Tl_6^3+b','Sb_4^3+, Sb_6^5+',
				 'Sr_6^2+','Cd_6^2+','Na_4^+','Bi_6^3+','Ba_6^2+','Ag_2^+','K_4^+','Rb_4^+c',
				 'Cs_3^+c'], 
'Lambda': [0.3,0.33,0.4,0.42,0.46,0.48,0.48,0.48,0.48,0.49,0.49,0.5,0.5,0.5,0.51,0.51,0.52,0.52,
		   0.55,0.54,0.54,0.55,0.55,0.56,0.57,0.58,0.6,0.6,0.61,0.61,0.62,0.62,0.63,0.64,0.64,0.64,
		   0.65,0.65,0.65,0.66,0.68,0.68,0.68,0.69,0.69,0.69,0.7,0.71,0.71,0.71,0.72,0.72,0.72,0.72,
		   0.74,0.74,0.75,0.75,0.75,0.75,0.75,0.75,0.76,0.76,0.77,0.77,0.77,0.78,0.78,0.78,0.79,
		   0.79,0.79,0.79,0.8,0.81,0.81,0.81,0.81,0.81,0.84,0.85,0.86,0.87,0.88,0.88,0.9,0.91,0.91,
		   0.92,0.96,0.96,0.96,0.97,0.98,0.98,0.98,1.0,1.0,1.03,1.05,1.1,1.12,1.15,1.19,1.2,1.25,
		   1.4,1.51,1.7] 
 }).set_index('Phase') 
