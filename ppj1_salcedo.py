import re
import pandas as pd
import xlsxwriter

# the dictionary where all the list values will be stored
clinic_data = {}

# all the lists you'll need to store key,values
clinic_names = []
clinic_num = []
clinic_addr = []

# a counter when prompting the user to input keys to look up in dictionary
count = 0

# open the txt file to access it, use 'r' to read it all
file = open('ColoradoClinics.txt', 'r')

for line in file:
    # within the txt file exists extra lines detailing num of clinics offices
    # these lines become a problem when parsing and storing, therefore conditions are needed to skip them
    # the below if statement skips those lines which occur several times in the 20 clinic list
    if re.search('(-.Medical clinic)|(-.Doctor)|(No reviews.-)', line):  # the '|' is used to create an OR condition
        # use 'continue' to skip these conditions when met
        continue

    # search for clinic names in txt file
    elif re.search(':(.*$)', line):
        clinic = re.findall(': (.*$)', line)  # the findall string is extremely case sensitive, account for spaces
        clinic = ''.join(clinic)
        clinic_names.append(clinic)

    # search for clinic phone numbers in txt file
    elif re.search('\d{3}.*\d{3}.*\d{4}.*', line):
        # the parentheses in each num group captures each individually and turns it into a tuple
        # the parentheses pulls out the numbers to get rid of any random spaces, etc
        num = re.findall('(\d{3}).*(\d{3}).*(\d{4}).*', line)  # use {} to limit amount of numbers to capture
        num = '-'.join(num[0])
        clinic_num.append(num)

    # search for clinic address in txt file
    elif re.search('.*-', line):
        addr = re.findall('. -\s*(.*$)', line)
        addr = ''.join(addr)
        clinic_addr.append(addr)

for name, addr, num in zip(clinic_names, clinic_addr, clinic_num):
    clinic_data[name] = [name, addr, num]
    count += 1
    # set to force display of all columns as some of them hide in '...'
    pd.set_option('display.max_columns', None)
    # declaring pandas DataFrame var, cannot call more than two columns, look at comment in line 53
    df = pd.DataFrame.from_dict(clinic_data, orient='index', columns=['Clinic Name:', 'Address:', 'Contact Number:'])
print(clinic_data.values())

# print total count
print('\n')
print('The total items in the dictionary is: ', str(count) + '\n')

while True:
    n = input("Please input either:\n"
              "a. 'clinic name' for information\n"
              "b. 'export' to produce .xlsx file of data\n"
              "c. 'exit' to end program\n"
              "User Input:")
    if n in clinic_data:
        info = clinic_data.get(n, 0)
        # gets second element(the addr) from value in dictionary
        print(n + ' address => ' + str(info[1]))
        # gets third element(the num) from value in dictionary
        print(n + ' phone => ' + str(info[2]))
        # break
    # enter 'exit' in user input to end program
    elif n == 'exit':
        break
    # enter 'export' to get excel doc of dictionary data
    elif n == 'export':
        excel_fname = input('please write a filename for the excel doc \nNOTE: do not add file extension: \nFileName:')
        # we'll use a little bit of concatenation with addition to take care of the file extension in every runtime
        export_data = pd.ExcelWriter(excel_fname + '.xlsx', engine='xlsxwriter')
        df.to_excel(export_data, sheet_name='sheet1', index=False)
        export_data.save()
    else:
        print("Please correct the provider's name and try again")
print(df)
