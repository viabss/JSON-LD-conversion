import pandas as pd
debug=True
def altLabelDict(raw_Data = pd.DataFrame()):
    debug=False
#    DO NOT USE .fromkeys to initialize the dictionary as it creates one object for all values! In essence
#    the empty list that we create for all keys is actually shared by them all.
    altlabel_Key = {k:[] for k in raw_Data['prefLabel']} #The dictionary to store the altLabels for each prefLabel
    for key,values in altlabel_Key.items():
        for rows in raw_Data.itertuples(index=False):
            if rows.prefLabel in key:
                altlabel_Key[key].append(rows.altLabel)
            else:
                continue
    if debug:
        print('[DEBUG]\n')
        print(altlabel_Key)
    return altlabel_Key

           
def prefLabelDict(raw_Data = pd.DataFrame()):
    debug = False
    dedup_raw_Data = raw_Data.drop_duplicates(subset = 'prefLabel',keep = 'first',inplace = False)
    preflabel_Key = {k:[] for k in dedup_raw_Data['prefLabel']}
    for key,values in preflabel_Key.items():
        for rows in dedup_raw_Data.itertuples(index=False):
            if rows.prefLabel in key:
                preflabel_Key[key] = list(rows)
    if debug:
        print('[DEBUG]\n')
        print(preflabel_Key)
    return preflabel_Key
    
               
    

    
def import_file():
    debug=False
    altlabel_Dict = {}
    preflabel_Dict = {}
    path = 'C:/' 
    file = 'Normalized_TEST_python.xlsx' 
    full_Path = path+'/'+file
    raw_Data=pd.DataFrame()
    raw_Data = pd.read_excel(full_Path,header = 0)
    if debug:
        print('[DEBUG]\n')
        print(raw_Data[['prefLabel','altLabel']])
    altlabel_Dict = altLabelDict(raw_Data[['prefLabel','altLabel']])
    preflabel_Dict = prefLabelDict(raw_Data.drop('altLabel',axis = 1))
    return {'altLabel_key':altlabel_Dict,'prefLabel_key':preflabel_Dict}
    

def main():
    returns = {}
    returns = import_file()
    print(returns)
    
main()
    

    



    


    
    
    






    

                
    
