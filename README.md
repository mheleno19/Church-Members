# Church Members

### Visão Geral do Projeto
**Descrição**: Aplicação para gerenciar membros de uma igreja. Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Streamlit, destinada ao gerenciamento de membros da igreja.  A aplicação inclui uma interface para autenticação de usuário, que restringe o acesso a páginas específicas, como a de consulta de dados dos membros.

**Objetivos**: Permitir o cadastro, consulta, edição e exclusão de membros da igreja, e com isso gerenciar a membresia.

### Estrutura do Projeto
- `Church-Members.py`: Arquivo principal da aplicação.
- `Pages/`: Contém as páginas da aplicação.
- `Controllers/`: Contém os controladores da aplicação.
- `services/database.py`: Conexão com o banco de dados.
- `membros.py`: Representa a estrutura de dados de um membro da igreja
- `requirements.txt`: Contém as bibliotecas da aplicação

### Configuração do Ambiente
**Pré-requisitos**: 
- Python 3.10+
- PostgreSQL
- Bibliotecas Python:
-- Streamlit
-- Pandas
-- Requests

### Instalação
**1. Clone o Repositório:**
```sh
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

**2. Crie um Ambiente Virtual (opcional, apenas recomendação):**
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3. Instale as Dependências:**
```sh
pip install -r requirements.txt
```

**4. Execute a Aplicação:**
```sh
streamlit run main.py
```

**5. Acesse a aplicação:**
```
A aplicação será acessível pelo navegador em http://localhost:8501 
(POSTERIOMENTE SERÁ FEITO DEPLOY EM SERVIDOR)
```

## Contribuição
**Para contribuir com o projeto:**
1. Faça um fork do repositório
2. Crie uma nova branch para suas alterações
3. Faça um commit das alterações
4. Envie suas alterações para o repositório remoto
5. Abra um pull request para revisão.



    





