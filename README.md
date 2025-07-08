# 🐳 Docker - Containerização de Aplicações

## 📦 O que é Docker?

Docker é uma plataforma que permite **empacotar, distribuir e executar aplicações em containers**. Com ele, você garante que sua aplicação funcione da mesma forma em qualquer ambiente — seja no seu computador, no servidor de produção ou em um serviço de nuvem.

---

## 🚀 Vantagens do Docker

- ✅ Isolamento de ambiente
- 📦 Deploy consistente e reproduzível
- 🔁 Facilidade para versionar e atualizar
- 🐍 Compatível com qualquer linguagem
- 📁 Integração com CI/CD e orquestradores como Kubernetes

---

## 🛠️ Principais Comandos

### 📥 Build da imagem
```bash
docker build -t nome-da-imagem .
```

### ▶️ Executar um container
```bash
docker run -d -p 8000:8000 nome-da-imagem
```

### 📄 Ver containers em execução
```bash
docker ps
```

### ❌ Parar e remover containers
```bash
docker stop <container_id>
docker rm <container_id>
```

### 🧹 Limpar recursos não utilizados
```bash
docker system prune
```

### 📁 Estrutura típica de um projeto com Docker
```bash
📦 meu-projeto/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml (opcional)
```

### 🐳 Exemplo de Dockerfile para app Python
```bash
# Usa uma imagem base com Python
FROM python:3.11

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao iniciar o container
CMD ["python", "app/main.py"]
```