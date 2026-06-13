# 🔒 SecurePass

Sistema de Geração e Gerenciamento de Senhas desenvolvido em Python utilizando Tkinter para interface gráfica e JSON para armazenamento de dados.

---

## 📋 Sobre o Projeto

O SecurePass foi criado com o objetivo de auxiliar usuários na geração e gerenciamento de senhas seguras para diferentes serviços digitais.

A aplicação permite gerar senhas aleatórias, armazenar credenciais e consultar registros de forma simples e intuitiva através de uma interface gráfica desktop.

Este projeto foi desenvolvido como atividade prática da disciplina **Development With Python**, aplicando conceitos de programação orientada a objetos, interfaces gráficas e persistência de dados.

---

## 🚀 Funcionalidades

### 🔑 Gerador de Senhas

* Geração automática de senhas seguras.
* Personalização do tamanho da senha.
* Utilização de:

  * Letras maiúsculas
  * Letras minúsculas
  * Números
  * Caracteres especiais

### 💾 Gerenciamento de Credenciais

* Cadastro de serviços.
* Armazenamento de login.
* Armazenamento de senha.
* Exibição das credenciais em tabela.

### 📂 Persistência de Dados

* Armazenamento local em arquivo JSON.
* Recuperação automática dos registros salvos.

---

## 🛠 Tecnologias Utilizadas

* Python 3
* Tkinter
* JSON
* Random
* String
* VS Code
* GitHub

---

## 📁 Estrutura do Projeto

```text
SecurePassManager/

├── app.py
├── passwords.json
├── assets/
│   └── logo.png
├── README.md
└── requirements.txt
```

---

## ▶️ Como Executar

### 1. Clone o Repositório

```bash
git clone https://github.com/SEU-USUARIO/securepass-manager.git
```

### 2. Acesse a Pasta

```bash
cd securepass-manager
```

### 3. Execute a Aplicação

```bash
python app.py
```

---

## 🖥️ Interface do Sistema

A aplicação possui uma interface gráfica desenvolvida com Tkinter contendo:

* Área de geração de senhas.
* Cadastro de credenciais.
* Visualização dos registros salvos.
* Mensagens de confirmação e validação.

---

## 📸 Evidências do Projeto

Inserir imagens da aplicação:

### Tela Inicial

<img src="screenshots/tela-inicial.png" width="700">

### Gerador de Senhas

<img src="screenshots/gerador.png" width="700">

### Cadastro de Credenciais

<img src="screenshots/cadastro.png" width="700">

### Lista de Credenciais

<img src="screenshots/listagem.png" width="700">

---

## 📊 Fluxo de Funcionamento

```text
Início
   ↓
Gerar Senha
   ↓
Cadastrar Credencial
   ↓
Salvar no JSON
   ↓
Exibir na Tabela
   ↓
Encerrar Sistema
```

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos da disciplina Development With Python.
* Desenvolver uma aplicação funcional utilizando interface gráfica.
* Implementar armazenamento persistente de dados.
* Demonstrar conhecimentos de programação orientada a objetos.

---

## 🔮 Melhorias Futuras

* Criptografia das senhas armazenadas.
* Senha mestra de acesso.
* Banco de dados SQLite.
* Pesquisa de credenciais.
* Exclusão e edição de registros.
* Exportação para PDF.
* Backup em nuvem.

---

## 👨‍💻 Autor

**Guilherme Melo Martins**

**RA:** 155370

**Curso:** Análise e Desenvolvimento de Sistemas

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina **Development With Python**.
