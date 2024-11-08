import Controllers.MembrosControllers as MembrosControllers
import streamlit as st
import pandas as pd
import sys
import Pages.Clientes.Create as PageCreate

# Adiciona o diretório raiz ao caminho do sistema
sys.path.append(r'C:\Users\mhele\Documents\VisualCode\PROJETO')

# Definindo as credenciais
USERNAME = "pastor"
PASSWORD = "admin123"


def login():
    st.markdown(
        "<h1 style='font-size:24px;'>Login do Administrador</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='font-size:15px;'>Página de uso exclusivo</h2>", unsafe_allow_html=True)

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == USERNAME and password == PASSWORD:
            st.session_state['authenticated'] = True
            st.success("Login bem-sucedido!")

            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")


def query():
    # Verifica se o usuário já está autenticado
    if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
        login()
        return  # Para aqui se o usuário não estiver autenticado

    # Obtém os parâmetros de consulta
    query_params = st.query_params
    paramId = query_params.get('id')

    if paramId is None:
        st.markdown(
            "<h1 style='font-size:24px;'>Consultar Membros</h1>", unsafe_allow_html=True)

        # Puxando os dados do BD
        membros_list = MembrosControllers.selecionar_todos()
        if not membros_list:
            st.write("Nenhum membro encontrado.")
            return

        # Converter a lista de membros em um DataFrame do pandas
        df_membros = pd.DataFrame([vars(item) for item in membros_list])

        # Botão para download dos dados em CSV
        csv = df_membros.to_csv(index=False)
        st.download_button(
            label="Baixar dados em CSV",
            data=csv,
            file_name='membros.csv',
            mime='text/csv',
        )

        for index, item in enumerate(membros_list):
            with st.expander(f"Membro {index + 1}: {item.nome}"):
                st.write(f"**ID**: {item.id}")
                st.write(f"**Nome**: {item.nome}")
                st.write(f"**Idade**: {item.idade}")
                st.write(f"**Data de Nascimento**: {item.data_nascimento}")
                st.write(f"**Telefone**: {item.telefone}")
                st.write(f"**Rua**: {item.rua}")
                st.write(f"**Complemento**: {item.complemento}")
                st.write(f"**Cidade**: {item.cidade}")
                st.write(f"**Estado**: {item.estado}")
                st.write(f"**Código Postal**: {item.codigo_postal}")
                st.write(f"**Estado Civil**: {item.estado_civil}")
                st.write(f"**Ministério**: {item.ministerio}")

                # EXCLUIR
                button_space_excluir = st.empty()
                on_click_excluir = button_space_excluir.button(
                    "Excluir", key=f"btnExcluir{item.id}_{index}")
                if on_click_excluir:
                    try:
                        MembrosControllers.excluir_membro(int(item.id))
                        st.rerun()  # Recarrega a página após exclusão
                    except ValueError as e:
                        st.error(f"Erro de valor: {e}")

                # EDITAR
                button_space_editar = st.empty()
                on_click_editar = button_space_editar.button(
                    "Editar", key=f"btnEditar{item.id}_{index}")

                if on_click_editar:
                    # Define o parâmetro de consulta
                    st.query_params["id"] = str(item.id)
                    st.rerun()  # Recarrega a página após definir o parâmetro

    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.query_params.clear()  # Limpa todos os parâmetros
            st.rerun()  # Recarrega a página

        PageCreate.create(paramId)


if __name__ == "__main__":
    query()
