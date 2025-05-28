# tika-server-docker

---

```markdown
# 📖 Projeto: Apache Tika Server + UI Flask + MongoDB + Mongo Express via Docker Compose

Este projeto oferece um ambiente completo para análise de documentos com OCR e extração de metadados usando **Apache Tika Server**, salvando os resultados em um **MongoDB** persistente, com **UI web em Flask** e administração via **Mongo Express**.

## 📦 Serviços

| Serviço        | Porta Local | Descrição                                |
|:---------------|:------------|:-----------------------------------------|
| Tika Server    | 9998         | API REST para OCR e extração de metadados |
| MongoDB        | 27018        | Banco de dados Mongo (volume persistente em `/storage/tika`) |
| Mongo Express  | 8082         | UI Web para o MongoDB com autenticação   |
| UI Flask       | 5000         | Interface web para upload, histórico e exportação |

## 📂 Estrutura de Diretórios


tika-stack/
├── docker-compose.yml
├── tika-config.xml
├── ui/
│   ├── app.py
│   └── templates/
│       ├── index.html
│       └── results.html
└── /storage/tika/    # Diretório persistente de dados do MongoDB no host



## 🚀 Como Rodar

### 1️⃣ Crie o diretório persistente no host:

```bash
sudo mkdir -p /storage/tika
sudo chown 999:999 /storage/tika
````

### 2️⃣ Suba os containers:

```bash
docker compose up -d --build
```

## 🔐 Credenciais

**Mongo Express:**

* Usuário: `admin`
* Senha: `admin123`

## 🌐 Endpoints e Funcionalidades

| URL                             | Descrição                                           |
| :------------------------------ | :-------------------------------------------------- |
| `http://localhost:5000/`        | Upload de arquivos para análise com OCR e metadados |
| `http://localhost:5000/history` | Histórico das análises feitas                       |
| `http://localhost:5000/export`  | Exporta todo o histórico em formato JSON            |
| `http://localhost:8082/`        | Mongo Express UI (administração do banco MongoDB)   |
| `http://localhost:9998/`        | API REST do Apache Tika Server                      |

## 📑 Observações

* A extração OCR está embutida no Apache Tika Server (OCR via Tesseract embutido no container oficial).
* Os resultados são salvos no MongoDB com metadados e conteúdo extraído.
* O MongoDB usa volume persistente no host em `/storage/tika`.
* O container do Tika Server não utiliza mais a flag `--enableUnsecureFeatures`, pois não é compatível na versão atual.

## 🛑 Parar os serviços

```bash
docker compose down
```


