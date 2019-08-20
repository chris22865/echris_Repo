import re

# the dictionary where all the list values will be stored
clinic_info = {}

# all the lists you'll need to store key,values
clinic_names = []
clinic_num = []
clinic_addr = []

# a counter when prompting the user to input keys to look up in dictionary
count = 0

# open the txt file to access it, use 'r' to read it all
file = open('StatesboroClinicInfo.txt', 'r')

for line in file:
    # within the txt file exists extra lines detailing num of doctors and reviews
    # these lines become a problem when parsing and storing, therefore conditions are needed to skip them
    # the below if statement skips those lines which occur several times in the 20 clinic list
    if re.search('(-.Medical clinic)|(-.Doctor)|(No reviews.-)', line): # the '|' is used to create an OR condition within the re.search
        # use 'continue' to skip these conditions when met
        continue
    # search for clinic names in txt file
    elif re.search(':(.*$)', line):
        name = re.findall(': (.*$)', line) # the findall string is extremely case sensitive, account for spaces
        name = ''.join(name)
        clinic_names.append(name)
        # print(clinic_names.count(name))
        #print(name)
    # search for clinic phone numbers in txt file
    elif re.search('\d{3}.*\d{3}.*\d{4}.*', line):
        # the parentheses in each num group captures each individually and turns it into a tuple
        # the parentheses pulls out the numbers to get rid of any random spaces, etc
        num = re.findall('(\d{3}).*(\d{3}).*(\d{4}).*', line) # use {} to limit amount of numbers to capture
        num = '-'.join(num[0])
        clinic_num.append(num)
        #print(num)
    # search for clinic address in txt file
    elif re.search('.*-', line):
        addr = re.findall('. -\s*(.*$)', line)
        addr = ''.join(addr)
        clinic_addr.append(addr)
        #print(addr)


for name,addr,num in zip(clinic_names, clinic_addr, clinic_num):
    clinic_info[name] = [addr, num]
    count += 1
print(clinic_info)

# print total count
print('\n')
print('The total items in the dictionary is: ', str(count) + '\n')

while True:
    n = input("Please input the query clinic provider's name: ")
    if n in clinic_info:
        info = clinic_info.get(n, 0)
        # gets first element(the addr) from value in dictionary
        print(n + ' address => ' + str(info[0]))
        # gets second element(the num) from value in dictionary
        print(n + ' phone => ' + str(info[1]))
        break
    else:
        print("Please correct the provider's name and try again")
