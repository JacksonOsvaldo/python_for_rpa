# python_for_rpa
Repositório com as aplicações que faremos em live.

# Arquiteutura
A intenção nesse projeto é utilizarmos uma arquitetura limpa, no caso a hexagonal. Aqui um exemplo de como ficará nossa aplicação.

```
project_root/
│
├── app/                    # Camada de interface e entrada
│   ├── main.py             # Runner principal que inicializa o RPA
│   ├── config.py           # Configurações gerais do projeto (ex.: env)
│   └── runners/            # Módulos específicos de runners
│       ├── __init__.py
│       ├── generic_runner.py  # Classe genérica de runner
│       └── custom_runner.py   # Runners customizados
│
├── core/                   # Camada de domínio (regras de negócio)
│   ├── __init__.py
│   ├── entities/           # Definições de entidades do domínio (ex.: Tarefas, Processos)
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/           # Lógica de negócios independente de tecnologia
│   │   ├── __init__.py
│   │   └── task_service.py # Exemplo de lógica de manipulação de tarefas
│   └── use_cases/          # Casos de uso do RPA (ex.: ExecuteTask, MonitorTask)
│       ├── __init__.py
│       └── execute_task.py
│
├── infrastructure/         # Camada de infraestrutura
│   ├── __init__.py
│   ├── repositories/       # Implementações de persistência e armazenamento
│   │   ├── __init__.py
│   │   └── task_repository.py
│   ├── external_services/  # Conexões com serviços externos (ex.: API, banco)
│   │   ├── __init__.py
│   │   └── external_api.py
│   └── adapters/           # Adaptações de dependências de sistema (ex.: Selenium)
│       ├── __init__.py
│       └── selenium_adapter.py
│
├── tests/                  # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_app/           # Testes da camada de interface
│   ├── test_core/          # Testes da camada de domínio
│   └── test_infrastructure/ # Testes da camada de infraestrutura
│
└── requirements.txt        # Dependências do projeto
```

# Tecnologias
Vamos abordar assuntos como Selenium, SAP, aplicações desktop, API e Orquestração de RPAs.
