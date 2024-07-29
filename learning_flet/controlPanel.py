import flet as ft

def main(page: ft.Page ):
    page.title = "Capacidade e Demanda"

    def pesquisar(e):
        pass

    txt_codigo = ft.Text('Código do item:')
    codigo = ft.TextField(label='Digite o código', text_align=ft.TextAlign.LEFT)
    txt_quantidade = ft.Text('Quantidade do item:')
    quantidade = ft.TextField(label='Digite a quantidade', text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Calcular', on_click=pesquisar)

    page.add(
        txt_codigo,
        codigo,
        txt_quantidade,
        quantidade,
        btn_produto
    )

ft.app(target=main)