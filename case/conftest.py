from otc_api import otc
import os
import  pytest
import  sys
import  json
sys.path.append("..")
from action import otc,otc_admin,merchant
# from common.db import *
from common.read_yaml import ReadYaml
data = ReadYaml("data.yml").get_yaml_data()#读取数据

# -----------------------------进行总后台登录--------------------------------------------
@pytest.fixture(scope="session")
def admin_action(admin_info):
    return otc_admin.OtcAdmin(admin_info)

# -----------------------------第一个人进行app登录--------------------------------------------
@pytest.fixture(scope="session")
def first_ad_action(first_ad_info):
    return  merchant.Merchant(first_ad_info)

# -----------------------------第二个人进行app登录--------------------------------------------
@pytest.fixture(scope="session")
def second_ad_action(second_ad_info):
    return  merchant.Merchant(second_ad_info)

# -----------------------------第三个人进行app登录(hbq)--------------------------------------------
@pytest.fixture(scope="session")
def three_ad_action(three_ad_info):
    return otc.Otc(three_ad_info)

# -----------------------------------第一，第二,第三个人登录的session---------------------------
@pytest.fixture(scope="session")
def first_ad_session(first_ad_action):
    return first_ad_action.session
@pytest.fixture(scope="session")
def second_ad_session(second_ad_action):
    return second_ad_action.session
@pytest.fixture(scope="session")
def three_ad_session(three_ad_action):
    return three_ad_action.session


# -----------------------------获取账号otc_user数据-------------------------------------
@pytest.fixture(scope="session")
def first_ad_info():
    return  data['otc_user']

# -----------------------------获取账号otc_user_second数据------------------------------
@pytest.fixture(scope="session")
def second_ad_info():
    return  data['otc_user_second']

# -----------------------------获取账号otc_user_three数据------------------------------

@pytest.fixture(scope="session")
def three_ad_info():
    return  data['otc_user_three']

# -----------------------------获取账号otc_admin数据-------------------------------------
@pytest.fixture(scope="session")
def admin_info():
    return data['otc_admin']



# -----------------------------获取账号企业平台merchant数据------------------------------
@pytest.fixture(scope="session")
def merchant_info():
    return data['merchant']

# -----------------------------进行企业平台登录--------------------------------------------
@pytest.fixture(scope="session")
def merchant_action(merchant_info):
    return merchant.Merchant(merchant_info)
