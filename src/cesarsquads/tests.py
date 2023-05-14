from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class TesteSelenium(LiveServerTestCase):
    # Set the path to your Chrome driver executable
    driver_path = '/path/to/chromedriver'

    # Start the Chrome driver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # Open the web application
    driver.get('http://127.0.0.1:8000')  # Replace with the URL of your Django application

    # Test the login functionality
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    submit_button = driver.find_element(By.ID, 'login')

    username_input.send_keys('selenium')
    password_input.send_keys('sele123456')
    submit_button.click()
    sleep(2)

    # Test the profile page
    profile_link = driver.find_element(By.ID, 'perfil')
    profile_link.click()
    sleep(2)

    # Verify that the user's information is displayed correctly
    username = driver.find_element(By.ID, 'username')
    nome = driver.find_element(By.ID, 'nome')
    email = driver.find_element(By.ID, 'email')
    assert nome.text == 'Selenium Web Driver'
    assert username.text == 'selenium'
    assert email.text == 'selenium@gmail.com'

    # Enter the tribe page
    tribo_desejada = "Selenium1"
    botoes_acordeao = driver.find_elements(By.CLASS_NAME, "accordion-button")

    botao_tribo = None
    for botao in botoes_acordeao:
        if botao.text.strip() == tribo_desejada:
            botao_tribo = botao
            break

    assert botao_tribo is not None, f"Botão da tribo '{tribo_desejada}' não foi encontrado"

    acordeon = botao_tribo.find_element(By.XPATH, "../..")

    if not acordeon.get_attribute("class").endswith("show"):
        botao_tribo.click()
    sleep(2)
    driver.find_element(By.ID, "entrar-tribo").click()
    sleep(2)

    # Enter a squad
    squad_desejada = "sele2"
    squad_find = driver.find_element(By.ID, f"entrar-squad-{squad_desejada}").click()
    sleep(2)

    #Back to tribe page
    driver.find_element(By.ID, "voltar").click()
    driver.refresh()
    sleep(2)

    #Try to create a squad with a name that already exists
    criar_squad = driver.find_element(By.ID, "criar-squad")
    criar_squad.send_keys("sele3")
    sleep(2)
    driver.find_element(By.ID, "criar-squad-button").click()
    sleep(2)
    squad_existe = driver.find_element(By.ID, "squad-existe").text
    assert squad_existe == "Já existe uma squad com este nome nesta tribo."
    driver.refresh()
    
    #Create a Squad
    criar_squad = driver.find_element(By.ID, "criar-squad")
    criar_squad.send_keys("sele4")
    sleep(2)
    driver.find_element(By.ID, "criar-squad-button").click()
    sleep(2)

    #Change bio from a Squad
    nova_descricao = "Nova descrição da squad"
    driver.find_element(By.ID, "editar-bio-squad").click()
    sleep(2)
    descricao_input = driver.find_element(By.ID, "bio-text")
    descricao_input.clear()
    descricao_input.send_keys(nova_descricao)
    driver.find_element(By.ID, "salvar-bio-squad").click()
    sleep(2)
    descricao_atualizada = driver.find_element(By.ID, "bio-squad")
    assert descricao_atualizada != nova_descricao, "A descrição da squad foi atualizada corretamente"

    #Change avatar from a Squad
    change_avatar_button = driver.find_element(By.ID, "change-avatar")
    change_avatar_button.click()
    sleep(2)
    avatar_input = driver.find_element(By.ID, "avatar")
    avatar_input.send_keys("C:/Users/fcoan/OneDrive/Documentos/Meus Projetos/Cesar Squads/fdsproject/src/media/squad/Final.png")
    sleep(2)
    submit_avatar_button = driver.find_element(By.ID, "submit-avatar")
    submit_avatar_button.click()
    sleep(2)
    
    driver.find_element(By.ID, "perfil").click()
    sleep(2)
    
    # Search tribe
    tribo_desejada = "teste"
    search_input = driver.find_element(By.ID, "search-tribe")
    search_input.send_keys(tribo_desejada)
    sleep(2)
    driver.find_element(By.ID, "search-button").click()
    sleep(2)
    link_tribo = driver.find_element(By.ID, f"enter-tribe-{tribo_desejada}")
    link_tribo.click()
    sleep(2)
    
    driver.find_element(By.ID, "perfil").click()
    
    # Try to create a tribe with a name that already exists
    input_tribe_name = driver.find_element(By.ID, "name-tribe")
    input_tribe_name.send_keys("Selenium3")
    sleep(2)
    create_tribe_button = driver.find_element(By.ID, "criar-tribo").click()
    sleep(2)
    assert driver.find_element(By.ID, "tribo-existe").text == "Esta tribo ja existe! Tente outro nome, ou procure a tribo na barra de pesquisa."
    
    # Create a tribe
    input_tribe_name = driver.find_element(By.ID, "name-tribe")
    input_tribe_name.send_keys("Selenium2")
    sleep(2)
    create_tribe_button = driver.find_element(By.ID, "criar-tribo")
    create_tribe_button.click()
    sleep(2)
    
    #Change bio from a tribe
    nova_descricao = "Nova descrição da tribo"
    driver.find_element(By.ID, "editar-bio-tribo").click()
    sleep(2)
    descricao_input = driver.find_element(By.ID, "bio-text")
    descricao_input.clear()
    descricao_input.send_keys(nova_descricao)
    driver.find_element(By.ID, "salvar-bio-tribo").click()
    sleep(2)
    descricao_atualizada = driver.find_element(By.ID, "bio-tribo")
    assert descricao_atualizada != nova_descricao, "A descrição da tribo foi atualizada corretamente"
    
    #Change avatar from a Tribe
    change_avatar_button = driver.find_element(By.ID, "change-avatar")
    change_avatar_button.click()
    sleep(2)
    avatar_input = driver.find_element(By.ID, "avatar")
    avatar_input.send_keys("C:/Users/fcoan/OneDrive/Documentos/Meus Projetos/Cesar Squads/fdsproject/src/media/tribe/marca_cesar_school.webp")
    sleep(2)
    submit_avatar_button = driver.find_element(By.ID, "submit-avatar")
    submit_avatar_button.click()
    sleep(2)
    
    driver.find_element(By.ID, "perfil").click()
    sleep(2)
    
    driver.find_element(By.ID, "logout").click()
    
    # Close the browser
    driver.quit()