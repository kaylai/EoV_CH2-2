import VESIcal as v

def calc_NBO_T(sample, method=4, metadata=False):
	"""
	Calcultes the NBO/T (non-bridging oxygens over tetrahedrally coordinated ions) for a given
	composition. 

	Parameters
	----------
	sample: VESIcal Sample class object

	method: int
		Default is 4. Integer from 1 to 4 inclusive. Use to choose which NBO/T parameterization to
		use as defined here:
			1: NF = Si, Al-mixed, Ti
			2: NF = Si, Al-mixed, Ti, P
			3: NF = Si, Al-mixed, Fe, Ti, P
			4: NF = Si, Al-mixed, Fe, Cr3+, Ti, P

	metadata: bool
		Default is False. If set to true, a dict is returned with more information calculated about
		the sample.

	Returns
	-------
	float or dict
		If metadata=False (default), returns float of NBO/T value
		If metadata=True, returns dict with keys #TODO add keys here
	"""
	oxides_for_calc = ["SiO2", "TiO2", "Al2O3", "FeO", "MgO", "CaO",
						"Na2O", "K2O", "MnO", "P2O5"]

	#S Convert to mole fraction
	sample_X = sample.get_composition(units='mol_oxides')
	atoms = sample.get_composition(units='mol_singleO')

	# CALCULATE METADATA
	Mg_number = (100*atoms["Mg"]/(atoms["Mg"]+atoms["Fe"]))
	alkalinity_index = (atoms["Na"]+atoms["K"])/atoms["Al"]

	if atoms["Al"] < (atoms["Ca"]+atoms["Na"]+atoms["K"]) and atoms["Al"] > (atoms["Na"]+atoms["K"]):
		metaluminous = True
	else:
		metaluminous = False

	if atoms["Al"] > atoms["Ca"] + atoms["Na"] + atoms["K"]:
		peraluminous = True
	else:
		peraluminous = False

	if atoms["Al"] < atoms["Na"] + atoms["K"]:
		peralkaline = True
	else:
		peralkaline = False

	# Calculate NBO/T
	sum_atoms = sum(atoms)

	if method == 3:
		atoms["Cr"] = 0
	if method == 2:
		atoms["Cr"] = 0
		atoms["Fe"] = 0
	if method == 1:
		atoms["P"] = 0

	a_alpha = (atoms["Fe"]+atoms["Al"])
	a_beta = ((atoms["K"]+atoms["Na"]+0.5*(atoms["Fe"]+atoms["Mg"]+atoms["Mn"] +
			   (atoms["Ca"]-1.5*atoms["P"]))))
	if a_alpha > a_beta:
		a = a_beta
		b = a_alpha - a_beta
	else:
		a = a_alpha
		b = 0

	if sum_atoms < a_alpha:
		NBO_over_T = (1/(atoms["Si"]+atoms["Ti"]+atoms["P"]+(a*b*3+atoms["Fe"]*2+atoms["Mg"]*2 + 
						(atoms["Ca"]-(atoms["P"]*1.5)-(0.5*((a_alpha)-atoms["Na"]-atoms["K"])))*
						2+atoms["Mn"]*2)))
	else:
		NBO_over_T = (1/(atoms["Si"]+atoms["Ti"]+atoms["Al"]+atoms["Fe"]+atoms["P"])*
						(atoms["Fe"]*2+atoms["Mg"]*2+(atoms["Ca"]-(atoms["P"]*1.5))*2+
						(atoms["Na"]+atoms["K"]-atoms["Al"]-atoms["Fe"])+
						atoms["Mn"]*2))

	if metadata == True:
		return {"NBO/T": NBO_over_T,
				"Mg#": Mg_number,
				"Alkalinity Index": alkalinity_index,
				"Metaluminous": metaluminous,
				"Peraluminous": peraluminous,
				"Peralkaline": peralkaline}
	else:
		return NBO_over_T

def batch_calc_NBO_T(batchfile, method=4, metadata=False):
	"""
	Calcultes the NBO/T (non-bridging oxygens over tetrahedrally coordinated ions) for a given
	composition. 

	Parameters
	----------
	sample: VESIcal BatchFile  object

	method: int
		Default is 4. Integer from 1 to 4 inclusive. Use to choose which NBO/T parameterization to
		use as defined here:
			1: NF = Si, Al-mixed, Ti
			2: NF = Si, Al-mixed, Ti, P
			3: NF = Si, Al-mixed, Fe, Ti, P
			4: NF = Si, Al-mixed, Fe, Ti, P

	metadata: bool
		Default is False. If set to true, a dict is returned with more information calculated about
		the sample.

	Returns
	-------
	float or dict
		If metadata=False (default), returns float of NBO/T value
		If metadata=True, returns dict with keys #TODO add keys here
	"""
 
	sample_names = batchfile.get_data().index
	file_df = batchfile.get_data()

	NBOT_val_list = []
	for samp in sample_names:
		mysample = batchfile.get_sample_composition(samp, asSampleClass=True)
		NBOT_val = calc_NBO_T(mysample, method=method, metadata=metadata)
		NBOT_val_list.append(NBOT_val)
	file_df['NBOT'] = NBOT_val_list
 
	file_new_bf = v.BatchFile_from_DataFrame(file_df)
 
	return file_new_bf