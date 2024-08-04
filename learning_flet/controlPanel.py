import flet as ft

def main(page: ft.Page ):
    page.title = "Controle de Estacionamento"
    BG = ''
    FWG = ''
    FG = ''
    PINK = ''

    lista_produtos = ft.ListView()
    
    def adicionar(e):
        lista_produtos.controls.append(ft.Text(f"Código: {codigo.value}, Quantidade: {quantidade.value}"))
        page.update()

    txt_codigo = ft.Text('Código do item:')
    codigo = ft.TextField(label='Digite o código', text_align=ft.TextAlign.LEFT)
    txt_quantidade = ft.Text('Quantidade do item:')
    quantidade = ft.TextField(label='Digite a quantidade', text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Adicionar', on_click=adicionar)


    page.add(
        txt_codigo,
        codigo,
        txt_quantidade,
        quantidade,
        btn_produto,
        lista_produtos,
    )


ft.app(target=main)