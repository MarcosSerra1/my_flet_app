import flet as ft

def create_banner(page: ft.Page) -> ft.Banner:
    def close_banner(e):
        page.close(banner)

    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)

    banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text(
            value='Por favor, preencha o campo de texto',
            color=ft.Colors.BLACK
        ),
        actions=[
            ft.TextButton(text='Fechar', style=action_button_style, on_click=close_banner)
        ],
        open=False
    )
    
    return banner
