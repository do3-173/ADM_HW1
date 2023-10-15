regex_pattern = r"^M{0,3}(CD|D?C{0,3}|CM)(XL|L?X{0,3}|XC)(IV|V?I{0,3}|IX)$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))