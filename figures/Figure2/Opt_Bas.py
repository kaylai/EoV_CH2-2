import opticalbasicity as ob
import VESIcal as v

def calc_optical_basicity(sample):
	"""
	Calculates the optical basicity of a sample based on composition. Uses optical basicity values
	from Table 4 of Leboutellier A, Courtine P (1998) Improvement of a bulk optical basicity table
	for oxidic systems. J Solid State Chem 137:94–103. https://doi.org/10.1006/jssc.1997.7722

	Uses method after Crisp, L.J. and Berry, A.J. (2022) A new model for zircon saturaiton in
	silicate melts. Contributions to Mineralogy and Petrology, 177:71.
	https://doi.org/10.1007/s00410-022-01925-6

	Lambda = Sigma(m_i*n_i*Lambda_i)/Sigma(m_i*n_i)
	where m_i is the number of moles of each oxide, n_i is the number of oxygens in the oxide (for
	example 3 for Al2O3), and Lambda_i is the optical basicity coefficient of each oxide from
	Table 4 of Leboutellier and Courtine (1998). The optical basicity for all Fe-bearing melt
	compositions here is calculated assuming Fe 3+ /ΣFe = 0, (where ΣFe = Fe 2+ + Fe 3+ ).

	Parameters
	----------
	sample: VESIcal Sample object

	Returns
	-------
	float
		Optical basicity value, Lambda.	
	"""
	oxides_for_calc = ob.optical_basicity.index.tolist()

	# STEP 1: Convert to mole fraction
	sample_X = sample.get_composition(units='mol_oxides')

	# STEP 2: Calculate numerator
	numer_sum = 0
	for ox, val in sample_X.items():
		if ox in oxides_for_calc:
			numer = val * v.core.OxygenNum[ox] * ob.optical_basicity.loc[ox]['Lambda']
			numer_sum += numer
		else:
			pass

	# STEP 3: Calculate denominator
	denom_sum = 0
	for ox, val in sample_X.items():
		if ox in oxides_for_calc:
			denom = val * v.core.OxygenNum[ox]
			denom_sum += denom
		else:
			pass

	# STEP 4: divide
	optical_bas = numer_sum / denom_sum

	return optical_bas

def batch_calc_optical_basicity(batchfile):
	"""
	Calculates the optical basicity of a sample based on composition. Uses optical basicity values
	from Table 4 of Leboutellier A, Courtine P (1998) Improvement of a bulk optical basicity table
	for oxidic systems. J Solid State Chem 137:94–103. https://doi.org/10.1006/jssc.1997.7722

	Uses method after Crisp, L.J. and Berry, A.J. (2022) A new model for zircon saturaiton in
	silicate melts. Contributions to Mineralogy and Petrology, 177:71.
	https://doi.org/10.1007/s00410-022-01925-6

	Lambda = Sigma(m_i*n_i*Lambda_i)/Sigma(m_i*n_i)
	where m_i is the number of moles of each oxide, n_i is the number of oxygens in the oxide (for
	example 3 for Al2O3), and Lambda_i is the optical basicity coefficient of each oxide from
	Table 4 of Leboutellier and Courtine (1998). The optical basicity for all Fe-bearing melt
	compositions here is calculated assuming Fe 3+ /ΣFe = 0, (where ΣFe = Fe 2+ + Fe 3+ ).

	Parameters
	----------
	sample: VESIcal BatchFile  object

	Returns
	-------
	float or dict
		If metadata=False (default), returns float of NBO/T value
		If metadata=True, returns dict with keys #TODO add keys here
	"""
 
	sample_names = batchfile.get_data().index
	file_df = batchfile.get_data()

	ob_val_list = []
	for samp in sample_names:
		mysample = batchfile.get_sample_composition(samp, asSampleClass=True)
		ob_val = calc_optical_basicity(mysample)
		ob_val_list.append(ob_val)
	file_df['Optical_Basicity'] = ob_val_list
 
	file_new_bf = v.BatchFile_from_DataFrame(file_df)
 
	return file_new_bf