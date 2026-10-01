## Sistema de Certificados

Sistema web para geração de certificados em PDF.

O projeto possui um frontend desenvolvido com Nexts.js e um backend desenvolvido com Python.

## Tecnologias

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- Python 3.12
- Flask
- Flask-CORS
- ReportLab

# Funcionalidades

- Preenchimento do nome do participante
- Preenchimento do nome do curso
- Informar a carga horária
- Envio dos dados para a API Python
- Geração automática do certificado em PDF
- Download automático do certificado

## Estrutura 

```text
SistemaCertificados-main/
└── SistemaCertificados-main/
    ├── app.py
    ├── certificado.pdf
    ├── requirements.txt
    ├── .gitignore
    └── README.md
```

## Backend

Utiliza o Flask e disponibiliza na porta 5000.

# Endpoint

POST /certificado

Dados Enviados

{
  "nome": "Mariana",
  "curso": "Curso de Informática",
  "cargaHoraria": "40 horas"
}

Resposta 

A API retorna um arquivo em PDF:

certificado.pdf

## Instalação

É necessário ter Python 3.12 instalado.

Entre na pasta do backend:
cd "C:\Users\aluno.petrolina\Downloads\SistemaCertificados-main\SistemaCertificados-main"

Instale as dependências:
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m pip install -r requirements.txt

## Executando o backend

Execute:
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" app.py

A API ficará disponível em:
http://localhost:5000

## Testando a API

Exemplo de dados:

{
  "nome": "Mariana",
  "curso": "Curso de Informática",
  "cargaHoraria": "40 horas"
}

O frontend envia esses dados para:

http://localhost:5000/certificado

# Frontend

O frontend utiliza Next.js

- Para executa o frontend, entre na pasta do projeto frontend e instale as dependências
npm install

- Depois execute
npm run dev

O frontend será disponibilizado em:
http://localhost:3001

# Funcionamento

O usuário preenche:
* Nome;
* Curso;
* Carga Horária.

Ao clicar em Gerar Certificado, o frontend realiza uma requisição:
Frontend
   ↓
POST /certificado
   ↓
Flask
   ↓
ReportLab
   ↓
PDF
   ↓
Download do certificado

# Exemplo de certificado

O certificado gerado contém:

CERTIFICADO

Certificamos que Mariana

concluiu o curso Curso de Informática

Carga horária: 40 horas

# Desenvolvimento

Frontend:

http://localhost:3001

Backend:

http://localhost:5000