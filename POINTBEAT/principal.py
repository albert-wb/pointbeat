import tkinter as tk
import customtkinter as ctk
import logging
import mysql.connector
import os
import sys
from tkinter import messagebox
from PIL import Image
from datetime import datetime as dt
from validate_docbr import CPF

conexao = mysql.connector.connect(
    host = 'viaduct.proxy.rlwy.net',
    port = 49237,
    user = 'root',
    password = 'BcH2eD1H31aHgd1521DC2bA-1H2H2c22',
    database ='railway'
)

cursor = conexao.cursor()

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.import_images()
        self.tela_login()
        self.frame_tela_login()
        self.widgets_login()
        self.janela.mainloop()
    
    def import_images(self):
        self.logo_1 = ctk.CTkImage(Image.open("images\\logo.png"), size=(333,83))
        self.fundotipoRegistro = ctk.CTkImage(Image.open("images\\tipo de registro.png"), size=(296,110))
        self.fundocaixaHora = ctk.CTkImage(Image.open("images\\caixa_horario.png"), size=(296,62))
        self.logo_header = ctk.CTkImage(Image.open("images\\logo_header.png"), size=(217,60))
        self.logo_header_admin = ctk.CTkImage(Image.open("images\\logo_laranja.png"), size=(217,60))

    def tela_login(self):
        self.janela.geometry("1280x800")
        self.janela.title("POINTBEAT")
        self.janela.resizable(0, 0)
        self.janela.configure(fg_color="Black")
    
    def frame_tela_login(self):
        self.frame = ctk.CTkFrame(self.janela, fg_color="transparent")
        self.frame.pack()

    def widgets_login(self):
        
        self.label = ctk.CTkLabel(self.frame, image=self.logo_1, text='')
        self.label.grid(row=0, column=1, pady=100)

        self.entryLogin = ctk.CTkEntry(self.frame, border_color="#00FF00", placeholder_text="Login")
        self.entryLogin.grid(row=1, column=1, pady=3)

        self.entrySenha = ctk.CTkEntry(self.frame, border_color="#00FF00", show="*", placeholder_text="Senha")
        self.entrySenha.grid(row=2, column=1, pady=3)

        self.buttonLogin = ctk.CTkButton(self.frame, text="Entrar", fg_color="#00FF00", text_color="black", command=self.logar_button)
        self.buttonLogin.grid(row=3, column=1, pady=3)

        self.buttonRegistro = ctk.CTkButton(self.frame, text="Registrar", fg_color="#00FF00", text_color="black", command=self.register_button)# command=lambda: cadastrar(self))
        self.buttonRegistro.grid(row=4, column=1, pady=3)

        self.buttonSair = ctk.CTkButton(self.frame, text="Sair", fg_color="#00FF00", text_color="black", command= self.sair)
        self.buttonSair.grid(row=5, column=1, pady=3)

    def logar_button(self):
        email = self.entryLogin.get()
        senha = self.entrySenha.get()
        query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        valores = (email, senha)
        cursor.execute(query, valores)
        resultado = cursor.fetchone()
        if resultado:
            if resultado[7] == 1:
                print("Login bem-sucedido ADM. Você o CONTROLE.")
                self.frame.destroy()
                self.tela_admin()
            else:
                print("Login bem-sucedido. Você pode acessar o programa.")
                self.frame.destroy()
                self.tela_inicial_usuario()
        else:
            print("Login mal-sucedido. Tente novamente")
            messagebox.showerror("Aviso", "Usuário ou senha incorretos. Tente novamente.")
    
    def cadastrar(self):
        Verificador = CPF()
        consulta = "SELECT * FROM empresa WHERE cod = %s"
        parametros = (self.EntryCodEmpresa.get(),)
        cursor.execute(consulta, parametros)
        resultados = cursor.fetchall()

        if Verificador.validate(self.EntryCPF.get()) == True and resultados:
            print("CPF e COD Empresa válidos")
        # Gravando no banco de dados
            if self.EntrySenha.get() == self.EntryConfirmarSenha.get():
                inserir = "INSERT INTO usuarios (nome, cpf, senha, email, celular, adm) VALUES (%s, %s, %s, %s, %s, %s)"
                parametros = (self.EntryUsuario.get(), self.EntryCPF.get(), self.EntrySenha.get(), self.EntryEmail.get(), self.EntryCelular.get(), 0)
                cursor.execute(inserir, parametros)
                conexao.commit()
                print("Dados gravados com sucesso!")
                messagebox.showinfo("Aviso", "Cadastro realizado com sucesso!")
            else:
                print("As senhas não batem")
                messagebox.showerror("Aviso", "Senhas não batem. Tente novamente.")
        
        else:
            print("CPF ou COD Empresa inválidos")
            # Mostrando uma mensagem de erro
            messagebox.showerror("Erro", "CPF ou COD Empresa inválidos. Por favor, verifique o número do CPF e o código da empresa.")
    
    def register_button(self):
        self.frame.destroy()
        self.tela_cadastro()
    
    def sair(self):
      self.janela.destroy() 

    def button_callbck(self):
        print("button clicked")

    def tela_cadastro(self):

        #------------------container------------------------------------
        self.frameCad = ctk.CTkFrame(self.janela, fg_color="transparent")
        self.frameCad.pack()

        self.frameLogoCad = ctk.CTkFrame(self.frameCad, fg_color="transparent")
        self.frameLogoCad.grid(row=0, columnspan=4, pady=100)

        self.labelLogoCad = ctk.CTkLabel(self.frameLogoCad, image=self.logo_1, text='')
        self.labelLogoCad.pack()
        
        #------------------Linha0---------------------------------------
    
        self.LabelCadastre = ctk.CTkLabel(self.frameCad, text='CRIE SEU CADASTRO', font=("",14))
        self.LabelCadastre.grid(row=1, column=0, columnspan=4)

        #------------------linha1--------------------------------

        self.EntryUsuario = ctk.CTkEntry(self.frameCad, border_color="#00FF00", placeholder_text="Nome")
        self.EntryUsuario.grid(row=2, column=0, columnspan=2, padx=3, pady=3, sticky="ew")

        self.EntryCPF = ctk.CTkEntry(self.frameCad, border_color="#00FF00", placeholder_text="CPF")
        self.EntryCPF.grid(row=2, column=2, columnspan=2, padx=3, pady=3, sticky="ew")

        # #----------------------linha2-----------------------------

        self.EntrySenha = ctk.CTkEntry(self.frameCad, border_color="#00FF00", show="*", placeholder_text="Senha")
        self.EntrySenha.grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="ew")

        self.EntryCodEmpresa = ctk.CTkEntry(self.frameCad, border_color="#00FF00", placeholder_text="Código da empresa")
        self.EntryCodEmpresa.grid(row=3, column=2, columnspan=2, padx=3, pady=3, sticky="ew")

        #----------------------Linha3------------------------------

        self.EntryConfirmarSenha = ctk.CTkEntry(self.frameCad, border_color="#00FF00", show="*", placeholder_text="Confirme a senha")
        self.EntryConfirmarSenha.grid(row=4, column=0, columnspan=2, padx=3, pady=3, sticky="ew")

        self.EntryCelular = ctk.CTkEntry(self.frameCad, border_color="#00FF00", placeholder_text="Celular")
        self.EntryCelular.grid(row=4, column=2, columnspan=2, padx=3, pady=3, sticky="ew")

        #--------------------Linha4-----------------------------------

        self.EntryEmail = ctk.CTkEntry(self.frameCad, border_color="#00FF00", placeholder_text="Email")
        self.EntryEmail.grid(row=5, column=0, columnspan=4, padx=3, pady=3, sticky="ew")

        #--------------------linha5-----------------------------------
        self.BotaoCadastrar = ctk.CTkButton(self.frameCad, text="Confirmar", fg_color="#00FF00", text_color="black", command= self.cadastrar)
        self.BotaoCadastrar.grid(row=6, column=0, columnspan=2, padx=3, pady=10, sticky="ew")

        self.BotaoCancelar = ctk.CTkButton(self.frameCad, text="Cancelar", fg_color="#00FF00", text_color="Black", command=self.back_tela_cadastro)
        self.BotaoCancelar.grid(row=6, column=2, columnspan=2, padx=3, pady=10, sticky="ew")
    
    def back_tela_cadastro(self):
        self.frameCad.destroy()
        self.frame_tela_login()
        self.widgets_login()
    
    def update_time(self):
        self.current_time = dt.now().strftime('%H:%M:%S')
        self.caixahora.configure(text=self.current_time)
        self.caixahora.after(1000, self.update_time)  # Atualiza a hora a cada 1000 milissegundos (1 segundo)

    def frame_container_user(self):
        # Ajuste as dimensões do frameContainer para 1080x500
        self.frameContainerUser = ctk.CTkFrame(self.janela, fg_color="transparent", width=1080, height=600)
        self.frameContainerUser.pack_propagate(0)  # Impede o frameContainer de se ajustar automaticamente 

    def tela_inicial_usuario(self):
        self.frame_container_user()
        self.frameHeaderUser = ctk.CTkFrame(self.janela, fg_color="#00ff00", height=100)
        self.frameCentral = ctk.CTkFrame(self.frameContainerUser, fg_color="transparent", width=296, height=600)
      
        #cabeçalho
        self.frameHeaderUser.pack_propagate(0)
        self.frameHeaderUser.pack(side=ctk.TOP, fill=ctk.X)
        self.logo_header_header = ctk.CTkLabel(self.frameHeaderUser, image=self.logo_header, text="")
        self.logo_header_header.pack(side=ctk.LEFT, padx=20)

        self.botaoTelaInicioUser = ctk.CTkButton(self.frameHeaderUser, text="Inicio", corner_radius=100, border_width=2, border_color="", fg_color="black", text_color="#00ff00", command=self.btn_TelaInicioUser)
        self.botaoTelaInicioUser.pack(side=ctk.RIGHT, padx=20)

        self.botaoTelaUserUser = ctk.CTkButton(self.frameHeaderUser, text="Perfil", corner_radius=100, border_width=2, border_color="black", fg_color="#00ff00", text_color="black", command=self.btn_TelaUser)
        self.botaoTelaUserUser.pack(side=ctk.RIGHT)
        
        #container que abriga a área de registro de pontos, centro e as avisos
        self.frameContainerUser.pack(pady=50)

        #cards central, registro e de notificações
        self.frameCentral.grid(row=0, column=2, padx=80)

        #------------------central-----------------------
        self.frameCentral.pack_propagate(0)
        self.tipoRegistro = ctk.CTkLabel(self.frameCentral, image=self.fundotipoRegistro, text="ENTRADA", font=('',40))
        self.tipoRegistro.pack()
        

        self.caixahora = ctk.CTkLabel(self.frameCentral, image=self.fundocaixaHora, text="", font=('Helvetica', 32))
        self.caixahora.pack(pady=50)

        self.botaoPrincipal = ctk.CTkButton(self.frameCentral, text="MARCAR PONTO", fg_color="transparent", border_color="red", border_width=2, width=296, height=62, font=("Arial", 25))
        self.botaoPrincipal.pack()

        self.update_time()

    def tela_usuario(self):
        #conteudo--------------------------------------------------------------------------------
        self.frame_container_user()
        self.frameContainerUser.pack(pady=50)

        self.labelNomeUser = ctk.CTkLabel(self.frameContainerUser, text="Isabelle Moura", font=("arial", 24), text_color="white")
        self.labelNomeUser.grid(row=0,column=1) 

        self.labelCargoUser = ctk.CTkLabel(self.frameContainerUser, text="Cargo: Administrador", text_color="white", anchor="w")
        self.labelCargoUser.grid(row=1,column=1)

        self.labelCargoUser = ctk.CTkLabel(self.frameContainerUser, text="Empresa 38347", text_color="white")
        self.labelCargoUser.grid(row=1,column=2)

        self.buttonFoPontoUser = ctk.CTkButton(self.frameContainerUser, text="Folhas de Ponto", border_width=2, fg_color="transparent",border_color="#00ff00", text_color="white", width=152, height=152, command= self.button_callbck)# command=lambda: folha_ponto(self))
        self.buttonFoPontoUser.grid(row=2,column=1, padx=20, pady=20)

        self.buttonInfoPessoais = ctk.CTkButton(self.frameContainerUser, text="Informações \nPessoais", border_width=2, fg_color="transparent",border_color="#00ff00", text_color="white", width=152, height=152, command=lambda: self.button_callbck)# command=lambda: funcionarios(self))
        self.buttonInfoPessoais.grid(row=2,column=2, padx=20, pady=20)

        self.buttonReErroUser = ctk.CTkButton(self.frameContainerUser, text="Relatar Erro", border_width=2, fg_color="transparent",border_color="#00ff00", text_color="white", width=152, height=152, command= self.generate_log)# command=lambda: relatar_erro(self))
        self.buttonReErroUser.grid(row=3,column=1, padx=20, pady=20)

        self.buttonSairContaUser = ctk.CTkButton(self.frameContainerUser, text="Sair", border_width=2, fg_color="transparent",border_color="#00ff00", text_color="white", width=152, height=152, command= self.sair)# command=lambda: sair_conta(self))
        self.buttonSairContaUser.grid(row=3,column=2, padx=20, pady=20)

    def btn_TelaInicioUser(self):
        self.frameContainerUser.destroy()
        self.tela_inicial_usuario()
        self.frameHeaderUser.destroy()
    
    def btn_TelaUser(self):
        self.frameContainerUser.destroy()
        self.tela_usuario()

    def tela_admin(self):
        #frame container-------------------------------------------------------------------------
        self.frameContainerAdmin = ctk.CTkFrame(self.janela, fg_color="transparent", width=1080, height=600)
        self.frameContainerAdmin.pack_propagate(0)  # Impede o frameContainerAdmin de se ajustar automaticamente

        #cabeçalh-------------------------------------------------------------------------------
        self.frameHeaderAdmin = ctk.CTkFrame(self.janela, fg_color="#FFE500", height=100)

        self.frameHeaderAdmin.pack_propagate(0)
        self.frameHeaderAdmin.pack(side=ctk.TOP, fill=ctk.X)
        self.logo_header_header_admin = ctk.CTkLabel(self.frameHeaderAdmin, image=self.logo_header_admin, text="")
        self.logo_header_header_admin.pack(side=ctk.LEFT, padx=20)

        #conteudo--------------------------------------------------------------------------------

        self.frameContainerAdmin.pack(pady=50)
        
        self.labelNome = ctk.CTkLabel(self.frameContainerAdmin, text="Isabelle Moura", font=("arial", 24), text_color="white")
        self.labelNome.grid(row=0,column=1) 

        self.labelCargo = ctk.CTkLabel(self.frameContainerAdmin, text="Cargo: Administrador", text_color="white", anchor="w")
        self.labelCargo.grid(row=1,column=1)

        self.labelCargo = ctk.CTkLabel(self.frameContainerAdmin, text="Empresa 38347", text_color="white")
        self.labelCargo.grid(row=1,column=2)

        self.buttonFoPonto = ctk.CTkButton(self.frameContainerAdmin, text="Folhas de Ponto", border_width=2, fg_color="transparent",border_color="#FFE500", text_color="white", width=152, height=152, command=lambda: self.button_callbck)# command=lambda: folha_ponto(self))
        self.buttonFoPonto.grid(row=2,column=1, padx=20, pady=20)

        self.buttonFuncionarios = ctk.CTkButton(self.frameContainerAdmin, text="Funcionário", border_width=2, fg_color="transparent",border_color="#FFE500", text_color="white", width=152, height=152, command=lambda: self.button_callbck)# command=lambda: funcionarios(self))
        self.buttonFuncionarios.grid(row=2,column=2, padx=20, pady=20)

        self.buttonReErro = ctk.CTkButton(self.frameContainerAdmin, text="Relatar Erro", border_width=2, fg_color="transparent",border_color="#FFE500", text_color="white", width=152, height=152, command= self.generate_log)# command=lambda: relatar_erro(self))
        self.buttonReErro.grid(row=3,column=1, padx=20, pady=20)

        self.buttonSairConta = ctk.CTkButton(self.frameContainerAdmin, text="Sair", border_width=2, fg_color="transparent",border_color="#FFE500", text_color="white", width=152, height=152, command=lambda: self.sair)# command=lambda: sair_conta(self))
        self.buttonSairConta.grid(row=3,column=2, padx=20, pady=20)

    

    def generate_log(self):
        logging.debug('Botão pressionado')
        messagebox.showinfo("Aviso", "Relatado com sucesso!")


Application()