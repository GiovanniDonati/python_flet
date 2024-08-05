import flet as ft
from flet import *

class MainContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            content=Column(
                spacing=10,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Estacionei",
                        size=20,
                        weight="w400",
                        color="white54",
                    ),
                    Text(
                        "Controle de vagas",
                        size=30,
                        weight="bold",
                    ),
                ],
            ),
        )

class DropDownContainer(UserControl):
    def __init__(
        self,
        initials: str,
        name: str,
        gen: str,
        title: str,
        description: str,
        salary: str,
    ):
        self.initials = initials
        self.name = name
        self.gen = gen
        self.title = title
        self.description = description
        self.salary = salary
        super().__init__()

    def ExpandContainer(self, e):
        if self.controls[0].height != 180:
            self.controls[0].height = 180
            self.controls[0].update()
        else:
            self.controls[0].height = 90
            self.controls[0].update()

    def TopContainer(self):
        return Container(
            width=450,
            height=90,
            content=Column(
                spacing=0,
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=40,
                                height=40,
                                bgcolor="white24",
                                border_radius=40,
                                alignment=alignment.center,
                                content=Text(
                                    self.initials,
                                    size=15,
                                    weight="bold",
                                ),
                            ),
                            VerticalDivider(width=2),
                            Container(
                                content=Column(
                                    spacing=1,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(self.name, size=11),
                                        Text(self.gen, size=9, color="white54"),
                                    ],
                                )
                            ),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Container(
                                content=IconButton(
                                    icon=icons.ARROW_DROP_DOWN_CIRCLE_ROUNDED,
                                    icon_size=20,
                                    on_click=lambda e: self.ExpandContainer(e),
                                )
                            )
                        ],
                    ),
                ],
            ),
        )

    def GetEmployeeData(self):
        items = [
            ["Descrição", self.title],
            ["Lote", self.description],
            ["Data adicionado", self.salary],
        ]
        l = []

        for item in items:
            l.append(
                Row(
                    controls=[
                        Column(
                            expand=1,
                            horizontal_alignment=CrossAxisAlignment.START,
                            controls=[
                                Text(
                                    item[0],
                                    size=9,
                                    weight="bold",
                                ),
                            ],
                        ),
                        Column(
                            expand=2,
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[
                                Text(
                                    item[1],
                                    size=9,
                                    weight="bold",
                                    color="white54",
                                ),
                            ],
                        ),
                    ]
                )
            )
        return l

    def BottomContainer(self):
        title, description, salary = self.GetEmployeeData()
        return Container(
            width=450,
            height=80,
            content=Column(
                spacing=12,
                controls=[
                    title,
                    description,
                    salary,
                ],
            ),
        )

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            width=450,
            height=90,
            bgcolor="white10",
            border_radius=11,
            animate=animation.Animation(400, "decelerate"),
            padding=padding.only(left=10, right=10, top=10),
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.TopContainer(),
                    self.BottomContainer(),
                ],
            ),
        )

def main(page: Page):
    page.title = "Estacionei"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = True

    principal_container = Container(
        alignment=ft.alignment.center,
        bgcolor="black",
        border_radius=40,
        padding=20,
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll="auto",
            controls=[
                Divider(height=20, color="transparent"),
                MainContainer(),
                Divider(height=30, color="white24"),
                Text("Todas as vagas", size=15),
                DropDownContainer(
                    "Vaga",
                    "Dono",
                    "Veiculo",
                    "Data entrada",
                    "Tipo de vaga",
                    "Valor Hora",
                ),
                DropDownContainer(
                    "Vaga",
                    "Dono",
                    "Veiculo",
                    "Data entrada",
                    "Tipo de vaga",
                    "Valor Hora",
                ),
                DropDownContainer(
                    "Vaga",
                    "Dono",
                    "Veiculo",
                    "Data entrada",
                    "Tipo de vaga",
                    "Valor Hora",
                ),
                DropDownContainer(
                    "Vaga",
                    "Dono",
                    "Veiculo",
                    "Data entrada",
                    "Tipo de vaga",
                    "Valor Hora",
                ),
                DropDownContainer(
                    "Vaga",
                    "Dono",
                    "Veiculo",
                    "Data entrada",
                    "Tipo de vaga",
                    "Valor Hora",
                ),
            ],
        ),
    )
    page.add(principal_container)
    page.update()
    pass

if __name__ == "__main__":
    ft.app(target=main)
