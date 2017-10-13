import pandas as pd
import json
debug=True
id_Seed = 1

path = 'C:\\Users\\viabs\\Documents\\Apps\\JSON-LD-conversion\\' 
file = 'Normalized TEST_python.xlsx' 

def altLabelDict(raw_Data = pd.DataFrame()):
    debug=False
#    DO NOT USE .fromkeys to initialize the dictionary as it creates one object for all values! In essence
#    the empty list that we create for all keys is actually shared by them all.
    altlabel_Key = {k:[] for k in raw_Data['prefLabel']} #The dictionary to store the altLabels for each prefLabel
    for key,values in altlabel_Key.items():
        for rows in raw_Data.itertuples(index=False):
            if rows.prefLabel in key:
                altlabel_Key[key].append('"{}"'.format(rows.altLabel.strip()))
            else:
                continue
    if debug:
        print('[DEBUG]\n')
        print(altlabel_Key)
    return altlabel_Key
               

def create_JSONLD(altlabel_Dict={}):
    debug = False
    global id_Seed 
    norm_JSON_record = {} #The final JSON-LD dictionary for each record
    norm_JSON_list = [] #The list of all records in the norm_JSON
    norm_JSON={}
    for key,values in altlabel_Dict.items():
        id_string = ('00000000'+str(id_Seed))[len('00000000'+str(id_Seed))-9:]
        keys = ['"{}"'.format('@context'),'"{}"'.format('@type'),'"{}"'.format('@id'),'"{}"'.format('additionaltype'),'"{}"'.format('prefLabel'),'"{}"'.format('altLabel')] 
        values = ['"{}"'.format('http://schema.org'),'"{}"'.format('Corporation'),'"{}"'.format('MFG'+id_string),'"{}"'.format('Manufacturer'),key,values]
        norm_JSON_record = {key:values for key,values in zip(keys,values)}
        norm_JSON_list.append(norm_JSON_record)
        id_Seed+=1
    norm_JSON['"{}"'.format('corporations')]= norm_JSON_list
    if debug:
        print('[DEBUG]\n')
        print(norm_JSON)
    return(norm_JSON)

def import_file():
    debug=False
    full_Path = path+file
    raw_Data=pd.DataFrame()
    try:
        raw_Data = pd.read_excel(full_Path,header = 0,sheetname='Raw Data',parse_cols = [1,2,3,4],names = ('altLabel','prefLabel','IsNormalized','IsCorrect'))
        if debug:
            print('[DEBUG]\n')
            print(raw_Data.loc[raw_Data['IsCorrect']==False])
        return(raw_Data.loc[raw_Data['IsCorrect']==False])
    except IOError:
        print("File does not exist in the location")
        return 0
    
def export_file(norm_JSON = {}):
    with open(file,'w') as outfile:
        json.dump(norm_JSON,outfile)
    
    
    
       

def main():
    raw_Data = pd.DataFrame()
    altlabel_Dict = {}
    norm_JSON = {}
    raw_Data = import_file()
    altlabel_Dict = altLabelDict(raw_Data[['prefLabel','altLabel']])
    norm_JSON = create_JSONLD(altlabel_Dict)
    export_file(norm_JSON)
    
    
main()
    

    



    


    
    
    






    

                
    
