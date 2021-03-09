import os,sys
sys.path.append(os.getcwd())
from config.variable import *
from config.xpath import *
from config.common import Common
from config.variable import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

###method parameters
like_unlike_button_id = "ps_1451"
save_button_id = "savelink_1451"
unsave_button_id = "unsavelink_1451"
commentbox_id = "commentparentx_1451"
commentbox_input_data = "testing_"

add_edit_skill_type = 'add'
add_remove_skill = 'python'
go_to_profile_button_class = "//a[@class='btn btn-secondary btn-block']"
add_skill_button_xpath ="//p[text()='Add a Skill ']"
type_skill_full_input_xpath = "//input[@id='SkillT_myprofile']//..//div"
type_skill_input_xpath = "//input[@type='text']"
skill_save_profile_id = "skillSave_myprofile"

class Homepage():

    def __init__(self):
        self.driver = driver

    def _like_unlike_post(self,button_id=like_unlike_button_id):
        Common()._do_click('id', button_id)

    def _save_unsave_post(self, button_id =save_button_id):
        try:
            Common()._do_click('id', button_id)
        except:
            print("Post is already saved/unsaved")

    def _add_comment(self,input_text_id=commentbox_id,input=commentbox_input_data):
        Common()._do_sendkeys('id', input_text_id,input)
        Common()._do_sendkeys('id', input_text_id,Keys.ENTER)

    def _add_edit_skill(self,type='remove',input=add_remove_skill):
        Common()._do_click('xpath', go_to_profile_button_class)
        if type.lower() == 'add':
            Common()._do_click('xpath', add_skill_button_xpath)
            time.sleep(10)
            Common()._do_move_to_element_click('xpath', type_skill_full_input_xpath)
            Common()._do_sendkeys('xpath', f'({type_skill_input_xpath})[104]', input)
            Common()._do_click('id', skill_save_profile_id)
        else:
            remove = f"//div[@id='skillList_myprofile']//a[text()='{add_remove_skill}']//..//a[@class='fa fa-times']"
            Common()._do_move_to_element_click('xpath', remove)
            time.sleep(5)
            self.driver.switch_to.alert.accept()

if __name__ == '__main__':
    pass
