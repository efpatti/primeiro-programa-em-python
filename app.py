import os

# Lista para armazenar os restaurantes
restaurantes = []

def iniciar():
   o1 = "Cadastrar restaurante"
   o2 = "Listar restaurantes"
   o3 = "Ativar restaurante"
   o4 = "Encerrar App"

   def reiniciar():
      os.system("clear")
      print("Reiniciando app...")
      iniciar()

   def encerrar_app():
      os.system("clear")
      print("Encerrando app!")
      quit()

   def deseja_reiniciar():
      deseja_reiniciar = input("Deseja reiniciar?\n S - Sim N - Não\nOpção escolhida: ").upper()
      if deseja_reiniciar == "S":
         reiniciar()
      else:
         encerrar_app()

   def cadastrar_restaurante():
      nome_restaurante = input("Nome do restaurante: ")
      categoria_restaurante = input("Categoria: ")
      # Adiciona o restaurante à lista
      restaurantes.append({"Nome": nome_restaurante, "Categoria": categoria_restaurante})
      print("Restaurante cadastrado com sucesso")
      cadastrar_outro = input("Deseja cadastrar outro restaurante?\nS - Sim N - Não\nOpção escolhida: ").upper()
      if cadastrar_outro == "S":
         cadastrar_restaurante()
      elif cadastrar_outro == "N":
         iniciar()
      else:
         opcao_invalida()

   def listar_restaurantes():
      print("Restaurantes:")
      for i, restaurante in enumerate(restaurantes, 1):
         print(f"{i} - Nome: {restaurante['Nome']}")
         print(f"    Categoria: {restaurante['Categoria']}")
      deseja_reiniciar()

   def opcao_invalida():
      os.system("clear")
      print("Opção inválida!\n")
      deseja_reiniciar()

   def exibir_opcoes():
      print(" 1 -",o1,"\n","2 -",o2,"\n","3 -",o3,"\n","4 -",o4,"\n")

   def escolher_opcao():
      exibir_opcoes()
      opcao_escolhida = int(input("Opção escolhida: "))
      if opcao_escolhida == 1:
         cadastrar_restaurante()
      elif opcao_escolhida == 2:
         listar_restaurantes()
      elif opcao_escolhida == 3:
         print("Ativar restaurante")
      elif opcao_escolhida == 4:
         encerrar_app()
      else:
         opcao_invalida()

   escolher_opcao()

iniciar()
