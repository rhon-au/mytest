import re
sample = "From Jan 2018 till Nov 2018 I was learning python daily at 10:00 PM"

# '\W+' represent non alphanumeric character or group of charactors - spaces and ":" in this case
print(re.split('\W+',sample))

# Extract only the month and Year form the string and print it
regex=re.compile('(?P<month>\w{3})\s+(?P<year>[0-9]{4})')

for m in regex.finditer(sample):
    value = m.groupdict()
    print (m)
    print ("Month: "+value['month']+" , "+"Year: "+value['year'])

# to extract the time with AM or PM addition
regex=re.compile('\d+:\d+\s[AP]M')
m=re.findall(regex,sample)
print (m)