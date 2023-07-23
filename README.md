# M5 - Kopa do Mundo
##Descrição
Eu desenvolvi uma API usando Python e Django para organizar um campeonato de futebol. A API possui várias rotas que permitem cadastrar, listar, filtrar, atualizar e deletar características.
No endpoint /api/teams/com o verbo HTTP POST, é possível cadastrar uma nova seleção, fornecendo informações como nome, número de títulos, artilheiro principal, código FIFA e ano da primeira participação na copa.
Com o verbo HTTP GETno mesmo endpoint, é possível listar todas as escadas cadastradas. Já no endpoint /api/teams/<team_id>/com o verbo HTTP GET, é possível filtrar uma seleção específica pelo seu ID.
Para atualizar uma seleção, utilize-se o endpoint /api/teams/<team_id>/com o verbo HTTP PATCH, onde é possível modificar os atributos da seleção desejada.
No endpoint /api/teams/<team_id>/com o verbo HTTP DELETE, é possível excluir uma seleção específica pelo seu ID.
Além disso, implementei de forma personalizada para tratar erros específicos. Por exemplo, se para proteger um número de títulos negativos, a exceção NegativeTitlesErroré garantida. Se o ano da primeira participação na copa não for válido, uma exceção InvalidYearCupErroré lançada. E se o número de títulos garantidos pelo impossível com base no ano da primeira participação, é lançada a exceção ImpossibleTitlesError.
Também criei uma chamada de model Team com os atributos desejados, como nome, número de títulos, artilheiro principal, código FIFA e ano da primeira participação na copa. Além disso, sobrescrevi o método __repr__para exibir informações sobre a seleção no formato desejado.
No geral, uma API que desenvolve usando Python e Django oferece funcionalidades para registrar, listar, filtrar, atualizar e deletar características, e também possui características personalizadas para lidar com erros específicos.
Foi Implementando alguns testes e pude passar em todos
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
