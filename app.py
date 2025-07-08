import streamlit as st

# Configuração da página
st.set_page_config(page_title="CV - Diogo Minoru Kokubu", layout="wide")

# Header
st.title("👨‍💻 Diogo Minoru Kokubu")
st.subheader("Analista de BI | Engenharia de Dados | Análise de Dados | dbt | SQL")
st.markdown("📍 Maringá - PR | (44) 9 9159-3628")
st.markdown("[📧 E-mail](diogominoru@hotmail.com) | [🔗 LinkedIn](https://www.linkedin.com/in/diogokokubu) | [💻 GitHub](https://github.com/diogo-minoru)")

# Seção: Objetivo
st.header("🎯 Objetivo")
st.markdown("**Engenheiro de Dados** ou **Analista de Dados**")

# Seção: Qualificações Técnicas
st.header("🛠️ Qualificações Técnicas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Ferramentas e Plataformas")
    st.markdown("- Git - dbt - Docker - Airflow - Prefect - Power BI - QlikView - Pentaho")

with col2:
    st.subheader("Programação e Linguagens")
    st.markdown("- SQL - DAX - Python")

# Seção: Experiência Profissional
st.header("💼 Experiência Profissional")

with st.expander("Analista de BI Jr. - Santa Casa de Maringá (Mai/2024 - Atual)"):
    st.markdown("""
- Implemento pipelines de ETL de dados com DBT, Pentaho e Prefect, extraindo dados de Oracle para PostgreSQL.
- Realizo análises em conjunto com os setores da instituição, identificando gargalos e propondo melhorias com base em dados.
- Participo ativamente na construção do Data Warehouse institucional.
- Desenvolvo dashboards e indicadores com Power BI, QlikView e consultas SQL ad hoc.
- Valido informações junto aos setores da instituição, propondo soluções baseadas em dados e insights operacionais.
    """)

with st.expander("Assistente de BI - Santa Casa de Maringá (Ago/2022 - Abr/2024)"):
    st.markdown("""
- Modelei dados e desenvolvi processos de ETL com SQL em bancos de dados Oracle, garantindo a confiabilidade dos dados para análise.
- Mantive e otimizei aplicações em QlikView, melhorando a performance de relatórios utilizados por diferentes áreas.
- Ofereci suporte técnico e atendimento aos usuários, contribuindo para decisões mais assertivas com base em dados.
- Documentei fluxos e processos analíticos, colaborando com a padronização de entregas da área.
- Manutenção de aplicações já existentes.
    """)

with st.expander("Assistente de Inteligência de Mercado - Century (Ago/2021 - Ago/2022)"):
    st.markdown("""
- Criei e mantive indicadores de performance comercial com Microsoft Power BI, apoiando a tomada de decisão do time comercial.
- Realizei extrações de dados do Oracle e transformações no Power Query, estruturando bases confiáveis para análise.
- Implementei regras de acesso com Row-Level Security (RLS), controlando a visualização dos dados por cliente.
- Atuei no suporte aos usuários, garantindo usabilidade e aderência dos dashboards à realidade de negócio.
    """)

# Seção: Formação Acadêmica
st.header("🎓 Formação Acadêmica")
st.markdown("**Engenharia de Produção com Ênfase em Software** — Universidade Estadual de Maringá (2015–2021)")

# Seção: Certificações
st.header("📜 Certificações")
st.markdown("""
- **AWS Certified Cloud Practitioner** — AWS (Jun/2025 - Jun/2028)
- O AWS Certified Cloud Practitioner valida a compreensão básica e de alto nível dos serviços, da terminologia e da Nuvem AWS.
""")

# Seção: Projetos
st.header("💡 Projetos")
with st.expander("Docker para executar aplicação streamlit"):
    st.markdown("""
- 🔗 [Repositório no GitHub](https://github.com/diogo-minoru/docker)
- Aplicando conceitos de containers para executar aplicações.
- Utilizando o gerenciador de pacotes uv e streamlit para criar uma aplicação e realizando um deploy na cloud "render".
    """)

with st.expander("Web Scraping do site maringa.com"):
    st.markdown("""
- 🔗 [Repositório no GitHub](https://github.com/diogo-minoru/scrapy_empregos)
- Programa criado utilizando a linguagem Python e a biblioteca Scrapy para coletar informações das vagas de empregos publicadas no site.
- Para cada vaga de emprego publicada, são coletadas as informações de: nome da vaga, experiência, área, nome da empresa, cidade, estado, data de publicação e link para a vaga.
    """)

# Seção: Cursos Complementares
st.header("📖 Cursos Complementares")
st.markdown("""
- **Desenvolvedor SQL Server** — DataCamp (2022)
- **Análise de Dados com Python** — DataCamp (2022–2023)
- **Introdução ao MongoDB** — MongoDB (2024)
- **Modelagem de Dados com MongoDB** — MongoDB (2024)
- **Introdução ao Git e GitHub** — Jornada de Dados (2025)
""")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Diogo Minoru Kokubu")
