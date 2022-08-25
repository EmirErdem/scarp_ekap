from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from bs4 import BeautifulSoup
import pandas as pd
import math

k=1
while k<=3:


  if k==1:

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': 'download_directory'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver_path = "C:\webdrivers\chromedriver.exe"
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    browser.get("https://ekap.kik.gov.tr/EKAP/Vatandas/KurulKararSorgu.aspx?KararTip=1")
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]

    year=2
    while year <= 2:

      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ddlYil']/option["+str(year)+"]").click()
      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_btnAra']").click()
      time.sleep(1)

      source = browser.page_source
      soup = BeautifulSoup(source, "html.parser")
      sayfa_sayisi = math.ceil(
        int(soup.find("div", attrs={"class": "gridToplamSayi"}).text.replace("Toplam Kayıt Sayısı:", "")) / 10)



      for i in range(sayfa_sayisi):



        karar_no = soup.find_all("span", attrs={"id": "lblKno"})
        for i in karar_no:
           k_n=i.text
           list1.append(k_n)

        tarih=soup.find_all("span",attrs={"id":"lblKtar"})
        for i in tarih:
           k_t=i.text
           list2.append(k_t)

        idare=soup.find_all("span",attrs={"id":"lblIdare"})
        for i in idare:
           id=i.text
           list3.append(id)

        basvuru_sahibi=soup.find_all("span",attrs={"id":"lblSikayetci"})
        for i in basvuru_sahibi:
          b_s=i.text
          list4.append(b_s)

        ihale=soup.find_all("span",attrs={"id":"lblIhale"})
        for i in ihale:
          i_h=i.text
          list5.append(i_h)

        a = 0
        while a <= 9:
          list_2 = []
          data = browser.find_elements_by_class_name("btn-Kucuk")
          for i in data:
            list_2.append(i)
          browser.execute_script("arguments[0].click();", list_2[a])
          iframe = browser.find_element_by_xpath("//*[@id='iframe_detayPopUp']")
          browser.switch_to.frame(iframe)
          browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_downloadKarar']").click()
          browser.switch_to.default_content()
          browser.find_element_by_xpath("//*[@id='btnKapatPencere_0']").click()
          a = a + 1

        list = []
        data = browser.find_element_by_class_name("gridPageButtons")
        dataList = data.find_elements_by_tag_name('a')
        for item in dataList:
          list.append(item)
        browser.execute_script("arguments[0].click();", list[-1])

      year=year+1
      df = pd.DataFrame()
      df["karar_no"] = list1
      df["karar_tarihi"] = list2
      df["idare"] = list3
      df["basvuru_sahibi"] = list4
      df["ihale"] = list5
      df.to_csv("data\ekap_uk.csv")
      k=k+1
      browser.close()
# -----------------------------------------------------------------------2-------------------------------------------------------------------------#
 
  elif k==2:

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': 'download_directory'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver_path = "C:\webdrivers\chromedriver.exe"
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    browser.get("https://ekap.kik.gov.tr/EKAP/Vatandas/KurulKararSorgu.aspx?KararTip=2")
    list2_1 = []
    list2_2 = []
    list2_3 = []

    year = 2
    while year <= 2:


      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ddlYil']/option[" + str(year) + "]").click()
      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_btnAra']").click()
      time.sleep(1)
      source = browser.page_source
      soup = BeautifulSoup(source, "html.parser")
      sayfa_sayisi = math.ceil(
        int(soup.find("div", attrs={"class": "gridToplamSayi"}).text.replace("Toplam Kayıt Sayısı:", "")) / 10)


      for i in range(sayfa_sayisi):

        source = browser.page_source
        soup = BeautifulSoup(source, "html.parser")

        karar_no = soup.find_all("span", attrs={"id": "lblKno"})
        for i in karar_no:
          k_n = i.text
          list2_1.append(k_n)

        tarih = soup.find_all("span", attrs={"id": "lblKtar"})
        for i in tarih:
          k_t = i.text
          list2_2.append(k_t)

        gundem_konusu = soup.find_all("span", attrs={"id": "lblBaskonu"})
        for i in gundem_konusu:
          g_k = i.text
          list2_3.append(g_k)

        list = []
        data = browser.find_element_by_class_name("gridPageButtons")
        dataList = data.find_elements_by_tag_name('a')
        for item in dataList:
          list.append(item)
        list[-1].click()

      year = year + 1
      df2 = pd.DataFrame()
      df2["karar_no"] = list2_1
      df2["karar_tarihi"] = list2_2
      df2["gündem_konusu"] = list2_3
      df2.to_csv("data\ekap_dk.csv")
      k = k + 1
      browser.close()

# -----------------------------------------------------------------------3-------------------------------------------------------------------------#

  elif k == 3:

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': 'download_directory'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver_path = "C:\webdrivers\chromedriver.exe"
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    browser.get("https://ekap.kik.gov.tr/EKAP/Vatandas/KurulKararSorgu.aspx?KararTip=3")

    list3_1 = []
    list3_2 = []
    list3_3 = []
    list3_4 = []
    list3_5 = []
    year = 2
    while year <= 2:


      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ddlYil']/option[" + str(year) + "]").click()
      browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_btnAra']").click()
      time.sleep(1)
      source = browser.page_source
      soup = BeautifulSoup(source, "html.parser")
      sayfa_sayisi = math.ceil(
        int(soup.find("div", attrs={"class": "gridToplamSayi"}).text.replace("Toplam Kayıt Sayısı:", "")) / 10)


      for i in range(sayfa_sayisi):


        karar_no = soup.find_all("span", attrs={"id": "lblKno"})
        for i in karar_no:
          k_n = i.text
          list3_1.append(k_n)

        tarih = soup.find_all("span", attrs={"id": "lblKtar"})
        for i in tarih:
          k_t = i.text
          list3_2.append(k_t)

        basvuru_sahibi = soup.find_all("span", attrs={"id": "lblSikayetci"})
        for i in basvuru_sahibi:
          b_s = i.text
          list3_3.append(b_s)

        ihale = soup.find_all("span", attrs={"id": "lblIhale"})
        for i in ihale:
          ih = i.text
          list3_4.append(ih)

        gundem_konusu = soup.find_all("span", attrs={"id": "lblBaskonu"})
        for i in gundem_konusu:
          g_k = i.text
          list3_5.append(g_k)

        a = 0
        while a <= 9:
          list_2 = []
          data = browser.find_elements_by_class_name("btn-Kucuk")
          for i in data:
            list_2.append(i)
          browser.execute_script("arguments[0].click();", list_2[a])
          iframe = browser.find_element_by_xpath("//*[@id='iframe_detayPopUp']")
          browser.switch_to.frame(iframe)
          browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_downloadKarar']").click()
          browser.switch_to.default_content()
          browser.find_element_by_xpath("//*[@id='btnKapatPencere_0']").click()
          a = a + 1

        list = []
        data = browser.find_element_by_class_name("gridPageButtons")
        dataList = data.find_elements_by_tag_name('a')
        for item in dataList:
          list.append(item)
        browser.execute_script("arguments[0].click();", list[-1])

      year = year + 1
      df3 = pd.DataFrame()
      df3["karar_no"] = list3_1
      df3["karar_tarihi"] = list3_2
      df3["basvuru_sahibi"] = list3_3
      df3['ihale'] = pd.Series(list3_4)
      df3['gündem_konusu'] = pd.Series(list3_5)
      df3.to_csv("data\ekap_mk.csv")
      browser.close()












