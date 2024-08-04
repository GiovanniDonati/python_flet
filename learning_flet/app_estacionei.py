import flet as ft
from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    # page.window_maximized = True
    page.window_height = 750
    page.window_width = 450

    first_page_contents = Container(
        bgcolor='red',
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            bgcolor='white',
                            content=Icon(icons.MENU)
                        ),
                        Container(
                            # Adicionar ícone de perfil
                        )
                    ]
                )
            ]
        )
    )

    card = Row(
        controls=[
            Container(
                margin=margin.only(
                    top=100, left=15
                ),
                width=120,
                height=90,
                bgcolor='white',
                border_radius=15,
            ),
            Container(
                margin=margin.only(
                    top=100, left=0
                    ),
                width=120,
                height=90,
                bgcolor='white',
                border_radius=15,
            )
        ]
    )
    controlPanel = Container(
        Row(
            controls=[
                Container(
                    margin=margin.only(
                        top=100, left=15
                    ),
                    width=120,
                    height=90,
                    bgcolor='white',
                    border_radius=15,
                ),
                Container(
                    margin=margin.only(
                        top=100, left=0
                        ),
                    width=120,
                    height=90,
                    bgcolor='white',
                    border_radius=15,
                )
            ]
        )
    )

    menu = Row(
        controls=[
            Container(
                width=280,
                height=650,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
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
        width=350,
        height=650,
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
