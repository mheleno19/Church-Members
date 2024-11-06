import streamlit as st
import sys
import datetime
import requests
import Controllers.MembrosControllers as MembrosControllers

# Adiciona o diretório raiz ao caminho do sistema
sys.path.append(r'C:\Users\mhele\Documents\VisualCode\PROJETO')


def create(paramId=None):
    # Acessa os parâmetros de consulta diretamente
    query_params = st.query_params
    membroBD = None  # Recuperando o cadastro do membro do BD

    if paramId is not None:  # Use paramId se for passado
        idEditar = int(paramId)  # Converter o ID para inteiro
        membroBD = MembrosControllers.selecionar_id(idEditar)
        st.markdown("<h1 style='font-size:24px;'>Alterar Membro</h1>",
                    unsafe_allow_html=True)
    else:
        st.markdown(
            "<h1 style='font-size:24px;'>Inserir Novos Membros</h1>", unsafe_allow_html=True)

    # Lista dos ministérios
    lista_ministerios = ["Louvor", "Dança", "Teatro", "Coral",
                         "Mídia (Som, Projeção, Fotos)", "Escola Infantil", "Serviço de Culto", "(nenhum)"]

    with st.form(key="include_membro"):
        if membroBD is None:
            # Inputs para novo membro
            input_name = st.text_input(label="Nome completo")
            input_age = st.number_input(label="Idade", format="%d", step=1)

            # Restringe data de nascimento a um intervalo específico (exemplo: pessoas nascidas nos últimos 100 anos)
            input_date = st.date_input(
                label="Data de Nascimento",
                value=datetime.date.today(),
                min_value=datetime.date(
                    datetime.date.today().year - 100, 1, 1),
                max_value=datetime.date.today(),
            )

            input_phone = st.text_input(label="Telefone")
            input_civil_status = st.selectbox("Estado Civil", options=[
                                              "Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"])

            st.markdown("2. Endereço")

            # Campo de entrada do CEP e botão de confirmação organizados em colunas
            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                input_zip = st.text_input("CEP")

            with col2:
                st.write("")  # Adiciona um espaço vazio para alinhamento

            with col3:
                confirmar_cep = st.form_submit_button("Confirmar CEP")

            # Verifica o CEP ao clicar no botão
            if confirmar_cep and input_zip:
                if len(input_zip) == 8:
                    response = requests.get(
                        f"https://viacep.com.br/ws/{input_zip}/json/")
                    if response.status_code == 200:
                        endereco = response.json()
                        if "erro" not in endereco:
                            st.session_state["input_street"] = endereco.get(
                                "logradouro", "")
                            st.session_state["input_city"] = endereco.get(
                                "localidade", "")
                            st.session_state["input_state"] = endereco.get(
                                "uf", "")
                        else:
                            st.warning("CEP não encontrado.")
                    else:
                        st.error("Erro ao acessar a API ViaCEP.")
                else:
                    st.warning("Por favor, insira um CEP válido de 8 dígitos.")

            input_street = st.text_input(
                "Rua", value=st.session_state.get("input_street", ""))
            input_complemento = st.text_input("Complemento")
            input_city = st.text_input(
                "Cidade", value=st.session_state.get("input_city", ""))
            input_state = st.text_input(
                "Estado", value=st.session_state.get("input_state", ""))

            st.markdown("3. Outras Informações")
            input_ministry = st.multiselect(
                "Qual seu ministério?", options=lista_ministerios)

        else:
            # Inputs para editar membro
            input_name = st.text_input("Nome completo", value=membroBD.nome)
            input_age = st.number_input(
                "Idade", format="%d", step=1, value=membroBD.idade)
            input_date = st.date_input(
                "Data de Nascimento", value=membroBD.data_nascimento)
            input_phone = st.text_input("Telefone", value=membroBD.telefone)
            input_civil_status = st.selectbox(
                "Estado Civil",
                options=["Solteiro(a)", "Casado(a)",
                         "Divorciado(a)", "Viúvo(a)"],
                index=["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"].index(
                    membroBD.estado_civil)
            )

            st.markdown("2. Endereço")
            input_zip = st.text_input("CEP", value=str(membroBD.codigo_postal))
            input_street = st.text_input("Rua", value=membroBD.rua)
            input_complemento = st.text_input(
                "Complemento", value=membroBD.complemento)
            input_city = st.text_input("Cidade", value=membroBD.cidade)
            input_state = st.text_input("Estado", value=membroBD.estado)

            st.markdown("3. Outras Informações")
            default_ministry = [
                membroBD.ministerio] if membroBD.ministerio in lista_ministerios else []
            input_ministry = st.multiselect(
                "Qual seu ministério?", options=lista_ministerios, default=default_ministry)

        # Botão de envio para o formulário
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if membroBD is None:
            # Inclusão de novo membro
            MembrosControllers.incluir_membro(
                input_name, input_age, input_date, input_phone,
                input_street, input_complemento, input_city,
                input_state, input_zip, input_civil_status, input_ministry
            )
            st.success("Membro cadastrado com sucesso!")
        else:
            # Edição de membro existente
            MembrosControllers.editar_membro(
                idEditar, input_name, input_age, input_date, input_phone,
                input_street, input_complemento, input_city,
                input_state, input_zip, input_civil_status, input_ministry
            )
            st.success("Membro alterado com sucesso!")

        # Limpa os parâmetros de consulta e recarrega a página
        st.query_params.clear()


if __name__ == "__main__":
    create()
