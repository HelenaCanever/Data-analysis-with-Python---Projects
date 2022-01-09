import numpy as np

def calculate(list):
  #check list lenght
  if len(list) != 9:
    raise ValueError ("List must contain nine numbers.")

  else:
    #convert list to 3 by 3 array
    a_list = np.asarray(list)
    a_list = a_list.reshape((3,3))


    #define output dictionary (not dict, must have order)
    output = {"mean":[],"variance":[],"standard deviation":[],"max" : [],"min" : [],"sum" : []}

    #mean
    output["mean"].append((np.mean(a_list, axis=0)).tolist())
    output["mean"].append((np.mean(a_list, axis=1)).tolist())
    output["mean"].append(np.mean(a_list))
    #variance
    output["variance"].append((np.var(a_list, axis=0)).tolist())
    output["variance"].append((np.var(a_list, axis=1)).tolist())
    output["variance"].append(np.var(a_list))
    #standard deviation
    output["standard deviation"].append((np.std(a_list, axis=0)).tolist())
    output["standard deviation"].append((np.std(a_list, axis=1)).tolist())
    output["standard deviation"].append(np.std(a_list))

    #max
    output["max"].append((np.amax(a_list, axis=0)).tolist())
    output["max"].append((np.amax(a_list, axis=1)).tolist())
    output["max"].append(np.amax(a_list))
    #min
    output["min"].append((np.amin(a_list, axis=0)).tolist())
    output["min"].append((np.amin(a_list, axis=1)).tolist())
    output["min"].append(np.amin(a_list))

    #sum
    output["sum"].append((np.sum(a_list, axis=0)).tolist())
    output["sum"].append((np.sum(a_list, axis=1)).tolist())
    output["sum"].append(np.sum(a_list))

    #print (output)
    return output
