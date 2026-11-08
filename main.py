import flet as ft

def main(page: ft.Page):
    page.title = "Buygram"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#121212" # Темный стиль мессенджера

    # Поле ввода номера
    phone_input = ft.TextField(
        label="Номер телефона",
        prefix_text="+",
        keyboard_type=ft.KeyboardType.PHONE,
        width=300,
        border_radius=10
    )

    # Кнопка продолжить
    def button_clicked(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Введен номер: {phone_input.value}"))
        page.snack_bar.open = True
        page.update()

    next_button = ft.ElevatedButton(
        text="Далее",
        on_click=button_clicked,
        width=300
    )

    # Добавляем элементы на экран
    page.add(
        ft.Column(
            [
                ft.Text("Добро пожаловать в Buygram", size=24, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("Введите ваш номер телефона для входа", size=14, color="grey"),
                ft.Container(height=20),
                phone_input,
                ft.Container(height=10),
                next_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
