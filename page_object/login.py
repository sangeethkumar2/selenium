import os,sys
sys.path.append(os.getcwd())
from config.variable import *
from config.xpath import *
from config.common import Common

class Login():

    def __init__(self):
        self.username_input_name = "lusername"
        self.password_input_name = "lpassword"

    def _login(self,username=username,password=password):
        Common()._open_url()
        Common()._do_sendkeys('name',self.username_input_name,username)
        Common()._do_sendkeys('name',self.password_input_name,password)
        Common()._do_click('name','login')

if __name__ == '__main__':
    pass
