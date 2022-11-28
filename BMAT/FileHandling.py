import csv  
    
# field names  
fields = ['Name', 'Branch', 'Year', 'CGPA']  
    
# data rows of csv file  
rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]  
    
# name of csv file  
filename = "university_records.csv"
    
 
with open(filename, 'w') as csvfile:  
   csvwriter = csv.writer(csvfile)  
   csvwriter.writerow(fields)  
   csvwriter.writerows(rows)