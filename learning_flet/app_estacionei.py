import flet as ft
from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    first_page_contents = Container(
        bgcolor='red',
        content=Column(
             controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            bgcolor='white',
                            content=Icon(
                                icons.MENU)),
                        Container(
                            #Adicionar icone de perfil
                            )
                        ]
                    )
                ]
            )
        )

    controlPanel = Container(

    )
    menu = Row(
        controls=[
            Container(
                width=280,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50,left=20,
                    right=20,bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )


    principal = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                menu,
                controlPanel,
            ]
        )
    )
    page.add(principal)

app(target=main)