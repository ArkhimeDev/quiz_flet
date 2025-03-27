import flet as ft
import json


def main(page: ft.Page):
    page.title = "Quiz"
    page.bgcolor = ft.Colors.WHITE

    numero_pregunta = ft.Text(value="1")
    puntuacion = ft.Text(value="0")

    # Funciones:

    def cargar_preguntas(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def comprobar(e):
        data = e.control.data
        nonlocal texto_resultado
        descripcion.value = preguntas[int(
            numero_pregunta.value)-1]["descripcion"]
        print(data)
        print(
            f"respuesta {preguntas[int(numero_pregunta.value)-1]["respuesta"]}")
        if data == preguntas[int(numero_pregunta.value)-1]["respuesta"]:
            print("CORRECTO")
            texto_resultado.value = "CORRECTO"
            texto_resultado.color = ft.Colors.GREEN_600
            puntuacion.value = str(int(puntuacion.value)+1)
            resultado(1)
        else:
            print("INCORRECTO")
            texto_resultado.value = "INCORRECTO"
            texto_resultado.color = ft.Colors.RED_600
            resultado(1)

    def aumentar_nivel():

        if int(numero_pregunta.value) < len(preguntas):
            numero_pregunta.value = str(int(numero_pregunta.value)+1)

            print(f"numero de pregunta: {numero_pregunta.value}")
        else:
            print(f"La puntuación obtenida es: {puntuacion} puntos")
        siguiente_pregunta()
        page.update()

    def siguiente_pregunta():
        cuestion.value = preguntas[int(numero_pregunta.value)-1]["pregunta"]
        opcion1.text = preguntas[int(numero_pregunta.value)-1]["opciones"][0]
        opcion1.data = preguntas[int(numero_pregunta.value)-1]["opciones"][0]
        opcion2.text = preguntas[int(numero_pregunta.value)-1]["opciones"][1]
        opcion2.data = preguntas[int(numero_pregunta.value)-1]["opciones"][1]
        opcion3.text = preguntas[int(numero_pregunta.value)-1]["opciones"][2]
        opcion3.data = preguntas[int(numero_pregunta.value)-1]["opciones"][2]
        opcion4.text = preguntas[int(numero_pregunta.value)-1]["opciones"][3]
        opcion4.data = preguntas[int(numero_pregunta.value)-1]["opciones"][3]

        page.update()

    def resultado(numero):
        nonlocal texto_resultado
        dialogo = ft.BottomSheet(
            on_dismiss=lambda _: aumentar_nivel(),
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.Container(
                            content=ft.Text(texto_resultado.value,
                                            color=texto_resultado.color,
                                            size=texto_resultado.size,
                                            weight=ft.FontWeight.BOLD
                                            ),
                            alignment=ft.alignment.center,
                            expand=False,
                        ),
                        ft.Container(
                            content=ft.Text(descripcion.value,
                                            color=ft.Colors.BLACK,
                                            size=20,
                                            ),
                            alignment=ft.alignment.center,
                            expand=False,
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Container(
                                    content=ft.Text(
                                        value="Siguiente pregunta", size=20, color=ft.Colors.WHITE),
                                ),
                                on_click=lambda _: page.close(dialogo),
                                bgcolor=ft.Colors.LIGHT_BLUE_900,

                            ),
                            alignment=ft.alignment.bottom_right,
                            expand=False,
                            margin=10
                        ),
                    ],
                ),
            ),
        )

        page.open(dialogo)

    preguntas = cargar_preguntas("preguntas.json")

    cuestion = ft.Text(
        value=preguntas[int(numero_pregunta.value)-1]["pregunta"], color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.W_800)

    opcion1 = ft.ElevatedButton(preguntas[int(numero_pregunta.value)-1]["opciones"][0],
                                on_click=comprobar,
                                data=preguntas[int(
                                    numero_pregunta.value)-1]["opciones"][0]
                                )
    opcion2 = ft.ElevatedButton(preguntas[int(numero_pregunta.value)-1]["opciones"][1],
                                on_click=comprobar,
                                data=preguntas[int(
                                    numero_pregunta.value)-1]["opciones"][1]
                                )
    opcion3 = ft.ElevatedButton(preguntas[int(numero_pregunta.value)-1]["opciones"][2],
                                on_click=comprobar,
                                data=preguntas[int(
                                    numero_pregunta.value)-1]["opciones"][2]
                                )
    opcion4 = ft.ElevatedButton(preguntas[int(numero_pregunta.value)-1]["opciones"][3],
                                on_click=comprobar,
                                data=preguntas[int(
                                    numero_pregunta.value)-1]["opciones"][3]
                                )
    texto_resultado = ft.Text(value="", size=30)

    descripcion = ft.Text(value="Aqui va la desrcipción de la respuesta")

    barra_estado = ft.Row(controls=[
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.QUESTION_ANSWER_OUTLINED),
                    ft.Container(
                        content=numero_pregunta
                    ),
                    ft.Text(value="/"),
                    ft.Container(
                        content=ft.Text(value=str(len(preguntas)))
                    ),
                ]
            ),
            margin=10
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.LIBRARY_ADD_CHECK_OUTLINED),
                    ft.Container(
                        content=puntuacion,
                        alignment=ft.alignment.center_right,
                        margin=10
                    )
                ]
            ),
            margin=10
        ),




    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    container = ft.Column(
        controls=[
            barra_estado,
            ft.Container(
                content=cuestion,
                alignment=ft.alignment.center,
                expand=True,
                margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_900,
                border_radius=10,
                padding=20,

            ),
            ft.Container(
                content=opcion1,
                alignment=ft.alignment.center,
                expand=True,
                margin=10
            ),
            ft.Container(
                content=opcion2,
                alignment=ft.alignment.center,
                expand=True,
                margin=10
            ),
            ft.Container(
                content=opcion3,
                alignment=ft.alignment.center,
                expand=True,
                margin=10
            ),
            ft.Container(
                content=opcion4,
                alignment=ft.alignment.center,
                expand=True,
                margin=10
            ),
        ]
    )

    page.add(container)


ft.app(target=main)
