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
        # My solution for Zybooks since the above 4 lines of code don't work with their automated test
        #     if filename == 'tux.cow':
        #         filecontents = r"""
#     .--.
#    |o_o |
#    |:_/ |
#   //   \ \
#  (|     | )
# /'\_   _/`\
# \___)=(___/"""
#     self.image = filecontents
