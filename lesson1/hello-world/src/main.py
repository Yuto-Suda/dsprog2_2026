import flet as ft


def main(page: ft.Page):

    # Hello World
    hello_world = ft.Text("Hello World", size=50)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    def decrement_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data -= 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.Row([
        ft.FloatingActionButton(
            icon=ft.Icons.REMOVE, key="decrement", on_click=decrement_click
            ),
        ft.FloatingActionButton(
            icon=ft.Icons.ADD, key="increment", on_click=increment_click
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=10,
        tight=True,
    )

    page.add(
        # 実行環境に表示エリアを合わせるためのオブジェクト
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                # content=counter,
                content=ft.Column(
                    controls=[hello_world, counter],
                    alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
