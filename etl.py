def transform(legacy_data):
    new_data = {}
    try:
        for key, value in legacy_data.items(): #loop the key and value in legacy_data dict
            l_list = legacy_data[key] #put the value in l_list based on different keys

            for i in l_list: #loop the value in list
                new_data[i.lower()] = key #Turning values into keys
        return new_data
    except:
        raise Exception("Legacy data not same with data!")

