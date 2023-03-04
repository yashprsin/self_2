import re
my_str = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place 
Landon SW1X 7HSc
Phone: 1234567890
Fax: 1234567890
Email: xyz@gamil.com
Website: www.xyz.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arglington, VA 22209-1911
USA
Phone: 1234567890
Fax: 1234567890
Email: xyz@gmail.com
Website: northamerica@tata.com
Directions: View map
'''
# functions - findall, search, split, sub, finditer
pat = re.compile(r'.')
# pat = re.compile(r'View')

ma = pat.finditer(my_str)
for match in ma:
    print(match)