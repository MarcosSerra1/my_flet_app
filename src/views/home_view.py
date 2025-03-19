import flet as ft
from controllers.search_controller import get_woman_info
from .banner import create_banner

def home_view(page: ft.Page):
    # Configurações iniciais da janela
    page.title = "Desafio #05"
    page.window.width = 480
    page.window.height = 750
    page.scroll = 'adaptive'

    # AppBar para um cabeçalho elegante
    appbar = ft.AppBar(
        title=ft.Text("Desafio #05", color=ft.Colors.WHITE, size=24, weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.BLUE_GREY_900,
    )
    page.appbar = appbar

    # Criar o banner de alerta
    banner = create_banner(page)

    # Cabeçalho principal da tela
    header_text = ft.Text(
        "Mulheres que Fizeram História na Computação",
        color=ft.Colors.WHITE,
        size=18,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Campo de entrada com estilo moderno
    name_field = ft.TextField(
        label="Digite uma frase",
        hint_text="Ex.: Ada Lovelace",
        border_color=ft.Colors.WHITE24,
        cursor_color=ft.Colors.WHITE,
        color=ft.Colors.WHITE,
        filled=True,
        fill_color=ft.Colors.BLUE_GREY_700,
        border_radius=ft.border_radius.all(10),
        width=320
    )

    # Componente para exibir o resultado
    result = ft.Text(
        "Preencha o campo acima para ver o resultado.",
        color=ft.Colors.GREEN_300,
        size=16,
        text_align=ft.TextAlign.LEFT,
        selectable=True,  # Permite selecionar o texto
        weight=ft.FontWeight.W_400,
    )

    # Função de callback do botão de busca
    def search(e):
        if not name_field.value:
            page.open(banner)
            return

        info = get_woman_info(name_field.value)
        result.value = info
        result.update()
        name_field.value = ""
        name_field.focus()
        name_field.update()

    # Botão de busca com ícone e tooltip
    search_button = ft.IconButton(
        icon=ft.Icons.SEARCH,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE,
        on_click=search,
        tooltip="Pesquisar"
    )

    # Linha que agrupa o campo de busca e o botão
    search_row = ft.Row(
        [
            name_field,
            search_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Cartão para o cabeçalho
    card1 = ft.Container(
        content=ft.Column(
            [header_text],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        margin=10,
        width=450,
        border_radius=ft.border_radius.all(15),
        bgcolor=ft.Colors.BLUE_GREY_800,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color=ft.Colors.BLACK45,
            spread_radius=1,
            offset=ft.Offset(0, 5)
        )
    )

    # Cartão para o campo de busca
    card2 = ft.Container(
        content=search_row,
        padding=20,
        margin=10,
        width=450,
        border_radius=ft.border_radius.all(15),
        bgcolor=ft.Colors.BLUE_GREY_700,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color=ft.Colors.BLACK45,
            spread_radius=1,
            offset=ft.Offset(0, 5)
        )
    )

    # Cartão para exibir o resultado
    card3 = ft.Container(
        content=ft.Column(
            [result],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.START
        ),
        padding=20,
        margin=10,
        width=450,
        border_radius=ft.border_radius.all(15),
        bgcolor=ft.Colors.BLUE_GREY_900,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color=ft.Colors.BLACK45,
            spread_radius=1,
            offset=ft.Offset(0, 5)
        )
    )

    # Criar o footer
    footer_text = ft.Text(
        "Desenvolvido com 💙 por Marcos Serra\n" +
        "Desafio proposto por PyPro\n" +
        "© 2025 - Todos os direitos reservados",
        color=ft.Colors.WHITE70,
        size=12,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_300,
    )

    footer = ft.Container(
        content=ft.Column(
            [
                ft.Divider(color=ft.Colors.WHITE24, height=1),
                footer_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        padding=ft.padding.only(top=20, bottom=20),
        margin=ft.margin.only(top=10),
        width=450,
    )

    # Adiciona os componentes na página
    page.add(card1, card2, card3, footer)
