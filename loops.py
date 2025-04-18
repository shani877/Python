list_of_cloud = ["aws", "gcp", "azure", "oracle", "openshift"]
cloud = "aws" #variable

print(list_of_cloud)


list_of_cloud.append("salesforce")

list_of_cloud.append("alibaba")

print(list_of_cloud)


list_of_cloud.insert(3,"Heroku")
print(list_of_cloud)

#list index starts from "0"

#insert "Cloud" to 0th index of list

list_of_cloud.insert(0, "Cloud")
print(list_of_cloud)

print(len(list_of_cloud))

#append vs insert

#iteration

for cloud in list_of_cloud:
  print(cloud)

for i in range(1,11):
  print(i)
