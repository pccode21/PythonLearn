#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time

class video_play_aiqiyi:
    def __init__(self, driver):
        self.driver = driver
        #查找必要的控件
        print 'aiqiyi begin to find element'
        self.video = self.driver.find_element_by_xpath('//video')
        self.video_start = self.driver.find_element_by_xpath('//*[@id="iqp-svg-pause"]')
        self.video_progress_bar = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/iqpdiv/iqpdiv[1]/iqpdiv[2]/iqpdiv/iqpdiv[2]/iqpdiv')
        self.video_progress_dot = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/iqpdiv/iqpdiv[1]/iqpdiv[2]/iqpdiv/iqpdiv[2]/iqpdiv/iqpdiv[3]')

        self.definition = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/iqpdiv/iqpdiv[1]/iqpdiv[2]/iqpdiv/iqpdiv[4]/iqpdiv[3]/iqpdiv[6]/iqp')
        self.definition_1080pClient = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_pca"]')
        self.definition_1080p = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_5"]')
        self.definition_720p = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_4"]')
        self.definition_GaoQing = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_2"]')
        self.definition_LiuChang = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_1"]')
        self.definition_JiSu = self.driver.find_element_by_xpath('//iqpspan[@data-player-hook="vip_definition_96"]')
        print 'has find all the elements'

    def play(self, definition_aiqiyi):
        self.set_definition(definition_aiqiyi)
        self.reset_progress()


    def set_definition(self, definition_aiqiyi):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.video).perform()#初次将鼠标移动到video上，会呼叫出control bar，在control bar上进行后续操作
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.definition).perform()#将鼠标移动至"清晰度"那里
        self.driver.save_screenshot('aiqiyi_set_definition.png')
        time.sleep(1)

        if definition_aiqiyi == '1080pClient':
            ActionChains(self.driver).click(self.definition_1080pClient).perform()
        elif definition_aiqiyi == '1080p':
            ActionChains(self.driver).click(self.definition_1080p).perform()
        elif definition_aiqiyi == '720p':
            ActionChains(self.driver).click(self.definition_720p).perform()
        elif definition_aiqiyi == 'GaoQing':
            ActionChains(self.driver).click(self.definition_GaoQing).perform()
        elif definition_aiqiyi == 'LiuChang':
            ActionChains(self.driver).click(self.definition_LiuChang).perform()
        elif definition_aiqiyi == 'JiSu':
            ActionChains(self.driver).click(self.definition_JiSu).perform()
        else :
            print 'param unvalid'
        time.sleep(1)

    def reset_progress(self):
        #晃一下，调出video的控制面板
        ActionChains(self.driver).move_to_element(self.video).perform()
        time.sleep(0.5)
        ActionChains(self.driver).move_by_offset(10, 10).perform()#在播放界面上移动一下
        time.sleep(0.5)

        ActionChains(self.driver).move_to_element(self.video_progress_bar).perform()#移动到progress_bar的中心位置
        time.sleep(0.5)

        width_bar = -((self.video_progress_bar.size['width']) / 2 - 1)#计算progress_bar长度的一半
        ActionChains(self.driver).move_by_offset(width_bar, 0).perform()#移动鼠标
        time.sleep(0.5)
        ActionChains(self.driver).click().perform()#在鼠标当前位置下触发点击事件

if __name__ == "__main__":
    driver = webdriver.Firefox(firefox_profile='./profile', executable_path='./geckodriver1.exe')#geckodriver的最新版本

    driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
    driver.get("https://www.iqiyi.com/v_19rr57hv5c.html")

    test = video_play_aiqiyi(driver)
    time.sleep(35)
    test.play("GaoQing")
    print 'video_play_aiqiyi test over'
