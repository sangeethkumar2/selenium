import os,sys
sys.path.append(os.getcwd())
# from config.common import Common
from page_object.login import Login
from page_object.HomePage import Homepage

class Test():
    def test_sample(self):
        Login()._login()
        Homepage()._like_unlike_post()
        Homepage()._save_unsave_post()
        Homepage()._add_comment()
        Homepage()._add_edit_skill()
        
if __name__ == '__main__':
    t=Test()
    t.test_sample()