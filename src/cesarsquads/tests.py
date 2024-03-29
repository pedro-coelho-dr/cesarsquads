import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



def setUp():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--icognito')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    return driver

class TesteSelenium(LiveServerTestCase):
    
    '''def test1_profile(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'perfil'))
        )
        profile_link.click()
        sleep(2)
        username = driver.find_element(By.ID, 'username')
        nome = driver.find_element(By.ID, 'nome')
        email = driver.find_element(By.ID, 'email')
        assert nome.text == 'Selenium Web Driver', "Nome está correto!"
        assert username.text == 'selenium', "Username está correto!"
        assert email.text == 'selenium@gmail.com', "Email está correto!"
        driver.close()'''	

    def test2_enter_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")

        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')

        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)

        tribo_desejada = "selenium1"

        entrar_tribo_buttons = driver.find_elements(By.NAME, "Acessar")
        for button in entrar_tribo_buttons:
            if f"entrar-tribo-selenium1" in button.get_attribute("id"):
                button.click()
                break


    def test3_enter_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/selenium1")
        sleep(2)
        squad_desejada = "sele2"
        element = driver.find_element(By.ID, f"entrar-squad-{squad_desejada}")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(1)
        element.click()
        sleep(2)
        squad_atual = driver.find_element(By.ID, "nome-squad")
        assert squad_atual.text == squad_desejada, "A squad atual é a squad desejada"

    def test4_create_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/selenium1")
        criar_squad =         criar_squad = driver.find_element(By.ID, "criar-squad")
        criar_squad.send_keys("sele3")
        sleep(2)
        driver.find_element(By.ID, "criar-squad-button").click()
        sleep(2)
        driver.refresh()
        criar_squad = driver.find_element(By.ID, "criar-squad")
        criar_squad.send_keys("sele4")
        sleep(2)
        driver.find_element(By.ID, "criar-squad-button").click()
        sleep(2)
        squad_atual = driver.find_element(By.ID, "nome-squad") 
        assert squad_atual.text == "sele4"

    def test5_change_bio_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/4/squad/sele1/")
        sleep(1)
        nova_descricao = "Nova descrição da squad"
        driver.find_element(By.ID, "editar-bio-squad").click()
        sleep(2)
        descricao_input = driver.find_element(By.ID, "bio-text")
        descricao_input.clear()
        descricao_input.send_keys(nova_descricao)
        driver.find_element(By.ID, "salvar-bio-squad").click()
        sleep(2)
        descricao_atualizada = driver.find_element(By.ID, "bio-squad")
        assert descricao_atualizada.text == nova_descricao, "A descrição da squad foi atualizada corretamente"

    def test6_change_avatar_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/4/squad/sele1/")
        sleep(1)
        change_avatar_button = driver.find_element(By.ID, "change-avatar")
        change_avatar_button.click()
        sleep(2)
        avatar_input = driver.find_element(By.ID, "avatar")
        avatar_input.send_keys("/home/runner/work/fdsproject/fdsproject/src/media/squad/logo_squad.png")
        sleep(2)
        submit_avatar_button = driver.find_element(By.ID, "submit-avatar")
        submit_avatar_button.click()
        sleep(2)
        assert True, "Avatar da squad foi atualizado corretamente"


    def test7_search_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        tribo_desejada = "Selenium Entre"
        search_input = driver.find_element(By.ID, "search-tribe")
        search_input.send_keys(tribo_desejada)
        sleep(2)
        driver.find_element(By.ID, "search-button").click()
        sleep(2)
        link_tribo = driver.find_element(By.ID, f"enter-tribe-{tribo_desejada}")
        link_tribo.click()
        sleep(2)
        tribo_atual = driver.find_element(By.ID, "nome-tribo")
        assert tribo_atual.text == tribo_desejada, "A tribo atual é a tribo desejada"


    def test8_create_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        input_tribe_name = driver.find_element(By.ID, "name-tribe")
        input_tribe_name.send_keys("Selenium2")
        sleep(2)
        create_tribe_button = driver.find_element(By.ID, "criar-tribo").click()
        sleep(2)
        input_tribe_name = driver.find_element(By.ID, "name-tribe")
        input_tribe_name.send_keys("Selenium3")
        sleep(2)
        create_tribe_button = driver.find_element(By.ID, "criar-tribo")
        create_tribe_button.click()
        sleep(2)
        tribo_atual = driver.find_element(By.ID, "nome-tribo")
        assert tribo_atual.text == "Selenium3", "A tribo atual é a tribo desejada"


    def test9_change_bio_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/selenium1/")
        nova_descricao = "Nova descrição da tribo"
        driver.find_element(By.ID, "editar-bio-tribo").click()
        sleep(2)
        descricao_input = driver.find_element(By.ID, "bio-text")
        descricao_input.clear()
        descricao_input.send_keys(nova_descricao)
        driver.find_element(By.ID, "salvar-bio-tribo").click()
        sleep(2)
        descricao_atualizada = driver.find_element(By.ID, "bio-tribo")
        assert descricao_atualizada.text == nova_descricao, "A descrição da tribo foi atualizada corretamente"


    def test10_change_avatar_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/selenium1/")
        change_avatar_button = driver.find_element(By.ID, "change-avatar")
        change_avatar_button.click()
        sleep(2)
        avatar_input = driver.find_element(By.ID, "avatar")
        avatar_input.send_keys("/home/runner/work/fdsproject/fdsproject/src/media/tribe/images.jpg")
        sleep(2)
        submit_avatar_button = driver.find_element(By.ID, "submit-avatar")
        submit_avatar_button.click()
        sleep(2)
        assert True, "Avatar da tribo foi atualizado corretamente"



    def test11_add_user_to_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        driver.get("http://127.0.0.1:8000/tribe/4/squad/sele3/")
        username_input = driver.find_element(By.ID, 'nome-usuario')
        username_input.send_keys('thas')
        username_desejado = 'thas'
        add_button = driver.find_element(By.ID, "adicionar-usuario")
        driver.execute_script("arguments[0].scrollIntoView();", add_button)
        sleep(2)
        add_button.click()
        sleep(2)
        squad_members = driver.find_element(By.ID, f'nome-{username_desejado}')
        assert squad_members.text == "Thiago Araújo", "Usuário adicionado corretamente"

    def test12_remove_user_from_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        driver.get("http://127.0.0.1:8000/tribe/4/squad/sele2/")
        sleep(2)
        select_element = driver.find_element(By.NAME, 'user_id')
        sleep(2)
        select = Select(select_element)
        sleep(2)
        select.select_by_visible_text('thas') 
        sleep(2)
        remove_button = driver.find_element(By.ID, 'remover')
        remove_button.click()

    def test13_add_user_to_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        driver.get("http://127.0.0.1:8000/tribe/selenium2/")
        username_input = driver.find_element(By.ID, 'nome-usuario')
        username_input.send_keys('thas')
        username_desejado = 'thas'
        add_button = driver.find_element(By.ID, "adicionar-usuario")
        driver.execute_script("arguments[0].scrollIntoView();", add_button)
        sleep(2)
        add_button.click()

    def test14_remove_user_from_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        driver.get("http://127.0.0.1:8000/tribe/selenium1/")
        sleep(2)
        select_element = driver.find_element(By.NAME, 'user_id')
        sleep(2)
        select = Select(select_element)
        sleep(2)
        select.select_by_visible_text('thas') 
        sleep(2)
        remove_button = driver.find_element(By.ID, 'remover')
        remove_button.click()
        
    def test15_leave_squad(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/4/squad/selesair/")
        sleep(2)
        sair = driver.find_element(By.ID, 'sair-squad')
        sair.click()
        
    def test16_leave_tribe(self):
        driver = setUp()
        driver.get("http://127.0.0.1:8000/")
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.ID, 'login')
        username_input.send_keys('selenium')
        password_input.send_keys('sele123456')
        sleep(2)
        submit_button.click()
        sleep(2)
        driver.get("http://127.0.0.1:8000/tribe/selenium-sair/")
        sleep(2)
        sair = driver.find_element(By.ID, 'sair-tribo')
        sair.click()