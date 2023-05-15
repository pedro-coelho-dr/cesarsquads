from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class TesteSelenium(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://127.0.0.1:8000/")
        sleep(2)
           

    
    def login(self):
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.ID, 'login')

        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        
    def test_profile(self):
        self.login()
        sleep(2)
        profile_link = self.driver.find_element(By.ID, 'perfil')
        profile_link.click()
        sleep(2)
        username = self.driver.find_element(By.ID, 'username')
        nome = self.driver.find_element(By.ID, 'nome')
        email = self.driver.find_element(By.ID, 'email')
        assert nome.text == 'Selenium Web Driver', "Nome esta correto!"
        assert username.text == 'selenium', "Username esta correto!"
        assert email.text == 'selenium@gmail.com', "Email esta correto!"
        self.driver.quit()

    def test_enter_tribe(self):
        self.login()
        tribo_desejada = "Selenium1"
        botoes_acordeao = self.driver.find_elements(By.CLASS_NAME, "accordion-button")

        botao_tribo = None
        for botao in botoes_acordeao:
            if botao.text.strip() == tribo_desejada:
                botao_tribo = botao
                break
            
        assert botao_tribo is None, f"Botão da tribo '{tribo_desejada}' não foi encontrado"

        acordeon = botao_tribo.find_element(By.XPATH, "../..")

        if not acordeon.get_attribute("class").endswith("show"):
            botao_tribo.click()
        sleep(2)
        self.driver.find_element(By.ID, "entrar-tribo").click()
        sleep(2)
        self.tearDownClass()
        self.driver.quit()

    def test_enter_squad(self):
        self.login()
        self.driver.get("http://127.0.0.1:8000/tribe/selenium1")
        sleep(2)
        squad_desejada = "sele2"
        self.driver.find_element(By.ID, f"entrar-squad-{squad_desejada}").click()
        sleep(2)
        self.driver.find_element(By.ID, "voltar").click()
        self.driver.refresh()
        sleep(2)
        self.tearDownClass()
        self.driver.quit()

    def test_create_squad(self):
        self.login()
        self.driver.get("http://127.0.0.1:8000/tribe/selenium1")
        criar_squad = self.driver.find_element(By.ID, "criar-squad")
        criar_squad.send_keys("sele3")
        sleep(2)
        self.driver.find_element(By.ID, "criar-squad-button").click()
        sleep(2)
        squad_existe = self.driver.find_element(By.ID, "squad-existe").text
        assert squad_existe == "Já existe uma squad com este nome nesta tribo."
        sleep(1)
        self.driver.refresh()
        criar_squad = self.driver.find_element(By.ID, "criar-squad")
        criar_squad.send_keys("sele4")
        sleep(2)
        self.driver.find_element(By.ID, "criar-squad-button").click()
        sleep(2)
        self.tearDownClass()
        self.driver.quit()

    def test_change_bio_squad(self):
        nova_descricao = "Nova descrição da squad"
        self.driver.find_element(By.ID, "editar-bio-squad").click()
        sleep(2)
        descricao_input = self.driver.find_element(By.ID, "bio-text")
        descricao_input.clear()
        descricao_input.send_keys(nova_descricao)
        self.driver.find_element(By.ID, "salvar-bio-squad").click()
        sleep(2)
        descricao_atualizada = self.driver.find_element(By.ID, "bio-squad")
        assert descricao_atualizada != nova_descricao, "A descrição da squad foi atualizada corretamente"
        self.driver.quit()

    def test_change_avatar_squad(self):
        change_avatar_button = self.driver.find_element(By.ID, "change-avatar")
        change_avatar_button.click()
        sleep(2)
        avatar_input = self.driver.find_element(By.ID, "avatar")
        avatar_input.send_keys("C:/Users/fcoan/OneDrive/Documentos/Meus Projetos/Cesar Squads/fdsproject/src/media/squad/Final.png")
        sleep(2)
        submit_avatar_button = self.driver.find_element(By.ID, "submit-avatar")
        submit_avatar_button.click()
        sleep(2)

        self.driver.find_element(By.ID, "perfil").click()
        sleep(2)
        self.driver.quit()

    def test_search_tribe(self):
        tribo_desejada = "Selenium Entre"

        search_input = self.driver.find_element(By.ID, "search-tribe")
        search_input.send_keys(tribo_desejada)
        sleep(2)
        self.driver.find_element(By.ID, "search-button").click()
        sleep(2)
        link_tribo = self.driver.find_element(By.ID, f"enter-tribe-{tribo_desejada}")
        link_tribo.click()
        sleep(2)

        self.driver.find_element(By.ID, "perfil").click()
        self.driver.quit()

    def test_create_tribe(self):
        input_tribe_name = self.driver.find_element(By.ID, "name-tribe")
        input_tribe_name.send_keys("Selenium2")
        sleep(2)
        create_tribe_button = self.driver.find_element(By.ID, "criar-tribo").click()
        sleep(2)
        tribo_existe = self.driver.find_element(By.ID, "tribo-existe").text
        sleep(2)
        input_tribe_name = self.driver.find_element(By.ID, "name-tribe")
        input_tribe_name.send_keys("Selenium3")
        sleep(2)
        create_tribe_button = self.driver.find_element(By.ID, "criar-tribo")
        create_tribe_button.click()
        sleep(2)
        self.driver.quit()

    def test_change_bio_tribe(self):
        nova_descricao = "Nova descrição da tribo"
        self.driver.find_element(By.ID, "editar-bio-tribo").click()
        sleep(2)
        descricao_input = self.driver.find_element(By.ID, "bio-text")
        descricao_input.clear()
        descricao_input.send_keys(nova_descricao)
        self.driver.find_element(By.ID, "salvar-bio-tribo").click()
        sleep(2)
        descricao_atualizada = self.driver.find_element(By.ID, "bio-tribo")
        assert descricao_atualizada != nova_descricao, "A descrição da tribo foi atualizada corretamente"
        self.driver.quit()

    def test_change_avatar_tribe(self):
        change_avatar_button = self.driver.find_element(By.ID, "change-avatar")
        change_avatar_button.click()
        sleep(2)
        avatar_input = self.driver.find_element(By.ID, "avatar")
        avatar_input.send_keys("C:/Users/fcoan/OneDrive/Documentos/Meus Projetos/Cesar Squads/fdsproject/src/media/tribe/marca_cesar_school.webp")
        sleep(2)
        submit_avatar_button = self.driver.find_element(By.ID, "submit-avatar")
        submit_avatar_button.click()
        sleep(2)
        
        

        self.driver.find_element(By.ID, "perfil").click()
        sleep(2)

        self.driver.find_element(By.ID, "logout").click()
        sleep(2)

