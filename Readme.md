# 🎭 Projeto de Automação de Testes com Playwright e Pytest

Projeto desenvolvido durante o curso de automação de testes com **Playwright e Pytest**, com o objetivo de aplicar conceitos de testes End-to-End (E2E), organização de testes, fixtures, configuração de ambientes e boas práticas de automação.

> ⚠️ Este projeto foi criado para fins de aprendizado e evolução profissional, utilizando como base a estrutura apresentada durante o curso ministrado por **Fernando Papito (TestBeyond)**, com adaptações e implementações próprias.

---

## 🎯 Objetivos

Os principais objetivos deste projeto são:

- Desenvolver testes E2E utilizando Playwright;
- Utilizar Python como linguagem de automação;
- Estruturar testes utilizando Pytest;
- Automatizar cenários funcionais;
- Validar resultados através de assertions;
- Criar uma estrutura organizada e escalável;
- Praticar técnicas de debugging;
- Evoluir gradualmente a arquitetura do projeto;
- Aplicar conhecimentos de QA Manual na automação.

---

## 🛠️ Tecnologias e ferramentas utilizadas

| Tecnologia / Ferramenta | Utilização |
|---|---|
| 🐍 **Python 3.11+** | Linguagem utilizada na automação |
| 🎭 **Playwright** | Automação de navegadores e testes E2E |
| 🧪 **Pytest** | Framework para execução e organização dos testes |
| 🔌 **pytest-playwright** | Integração entre Pytest e Playwright |
| 🖥️ **Cursor** | Ambiente de desenvolvimento com recursos de IA |
| 📦 **pip** | Gerenciamento de dependências |
| 🌱 **Git** | Controle de versão |
| 🐙 **GitHub** | Versionamento, documentação e portfólio |

---

## 📋 Pré-requisitos

- Python 3.11+
- pip

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/TestBeyond/playwright-pytest.git
cd playwright-pytest

# Instale as dependências
pip install -r requirements.txt

# Instale os browsers
playwright install
```

## 🧪 Executando os Testes

```bash
# Todos os testes
pytest

# Testes E2E específicos
pytest -m e2e

# Com relatório detalhado
pytest -v

# Em modo visual (headed)
pytest --headed

# Em browser específico
pytest --browser firefox

# Teste específico
pytest playwright/e2e/test_landing_page.py::test_landing_page
```

## 📁 Estrutura do Projeto

```
playwright-pytest/
├── playwright/
│   ├── conftest.py              # Configurações do pytest e fixtures
│   └── e2e/
│       └── test_landing_page.py # Testes end-to-end
├── requirements.txt             # Dependências Python
├── pytest.ini                   # Configurações do pytest
└── README.md
```

## 🔧 Configuração

### pytest.ini
```ini
[pytest]
testpaths = playwright
markers =
    e2e: End-to-end tests
```

### Variáveis de Ambiente (opcional)
```bash
BASE_URL=https://testbeyond.com
HEADLESS=true
```

## 📝 Exemplo de Teste

```python
import pytest
from playwright.sync_api import expect

@pytest.mark.e2e
def test_home(page):
    page.goto('https://testbeyond.com')
    expect(page).to_have_title('Projeto TestBeyond')
```

## 🐛 Debug

```bash
# Modo debug com Playwright Inspector
PWDEBUG=1 pytest

# Screenshots e vídeos
pytest --screenshot on --video on

# Pausar no código
page.pause()
```

## 📦 Dependências Principais

- pytest
- pytest-playwright
- playwright

