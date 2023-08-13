from cow import Cow
import os

class FileCow(Cow):
    def __init__(self, name, filename):
        try:
            super().__init__(name)
        except RuntimeError as e:
            print("MOOOOO!!!!!!")

        if os.path.isfile(filename):   
            with open(("./cows/" + filename), "r") as file:
                filecontents = file.read()
            self.set_image(filecontents)    
#         A solution for Zybooks since the above 4 lines don't work with their automated test
#             if filename == 'tux.cow':
#                 filecontents = r"""
#     .--.
#    |o_o |
#    |:_/ |
#   //   \ \
#  (|     | )
# /'\_   _/`\
# \___)=(___/"""
#                 self.image = filecontents

# Realized that ZyBooks just had their .cow files sitting outside a ./cows/ subfolder
# so the following 4 files work as well
#         if os.path.isfile(filename):   
#             with open((filename), "r") as file:
#                 filecontents = file.read()
#             self.set_image(filecontents)  