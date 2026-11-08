import flet as ft

def main(page: ft.Page):
    page.title = "Buygram"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    app_bar = ft.AppBar(
        title=ft.Text("Buygram", weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_900,
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ],
    )

    messages_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    input_field = ft.TextField(
        hint_text="Сообщение...",
        expand=True,
        border_radius=20,
        content_padding=10
    )

    def send_message(e):
        if input_field.value.strip():
            messages_list.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(input_field.value, color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.BLUE_600,
                            padding=10,
                            border_radius=12,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )
            val = input_field.value
            input_field.value = ""
            page.update()

            messages_list.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(f"Buygram Bot: Принято «{val}»", color=ft.Colors.WHITE),
                            bgcolor=ft.Colors.GREY_800,
                            padding=10,
                            border_radius=12,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
            page.update()

    send_btn = ft.IconButton(
        icon=ft.Icons.SEND,
        icon_color=ft.Colors.BLUE_400,
        on_click=send_message
    )

    messages_list.controls.append(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Добро пожаловать в Buygram!", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREY_800,
                    padding=10,
                    border_radius=12,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )

    page.add(
        app_bar,
        messages_list,
        ft.Container(
            content=ft.Row([input_field, send_btn]),
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_900
        )
    )

ft.app(main)
