import pandas as pd
debug=True
def altLabelDict(raw_Data = pd.DataFrame()):
    debug=False
#    DO NOT USE .fromkeys to initialize the dictionary as it creates one object for all values! In essence
#    the empty list that we create for all keys is actually shared by them all.
    
    key = 'altlabel'
    altlabel_dict = dict.fromkeys(key)
    print(altlabel_dict)
    altlabel_Key = {k:[altlabel_dict] for k in raw_Data['prefLabel']} #The dictionary to store the altLabels for each prefLabel
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
            
#def prefLabelDict(raw_Data = pd.DataFrame()):
#    debug = False
#    preflabel_Key = {k:[] for k in raw_Data['prefLabel']}
    
               
    

    
def import_file():
    debug=False
    altlabel_Dict = {}
    path = 'C:/Users/viabs/Documents/Apps/JSON-LD' 
    file = 'Normalized_TEST_python.xlsx' 
    full_Path = path+'/'+file
    raw_Data=pd.DataFrame()
    raw_Data = pd.read_excel(full_Path,header = 0)
    if debug:
        print('[DEBUG]\n')
        print(raw_Data[['prefLabel','altLabel']])
    altlabel_Dict=altLabelDict(raw_Data[['prefLabel','altLabel']])
#    prefLabelDict(raw_Data)
    

def main():
    import_file()
    
main()
    

    



    


    
    
    






    

                
    
