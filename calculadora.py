import streamlit as st

def display_ava1():
    st.subheader("a) Avaliação de mérito técnico-científico")
    st.write("Por favor, insira as notas de cada critério. As notas devem estar entre 0,0 e 10,0.")

    # Definindo os critérios e seus pesos
    criterios = {
        "1. Conformidade ao objetivo (Chamada/Objetivo e Objeto)": 3,
        "2. Estágio de desenvolvimento (pesquisa, produto e/ou processo)": 4,
        "3. Grau de inovação para o mercado nacional ou mundial e risco tecnológico": 4,
        "4. Capacitação técnica da equipe executora": 4,
        "5. Adequação da metodologia": 3,
        "6. Adequação da infraestrutura": 2,
        "7. Adequação do orçamento do projeto": 1,
        "8. Adequação do cronograma físico do projeto": 1,
    }

    # Criar campos para as notas
    notas = {}
    for criterio in criterios:
        nota = st.number_input(f"**{criterio} (Nota de 0,0 a 10,0)**", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
        notas[criterio] = nota

    # Calcular a nota total ponderada
    nota_total = sum(notas[criterio] * peso for criterio, peso in criterios.items())
    peso_total = sum(criterios.values())

    # Calcular a média ponderada
    media_ponderada = nota_total / peso_total

    # Exibir o valor total da soma das notas ponderadas e a média ponderada
    st.subheader("Resultado da Avaliação")
    st.write(f"**Soma total das notas ponderadas:** {nota_total:.2f}")
    st.write(f"**Média ponderada:** {media_ponderada:.2f}")

    return media_ponderada  # retorna a média ponderada diretamente para cálculo

def display_ava2():
    st.subheader("b) Avaliação de maturidade tecnológica de projeto")

    # Definindo os níveis de TRL e suas descrições
    niveis_trl = {
        "TRL/MLR 1": "Ideia da pesquisa que está sendo iniciada e esses primeiros indícios de viabilidade estão sendo traduzidos em pesquisa e desenvolvimento futuros.",
        "TRL/MLR 2": "Os princípios básicos foram definidos e há resultados com aplicações práticas que apontam para a confirmação da ideia inicial.",
        "TRL/MLR 3": "Em geral, estudos analíticos e/ou laboratoriais são necessários nesse nível para ver se uma tecnologia é viável e pronta para prosseguir para o processo de desenvolvimento. Neste caso, muitas vezes, é construído um modelo de prova de coesão.",
        "TRL/MLR 4": "Coloca-se em prática a prova de conceito, que consiste em sua aplicação em ambiente similar ao real, podendo constituir testes em escala de laboratório.",
        "TRL/MLR 5": "A tecnologia deve passar por testes mais rigorosos do que a tecnologia que está apenas na TRL 4, ou seja, validação em ambiente relevante de componentes ou arranjos experimentais, com configurações físicas finais. Capacidade de produzir protótipo do componente do produto.",
        "TRL/MLR 6": "A tecnologia constitui um protótipo totalmente funcional ou modelo representacional, sendo demonstrado em ambiente operacional (ambiente relevante no caso das principais tecnologias facilitadoras).",
        "TRL/MLR 7": "O protótipo está demonstrado e validade em ambiente operacional (ambiente relevante no caso das principais tecnologias facilitadoras).",
        "TRL/MLR 8": "A tecnologia foi testada e qualificada para o ambiente real, estando pronta para ser implementada em um sistema ou tecnologia já existente.",
        "TRL/MLR 9": "A tecnologia está comprovada em ambiente operacional (fabricação competitiva no caso das principais tecnologias facilitadoras), uma vez que já foi testada, validada, comprovada em todas as condições, com seu uso em todo seu alcance e qualidade. Produção estabelecida."
    }

    # Caixa de seleção para escolher o nível TRL
    nivel_selecionado = st.selectbox("Selecione o nível TRL:", list(niveis_trl.keys()))

    # Exibindo a descrição do nível selecionado
    st.write(f"**Descrição do {nivel_selecionado}:**")
    st.write(niveis_trl[nivel_selecionado])

    # Converter o nível TRL selecionado para uma pontuação numérica
    nota_trl = int(nivel_selecionado.split(" ")[-1])
    return nota_trl

def display_calculo_trl(nota_merito, nota_trl):
    st.subheader("Cálculo TRL")

    # Cálculo final
    nota_final = (nota_merito + nota_trl) / 2
    st.write(f"Nota final: **{nota_final:.2f}**")

if __name__ == '__main__':
    st.title("Avaliação de Projetos e-FAP")

    st.divider()

    # Avaliação de mérito técnico-científico
    nota_merito = display_ava1()

    st.divider()

    # Avaliação de maturidade tecnológica de projeto
    nota_trl = display_ava2()
    
    st.divider()

    # Cálculo final usando as notas normalizadas
    display_calculo_trl(nota_merito, nota_trl)