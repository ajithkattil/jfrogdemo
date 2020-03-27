# This Python script will generate a report of most popular and second most popular jars in the artifactory server
# The Artifactory server path and API Key need to be supplied as arguments to the script
########################################################################################################
import sys
import json
from artifactory import ArtifactoryPath
from pprint import pprint

#aql = ArtifactoryPath("http://35.193.65.132/artifactory", apikey="AKCp5ekmesKJi3ccYGVL5EAxGTtwvQyHwKrkQ9jH3D4KFdL91BLERDphTXjSAPJMp2x3zwXTC")# path to artifactory, NO repo
#print ("The script has the name %s" % (sys.argv[0])")
# Count the arguments
#arguments=len(sys.argv) - 1
#print ("The script is called with %i arguments" % (arguments))

#art_url=sys.argv[1]
#apikey=sys.argv[2]
art_url="http://jfrog.local/artifactory"
key="AKCp5ekmesKJi3ccYGVL5EAxGTtwvQyHwKrkQ9jH3D4KFdL91BLERDphTXjSAPJMp2x3zwXTC"
aql = ArtifactoryPath("http://35.193.65.132/artifactory", apikey="AKCp5ekmesKJi3ccYGVL5EAxGTtwvQyHwKrkQ9jH3D4KFdL91BLERDphTXjSAPJMp2x3zwXTC")# path to artifactory, NO repo
#aql = ArtifactoryPath(art_url."/artifactory", apikey=key)# path to artifactory, NO repo

artifacts = aql.aql("items.find()", ".include", ["name","stat.downloads"])
# The following steps will filter the artifacts list and give a list of only jars

jarlistall=[]
for artifactdetails in artifacts:
    for key, value in artifactdetails.items():
        count = 0
        if "jar" in value:
            jarlistall.append(artifactdetails)
#print (jarlistall)
total_jars=len(jarlistall)
print("total_jars=", total_jars)

#The following steps will provide a list of jar names and stats
jardownloadlist=[]
for jardetails in jarlistall:
   for key, value in jardetails.items():
       jarname=jardetails["name"]
       downloads=jardetails["stats"]
       dict={jarname:downloads}
       jardownloadlist.append(dict)

# A list of dictionaries with each dictionary having two items
#sample list item:-  {'multi1-3.7-20190715.221341-10.jar': [{'downloads': 0}]}

# The following steps will create a dictionary with key as jar name and value
# as number of downloads
# This will make it easy to do dictionary manipulation of dictionary values

jardict={}
for jardownloaddetails in jardownloadlist:
    for key, value in jardownloaddetails.items():
        dictvalue=value[0]
        downloadvalue=dictvalue['downloads']
        #print (downloadvalue)
        dictitem={key:downloadvalue}
        jardict[key] = downloadvalue
#print(jardict)
print('*********************************************************')
max = max(jardict.values())
# iterate through the dictionary
print(f'The highest no of downloads is  {max}.')
max2 = 0
for v in jardict.values():
     if(v>max2 and v<max):
            max2 = v
# print the second largest value
print(f'second highest no of downloads is  {max2}.')

#print(f'The repository {art_url} has been queried and the highest download value is {max} and the second highest download value is {max2}.')
# This function will give the list of jars with a particular value of downloads
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

#######REPORTING ###############################################
mostpopularjars=getKeysByValue(jardict,max)
secondpopularjars=getKeysByValue(jardict,max2)
#pprint(mostpopularjars)
#print('*********************************************************')
print('*********************************************************')
#print(f'Second highest downloads is  {max2}. and the following are the jars')
#pprint(secondpopularjars)

# Create a dictionary with the jar details
combined_report_dict={'most popular jars': mostpopularjars, 'second most popular jars': secondpopularjars}
#print(combined_report_dict)

print("############Json report provided below############")
print(json.dumps(combined_report_dict, indent=2))
