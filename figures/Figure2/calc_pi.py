import VESIcal as v

def calc_Pi_parameter(sample):
	"""
	Calculates the Dixon Pi parameter.

	Parameters
	----------
	sample: VESIcal Sample object

	Returns
	-------
	float
		Pi
	"""
	samp_mol_cations = sample.get_composition(units='mol_cations')
	Pi_val = (
		-6.5 * (
			samp_mol_cations['Si'] + 
			samp_mol_cations['Al']
		) +
		20.17 * (
			samp_mol_cations['Ca'] +
			0.8 * samp_mol_cations['K'] +
			0.7 * samp_mol_cations['Na'] +
			0.4 * samp_mol_cations['Mg'] +
			0.4 * samp_mol_cations['Fe']
		)
	)

	return Pi_val

def batch_calc_Pi_parameter(batchfile):
	"""
	Calculates the Dixon Pi parameter.

	Parameters
	----------
	sample: VESIcal BatchFile object

	Returns
	-------
	VESIcal BatchFile object
	"""
 
	sample_names = batchfile.get_data().index
	file_df = batchfile.get_data()

	Pi_val_list = []
	for samp in sample_names:
		mysample = batchfile.get_sample_composition(samp, asSampleClass=True)
		Pi_val = calc_Pi_parameter(mysample)
		Pi_val_list.append(Pi_val)
	file_df['Pi_Parameter'] = Pi_val_list

	file_new_bf = v.BatchFile_from_DataFrame(file_df)

	return file_new_bf

