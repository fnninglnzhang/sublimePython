# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

from pppig_page import Page
from selenium.webdriver.common.by import By
import wait


# 风险评估
class To_User_Snswer_page(Page):
    #我的账户
    url = '/accountInfo'

    #title
    pppigcheck_title = ('胖胖猪-我的账户-账户概要')

    #重新评估
    pppigalertQuestions_button = (By.CSS_SELECTOR, 'body > div.ytop_account_bannre > div.ytop_account_center > div.ytop_account_main > div.ytop_account_main_bottom > span.ytop_acc_mb_tit1.ytop_acc_mb_red > a')
    # pppigalertQuestions_button_text = (By.linkText,'javascript:void(0)').getText()
    # pppigalertQuestions_button = (By.CSS_SELECTOR, 'span.ytop_acc_mb_tit1: nth - child(4) > a:nth - child(2)')
    # pppigalertQuestions_button = (By.XPATH, 'javascript:void(0)')

    #点击提交
    pppigSub_button = (By.CSS_SELECTOR, '#sub')

    #点击确定
    pppigOk = (By.CSS_SELECTOR, '#Ques_res > div > button')

    # 年龄
    dictAgeOne = {"18-25": "(By.CSS_SELECTOR, '#check_21')",
                  "26-30": "(By.CSS_SELECTOR, '#check_22')",
                  "31-40": "(By.CSS_SELECTOR, '#check_23')",
                  "41-50": "(By.CSS_SELECTOR, '#check_24')",
                  "50-": "(By.CSS_SELECTOR, '#check_25')"}

    dictAgeOne_1 = {"18-25": "'#check_21'",
                  "26-30": "'#check_22'",
                  "31-40": "'#check_23'",
                  "41-50": "'#check_24'",
                  "50-": "'#check_25'"}

    # 18岁-25岁
    pppigCheck_21_Radio = (By.CSS_SELECTOR, '#check_21')
    # 26岁-30岁
    pppigCheck_22_Radio = (By.CSS_SELECTOR, '#check_22')
    # 31岁-40岁
    pppigCheck_23_Radio = (By.CSS_SELECTOR, '#check_23')
    # 41岁-50岁
    pppigCheck_24_Radio = (By.CSS_SELECTOR, '#check_24')
    # 50岁以上
    pppigCheck_25_Radio = (By.CSS_SELECTOR, '#check_25')
    #Auto
    dictAgeOneResult = dictAgeOne_1['18-25']
    pppigCheck_auto_Radio = (By.CSS_SELECTOR, dictAgeOneResult)



    # 家庭年收入
    dictIncomeOne = {"-5": "(By.CSS_SELECTOR, '#check_41')",
                     "5-10": "(By.CSS_SELECTOR, '#check_42')",
                     "10-20": "(By.CSS_SELECTOR, '#check_43')",
                     "20-30": "(By.CSS_SELECTOR, '#check_44')",
                     "30-": "(By.CSS_SELECTOR, '#check_45')"}
    # 5万以下
    pppigCheck_41_Radio = (By.CSS_SELECTOR, '#check_41')
    # 5万-10万
    pppigCheck_42_Radio = (By.CSS_SELECTOR, '#check_42')
    # 10万-20万
    pppigCheck_43_Radio = (By.CSS_SELECTOR, '#check_43')
    # 20万-30万
    pppigCheck_44_Radio = (By.CSS_SELECTOR, '#check_44')
    # 30万以上
    pppigCheck_45_Radio = (By.CSS_SELECTOR, '#check_45')

    # 关注
    dictAttentionOne = {"anquan": "(By.CSS_SELECTOR, '#check_81')",
                        "shouyi": "(By.CSS_SELECTOR, '#check_82')",
                        "baozheng": "(By.CSS_SELECTOR, '#check_83')",
                        "linghuo": "(By.CSS_SELECTOR, '#check_84')"}
    # 资金安全
    pppigCheck_81_checkbox = (By.CSS_SELECTOR, '#check_81')
    # 资金收益
    pppigCheck_82_checkbox = (By.CSS_SELECTOR, '#check_82')
    # 品牌保证
    pppigCheck_83_checkbox = (By.CSS_SELECTOR, '#check_83')
    # 资金灵活
    pppigCheck_84_checkbox = (By.CSS_SELECTOR, '#check_84')

    # 年利率
    dictRateOne = {"6": "(By.CSS_SELECTOR, '#check_e1')",
                   "8": "(By.CSS_SELECTOR, '#check_e2')",
                   "10": "(By.CSS_SELECTOR, '#check_e3')",
                   "12": "(By.CSS_SELECTOR, '#check_e4')",
                   "12-": "(By.CSS_SELECTOR, '#check_e5')"}
    # 6%
    pppigCheck_e1_checkbox = (By.CSS_SELECTOR, '#check_e1')
    # 8%
    pppigCheck_e2_checkbox = (By.CSS_SELECTOR, '#check_e2')
    # 10%
    pppigCheck_e3_checkbox = (By.CSS_SELECTOR, '#check_e3')
    # 12%
    pppigCheck_e4_checkbox = (By.CSS_SELECTOR, '#check_e4')
    # 12%以上
    pppigCheck_e5_checkbox = (By.CSS_SELECTOR, '#check_e5')

    # 期限
    dictLimtOne = {"-1": "(By.CSS_SELECTOR, '#check_f1')",
                   "1-3": "(By.CSS_SELECTOR, '#check_f2')",
                   "3-6": "(By.CSS_SELECTOR, '#check_f3')",
                   "6-12": "(By.CSS_SELECTOR, '#check_f4')",
                   "12-": "(By.CSS_SELECTOR, '#check_f6')"}
    # 一个月内
    pppigCheck_f1_checkbox = (By.CSS_SELECTOR, '#check_f1')
    # 1月-3月
    pppigCheck_f2_checkbox = (By.CSS_SELECTOR, '#check_f2')
    # 3月-6月
    pppigCheck_f3_checkbox = (By.CSS_SELECTOR, '#check_f3')
    # 6月-12月
    pppigCheck_f4_checkbox = (By.CSS_SELECTOR, '#check_f4')
    # 12月以上
    pppigCheck_f5_checkbox = (By.CSS_SELECTOR, '#check_f5')

    #开始测评
    def alertQuestions_Button(self):
        wait.wait_presence_of_element_located(*self.pppigalertQuestions_button)
        self.find_element(*self.pppigalertQuestions_button).click()
    #选择年龄
    def dictAgeOne_Select(self,status):
        if status == 0:
            self.find_element(*self.pppigCheck_21_Radio).click()
        elif status == 1:
            self.find_element(*self.pppigCheck_22_Radio).click()
        elif status == 2:
            self.find_element(*self.pppigCheck_23_Radio).click()
        elif status == 3:
            self.find_element(*self.pppigCheck_24_Radio).click()
        elif status == 4:
            self.find_element(*self.pppigCheck_25_Radio).click()
        else:
            print("年龄传值错误")


    #选择收入
    def dictIncomeOne_Select(self,status):
        if status == 0:
            self.find_element(*self.pppigCheck_41_Radio).click()
        elif status == 1:
            self.find_element(*self.pppigCheck_42_Radio).click()
        elif status == 2:
            self.find_element(*self.pppigCheck_43_Radio).click()
        elif status == 3:
            self.find_element(*self.pppigCheck_44_Radio).click()
        elif status == 4:
            self.find_element(*self.pppigCheck_45_Radio).click()
        else:
            print("收入传值错误")

    #关注(限选三项)
    def dictAttentionOne_Select_Group(self,status):
        if status == 0:
            self.find_element(*self.pppigCheck_81_checkbox).click()
        elif status == 1:
            self.find_element(*self.pppigCheck_82_checkbox).click()
        elif status == 2:
            self.find_element(*self.pppigCheck_83_checkbox).click()
        elif status == 3:
            self.find_element(*self.pppigCheck_84_checkbox).click()
        else:
            print("关注传值错误")

    def dictAttentionOne_Select(self,status1,status2,status3):
        list1 = [status1,status2,status3]
        if len(list1) != len(set(list1)):
            print("数据重复，请回去检查数据哦")
        else:
            print("没有重复数据，可以执行啦")
            self.dictAttentionOne_Select_Group(status1)
            self.dictAttentionOne_Select_Group(status2)
            self.dictAttentionOne_Select_Group(status3)

    #年利率
    def dictRateOne_Select(self,status):
        if status == 0:
            self.find_element(*self.pppigCheck_e1_checkbox).click()
        elif status == 1:
            self.find_element(*self.pppigCheck_e2_checkbox).click()
        elif status == 2:
            self.find_element(*self.pppigCheck_e3_checkbox).click()
        elif status == 3:
            self.find_element(*self.pppigCheck_e4_checkbox).click()
        elif status == 4:
            self.find_element(*self.pppigCheck_e5_checkbox).click()
        else:
            print("年利率传值错误")

    #期限
    def dictLimitOne_Select(self,status):
        if status == 0:
            self.find_element(*self.pppigCheck_f1_checkbox).click()
        elif status == 1:
            self.find_element(*self.pppigCheck_f2_checkbox).click()
        elif status == 2:
            self.find_element(*self.pppigCheck_f3_checkbox).click()
        elif status == 3:
            self.find_element(*self.pppigCheck_f4_checkbox).click()
        elif status == 4:
            self.find_element(*self.pppigCheck_f2_checkbox).click()
        else:
            print("期限传值错误")

    #点击提交
    def pppigSub_button_button(self):
        self.find_element(*self.pppigSub_button).click()
    #结束测试，关闭弹层
    def pppigOk_button(self):
        self.find_element(*self.pppigOk).click()

    #进取型配置
    def pppigToUserAnswer_Action1(self,ageSelect,incomeSelect,attentionSelect1,attentionSelect2,attentionSelect3,rateSelect,limitSelect):
        self.alertQuestions_Button()
        sleep(2)
        self.dictAgeOne_Select(ageSelect)
        self.dictIncomeOne_Select(incomeSelect)
        self.dictAttentionOne_Select(attentionSelect1,attentionSelect2,attentionSelect3)
        self.dictRateOne_Select(rateSelect)
        self.dictLimitOne_Select(limitSelect)
        self.pppigSub_button_button()
        sleep(2)
        self.pppigOk_button()
