from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from zipfile import ZipFile
import os

options = Options() 

options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\descargas",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


driver = webdriver.Chrome(options=options, executable_path=r"C:\chromeDriver\chromedriver.exe")

driver.get("http://eportal.mapama.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1")

driver.maximize_window()

## Selecciona la comunidad
comunidad_id = str(1)
select_com = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$DropDownListCCAA'))
select_com.select_by_value(comunidad_id)
time.sleep(2)

## Selecciona la provincia
provincia_id = str(4)
select_prov = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$DropDownListProvincia'))
select_prov.select_by_value(provincia_id)
time.sleep(2)

## Selecciona la estación (Seleccionamos un par)
estacion_id = str(2)
select_est = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$DropDownListEstacion'))
select_est.select_by_value(estacion_id)
time.sleep(2)
## Click en botón de añadir
#driver.find_element_by_id("ContentPlaceHolder1_ButtonAgregar").click();
#time.sleep(2)
#estacion_id = str(8)
#select_est = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$DropDownListEstacion'))
#select_est.select_by_value(estacion_id)
#time.sleep(2)
driver.find_element_by_id("ContentPlaceHolder1_ButtonAgregar").click();
time.sleep(2)

## Seleccionamos fechas
driver.find_element_by_id("txtFechaIni").clear()
time.sleep(4)
driver.find_element_by_id("txtFechaIni").send_keys('03/10/2019')
time.sleep(2)
driver.find_element_by_id("txtFechaFin").clear()
time.sleep(4)
driver.find_element_by_id("txtFechaFin").send_keys('10/10/2019')
time.sleep(2)
driver.find_element_by_id("ContentPlaceHolder1_btnConsultar").click()
time.sleep(5)

## Cambio de pestaña y descargo el archivo
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("ContentPlaceHolder1_ExportarCSV").click(); 
driver.close()

time.sleep(5)
## Extraigo el zip
zf = ZipFile('C:/descargas/InformeDatos.zip', 'r')
zf.extractall('C:/descargas')
zf.close()

os.remove("C:/descargas/InformeDatos.zip")