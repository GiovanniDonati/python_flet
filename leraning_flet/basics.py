import flet as ft

def main(page: ft.Page):
    page.title = "Desvendando o flet"
    # page.padding = 0
    # page.window_width = 400
    # page.window_height = 400

    # c1 = ft.Container(
    #     content = ft.ElevatedButton("Botão Elevado"),
    #     bgcolor = "#f67893",
    #     padding = 10,
    # )

    # c2 = ft.Container(
    #     content = ft.ElevatedButton("Botão Elevado"),
    #     bgcolor = "#f67893",
    #     padding = 10,
    # )

    # lista = [c1,c2]

    # row1 = ft.Row(spacing=5, controls = lista)
    # row2 = ft.Row(spacing=5, controls = lista)
    
    # column1 = ft.Column(spacing=5, controls= lista)

    # st = ft.Stack(
    #     [
    #         ft.Image(
    #             src=f"",
    #             width=150,
    #             height=150
    #         ),
    #         ft.ElevatedButton("Botão 1"),

    #     ],

    #     width=300,
    #     height=300
    # )

    # lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    # lv.controls.append(ft.Text("Texto 1"))
    # lv.controls.append(ft.Text("Texto 2"))

    # gv = ft.GridView(
    #     expand=1, runs_count=5, max_extent=150, child_aspect_ratio=1.0, spacing=5, run_spacing=5,
    # )

    # gv.controls.append(ft.Text("Texto 1"))
    # gv.controls.append(ft.Text("Texto 2"))

    # rr = ft.ResponsiveRow([
    #     ft.Column(col={"sm":6}, controls=[ft.Text("Coluna 1")]),
    #     ft.Column(col={"sm":6}, controls=[ft.Text("Coluna 2")])
    # ])

    # pw = ft.Text(bottom=50, right=50, style="displaysmall")
    # page.overlay.append(pw)


    # cartao = ft.Card(
    # content=ft.Container(
    #     content=ft.Column([
    #         ft.ListTile(
    #             # leading=ft.Icon(ft.Icons.ALBUM)
    #             title=ft.Text("Título do cartão"),
    #             subtitle=ft.Text("Subtítulo do Cartão"),
    #         ),
    #         ft.Row(
    #             [
    #                 ft.TextButton("Cancelar"),
    #                 ft.TextButton("Confirmar"),
    #             ],
    #             alignment=ft.MainAxisAlignment.END,
    #         ),
    #     ]),
    #     width=200,
    #     padding=10,
    # ),
    # )
    
    page.add()
ft.app(target=main)