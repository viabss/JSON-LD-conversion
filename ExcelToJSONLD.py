import pandas as pd
import json
import os
debug=True

drive = 'I:\\'
subFolder_1 = 'General'
subFolder_2 = 'Normalized Files'
subFolder_3_input = 'Normalized Input'
subFolder_3_output = 'Normalized Output'

def altLabelDict(raw_Data = pd.DataFrame()):
    debug=False
#    DO NOT USE .fromkeys to initialize the dictionary as it creates one object for all values! In essence
#    the empty list that we create for all keys is actually shared by them all.
    altlabel_Key = {k:[] for k in raw_Data['prefLabel']} #The dictionary to store the altLabels for each prefLabel
    for key,values in altlabel_Key.items():
        for rows in raw_Data.itertuples(index=False):
            if rows.prefLabel in key:
                altlabel_Key[key].append(rows.altLabel.strip())
            else:
                continue
    if debug:
        print('[DEBUG]\n')
        print(altlabel_Key)
    return altlabel_Key
               

def create_JSONLD(id_Seed,altlabel_Dict={}):
    debug = False
    norm_JSON_record = {} #The final JSON-LD dictionary for each record
    norm_JSON_list = [] #The list of all records in the norm_JSON
    norm_JSON={}
    for key,values in altlabel_Dict.items():
        id_string = ('00000000'+str(id_Seed))[len('00000000'+str(id_Seed))-9:] #The ID should be of the form MFGxxxxxxxxx
        keys = ['@context','@type','@id','additionalType','prefLabel','altLabels'] 
        values = ['http://schema.org','Corporation','MFG'+id_string,'Manufacturer',key,values]
        norm_JSON_record = {key:values for key,values in zip(keys,values)}
        norm_JSON_list.append(norm_JSON_record)
        id_Seed+=1
    norm_JSON['corporations']= norm_JSON_list
    if debug:
        print('[DEBUG]\n')
        print(norm_JSON)
    return(norm_JSON)

def import_file(folder):
    debug=False
    file_in = 'Manufacturer Normalization.xlsx'
    full_path = os.path.join(drive,subFolder_1,subFolder_2,subFolder_3_input,folder,file_in)
    raw_Data=pd.DataFrame()
    try:
        raw_Data = pd.read_excel(full_path,header = 0,sheetname='Raw Data',parse_cols = [1,2,3,4],names = ('altLabel','prefLabel','IsNormalized','IsCorrect'))
        if debug:
            print('[DEBUG]\n')
            print(raw_Data.loc[(raw_Data['IsCorrect']==False)&(raw_Data['IsNormalized']=='Y')])
        return(raw_Data.loc[(raw_Data['IsCorrect']==False)&(raw_Data['IsNormalized']=='Y')])
    except IOError:
        print("File does not exist in the location")
        return 0
    
def export_file(norm_JSON,folder):
    file_out = 'norm_JSON.json'
    full_path = os.path.join(drive,subFolder_1,subFolder_2,subFolder_3_output,folder,file_out)
    path_dir = os.path.join(drive,subFolder_1,subFolder_2,subFolder_3_output,folder)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    with open(full_path,'w+') as file:
        json.dump(norm_JSON,file,indent=4)


        
def main():
    raw_Data = pd.DataFrame()
    altlabel_Dict = {}
    norm_JSON = {}
    folder = input("Please enter the file Date Stamp of the form [YYYYDDMM]:")
    raw_Data = import_file(folder)
    id_Seed = int(input('Please enter the seed for the ID(+1 to the last ID):'))
    altlabel_Dict = altLabelDict(raw_Data[['prefLabel','altLabel']])
    norm_JSON = create_JSONLD(id_Seed,altlabel_Dict)
    export_file(norm_JSON,folder)
    
    
main()
    

    



    


    
    
    






    

                
    
