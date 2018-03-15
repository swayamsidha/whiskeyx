import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
whiskey = pd.read_csv("whiskey.csv")
whiskey["regions"] = pd.read_csv("region.txt")
#creating a dataframe of columns representing flavors
flavors = whiskey.iloc[:,2:14]
#finds the pearsons coefficient
cor_flav = pd.DataFrame.corr(flavors)
print(cor_flav)
plt.figure(figsize = (10,10))
plt.pcolor(cor_flav)
#includes the color bar in the graph
plt.colorbar()
#save as pdf
plt.savefig("cor_flav.pdf")
#coreletion among distilaries interms of whiskeys
cor_dist = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10,10))
plt.pcolor(cor_dist)
plt.axis("tight")
plt.colorbar()
plt.savefig("cor_dist.pdf")
#clustering whiskeys into groups of similarity in flavours
whiskey['Group'] = pd.Series(model.rows_lebels_,index=whiskey.index)
#Perform an indirect sort along the given axis
#returns an array of indices of the same shape as`a` that index data along the given axis in sorted order.
whiskey = whiskey.ix[np.argsort(model.rows_labels_)]
whiskey = whiskey.reset_index(drop=True)
#recalculate the correletion and capture in array
corrsf = pd.DataFrame(whiskey.iloc[:,2:14].transpose())
corrsf = np.array(corrsf)
plt.figure(figsize = (10,10))
plt.subplot(121)
plt.pcolor(cor_dist)
plt.axis("tight")
plt.title("original")
plt.subplot(122)
plt.pcolor(corrsf)
plt.axis("tight")
plt.title("rearranged")
plt.colorbar()
#in the graph whiskey belong to same block represents same taste
plt.savefig("cluster.pdf")
