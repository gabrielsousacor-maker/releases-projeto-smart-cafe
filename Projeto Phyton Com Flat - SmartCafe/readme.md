# ☕ Smart Café – Sistema em Python com Flat

Este projeto simula o sistema de uma cafeteria inteligente, desenvolvido com Python e Flat. Ele inclui telas de login, visualização de produto, permissões de usuário e navegação entre telas. Os dados são armazenados em arquivos JSON, ideal para protótipos e projetos acadêmicos.

---

## 🚀 Funcionalidades
- 🔐 Tela de login com validação
- 📦 Exibição de produto com imagem e características
- 👤 Permissões de usuário por nível
- 🧭 Navegação entre telas
- 📁 Dados armazenados em JSON

---

## 🗂️ Estrutura de Pastas
## 🗂️ Estrutura de Pastas
projeto/
├── [app.py](app.py)                  # Arquivo principal que inicia o app
│
├── data/                             # Dados fixos em JSON
│   ├── [produto.json](data/produto.json)        # Dados do produto
│   └── [usuario.json](data/usuario.json)        # Dados do usuário
│
├── models/                           # Classes que representam entidades
│   ├── [produto.py](models/produto.py)
│   └── [usuario.py](models/usuario.py)
│
├── screens/                          # Telas da aplicação (UI)
│   ├── [home_screen.py](screens/home_screen.py)
│   ├── [login_screen.py](screens/login_screen.py)
│   ├── [main.py](screens/main.py)                # Gerencia navegação
│   ├── [permissoes_screen.py](screens/permissoes_screen.py)
│   ├── [produto_screen.py](screens/produto_screen.py)
│   └── [sucesso_screen.py](screens/sucesso_screen.py)
│
├── services/                         # Regras de negócio / lógica
│   ├── [autenticacao.py](services/autenticacao.py)     # Valida login
│   └── [produto_service.py](services/produto_service.py) # Busca produto
│
├── static/                           # Arquivos estáticos (imagens, ícones, logos)
│   ├── [cafeteria.jpg](static/cafeteria.jpg)
│   └── [logoempresa.jpg](static/logoempresa.jpg)
│
└── utils/                            # Utilitários
    └── [json_loader.py](utils/json_loader.py)           # Funções para carregar JSON


---

## 🧠 Tecnologias Usadas
- 🐍 Python
- 🎨 Flet
- 📄 JSON

---

## ▶️ Como Executar
1. Instale o Flet:
   ```bash
   pip install flet

## Execute o app:
python app.py


## 📄 Documentação

## 📄 Documentação
- Slides acadêmicos em PDF: [`docs/SmartCafe.pdf`](docs/SmartCafe.pdf)  
- Projeto completo: [`releases/projeto-smart-cafe`](releases/projeto-smart-cafe)


 ## 👨‍🎓 Créditos
Desenvolvido por Gabriel Sales 
Projeto: Desenvolvimento de uma empresa de cafeteria / Phyton com Flat 


