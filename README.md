# M5 - Kopa do Mundo
## Descrição
Descrição da API de Campeonato de Futebol
Eu desenvolvi uma API usando Python e Django para organizar um campeonato de futebol. Uma API possui várias rotas que permitem:

# Cadastrar Equipes
1. Terminal: /api/teams/(HTTP POST)
2. Parâmetros: Nome, Número de Títulos, Artilheiro Principal, Código FIFA, Ano da Primeira Participação na Copa
# Listar Equipes
1 .Terminal: /api/teams/(HTTP GET)
2 .Retornar Lista de todas as equipes cadastradas
# Filtrar Equipe Específica
1. Terminal: /api/teams/<team_id>/(HTTP GET)
2.Parâmetro: <team_id>- ID da equipe desejada
3.Retornar Detalhes da equipe específica
 # Atualizar Equipe
1. Endpoint: /api/teams/<team_id>/(HTTP PATCH)
2. Parâmetro: <team_id>- ID da equipe a ser atualizado
3. Modificações: Atributos da equipe a serem atualizados
# Deletar Equipe
1. Terminal: /api/teams/<team_id>/(HTTP EXCLUIR)
2. Parâmetro: <team_id>- ID da equipe a ser excluído
3. Tratamento Personalizado de Erros
4. Exceção: NegativeTitlesErrorpara proteger números de títulos negativos
5. Exceção: InvalidYearCupErrorpara anos inválidos de primeira participação na Copa
6. Exceção: ImpossibleTitlesErrorpara títulos impossíveis com base no ano da primeira participação
# Modelo de Dados
1. Criação: Classe Teamcom atletas como nome, número de títulos, artilheiro principal, código FIFA e ano da primeira participação na Copa
2. Sobrescrita: Método __repr__para exibir informações da equipe no formato desejado
3. Funcionalidades Gerais
4. Registro, listagem, filtragem, atualização e exclusão de equipes
5. Recursos personalizados para lidar com erros específicos
# Testes Implementados
1. Implementação de testes unitários
2. Testes abrangem diferentes funcionalidades da API
3. Todos os testes foram aprovados
4. Isso resume a descrição de sua API desenvolvida em Python e Django para um campeonato de futebol, suas funcionalidades e recursos personalizados para tratamento de erros.

## Como rodar os testes localmente

- Verifique se os pacotes pytest e/ou pytest-testdox estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o pytest e/ou pytest-testdox e/ou pytest-django em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest pytest-testdox -y
```

---

## Próximos passos:

### 1. Crie seu ambiente virtual:

```shell
python -m venv venv
```

### 2. Ative seu venv:

```shell
# Linux:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

### 3. Instalar o pacote <strong>pytest-testdox</strong>:

```shell
pip install pytest-testdox pytest-django
```

### 4. Rodar os testes referentes a cada tarefa isoladamente:

Exemplo:

- Tarefa 1

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

---

## Execução de testes a partir da tarefa 2

A partir de agora, para os testes das tarefas 2, 3 e 4, já que começaremos a usar o Django, precisaremos de um arquivo **pytest.ini**, você **DEVE** cria-lo na raiz do projeto, depois de criar esse aquivo você precisa adicionar nele a seguinte configuração:

```python
[pytest]
DJANGO_SETTINGS_MODULE = kopa_do_mundo.settings
```

Após isso, você pode executar os comandos abaixo para rodar os testes:

- Tarefa 1

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Tarefa 2

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```

- Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

- Tarefa 4

```shell
pytest --testdox -vvs tests/tarefas/tarefa_4/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo: executar somente "test_object_representation"

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_model.py::TeamModelTest::test_object_representation
```

Caso queira, também é possível rodar todos os testes de uma vez:

```shell
pytest --testdox -vvs
```
