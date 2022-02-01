from django.test import LiveServerTestCase
from selenium import webdriver  
from animais.models import Animal
import time

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.animal = Animal.objects.create(

            nome_animal ='Leão', 
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Não'

        )

    def tearDown(self):
        self.browser.quit()

    def test_pesquisa_animal(self):
        
        #Usuario encontra o site e decide acessar o menu Busca Animal  
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_tag_name('a')
        self.assertEqual('Busca Animal', brand_element.text)
        #ele vê um campo para pesuisar o animal 
        busca_animal_input = self.browser.find_element_by_css_selector('input#buscar_animal')
        self.assertEqual(busca_animal_input.get_attribute('placeholder'), 'Exemplo: Leão')
        busca_animal_input.send_keys('leão')
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(2)
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        time.sleep(2)
        self.assertGreater(len(caracteristicas), 3)


    #/html/body/form/button

    # def test_my_server(self):
    #     self.browser.get(self.live_server_url)
        



