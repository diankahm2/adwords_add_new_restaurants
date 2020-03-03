string = "hello ; words ( Абылай Хана )"
print(string)
import re
#result = re.sub(r'[^A-Za-z]', '', string)
result = re.sub(r"(^| )[^ ]*[^A-Za-z ][^ ]*(?=$| )", "", string)
print(result)


