import os

def prepare_files(project):
	# List files in the directory
	files = os.listdir(project + '/')

	#Start dic for clinical data
	clin_data = {}

	#Add clinical data for each sample to clin_data    
	with open(project + '.tsv','r') as texto:
		for line in texto:
			linha=line.split()
			if 'Category' not in line:
				clin_data[linha[0]] = linha[-1]
		    
	# Print the list of files
	tumor_count = 0
	norm_count = 0
	with open('Check.txt','w') as texto:
		texto.write('Folder,File')
	for file in files:
		if '.txt' not in file:
			if clin_data[file] == 'Normal':
				norm_count+=1
				name = 'Normal_'+str(norm_count)
				os.rename(project+'/'+file,project+'/'+name)          
			elif clin_data[file] == 'Tumor':
				tumor_count+=1
				name = 'Tumor_'+str(tumor_count)
				os.rename(project+'/'+file,project+'/'+name)
			directory_path = project+'/'+name			
			if os.path.isdir(directory_path):		
				data_files = [x for x in os.listdir(directory_path) if '.txt' not in x]
				old_file_name = data_files[0]
				new_file_name = name + '.tsv'
				old_file_path = os.path.join(directory_path, old_file_name)
				new_file_path = os.path.join(directory_path, new_file_name)
				os.rename(old_file_path, new_file_path)			       
					
def prepare_counts(project):
	files = [x for x in os.listdir(project + '/') if '.txt' not in x]
	for file in files:
		data = project+'/'+file+'/'+file+'.tsv'
		data_dic = {}			    	
		with open(data,'r') as texto:
			for line in texto:
				if 'protein_coding' in line:
					linha = line.split()
					data_dic[linha[1]] = linha[4]
		with open(project+'/'+file+'.tabular','w') as texto:
			texto.write('Gene,Counts')
			for key, value in data_dic.items():
				texto.write(f'\n{key},{value}')	
			
