import flet as ft
import json


def main(page: ft.Page):
    page.title = "Quiz"
    page.bgcolor = ft.Colors.WHITE

    numero_pregunta = 0
    puntuacion = 0

    # Funciones:

    def cargar_preguntas(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def comprobar(e):
        data = e.control.data
        nonlocal texto_resultado
        nonlocal puntuacion
        descripcion.value = preguntas[numero_pregunta]["descripcion"]
        print(data)
        print(f"respuesta {preguntas[numero_pregunta]["respuesta"]}")
        if data == preguntas[numero_pregunta]["respuesta"]:
            print("CORRECTO")
            texto_resultado.value = "CORRECTO"
            texto_resultado.color = ft.Colors.GREEN_600
            puntuacion += 1
            resultado(1)
        else:
            print("INCORRECTO")
            texto_resultado.value = "INCORRECTO"
            texto_resultado.color = ft.Colors.RED_600
            resultado(1)

    def aumentar_nivel():
        nonlocal numero_pregunta
        if numero_pregunta < len(preguntas)-1:
            numero_pregunta += 1
        else:
            print(f"La puntuación obtenida es: {puntuacion} puntos")
        siguiente_pregunta()

    def siguiente_pregunta():
        cuestion.value = preguntas[numero_pregunta]["pregunta"]
        opcion1.text = preguntas[numero_pregunta]["opciones"][0]
        opcion1.data = preguntas[numero_pregunta]["opciones"][0]
        opcion2.text = preguntas[numero_pregunta]["opciones"][1]
        opcion2.data = preguntas[numero_pregunta]["opciones"][1]
        opcion3.text = preguntas[numero_pregunta]["opciones"][2]
        opcion3.data = preguntas[numero_pregunta]["opciones"][2]
        opcion4.text = preguntas[numero_pregunta]["opciones"][3]
        opcion4.data = preguntas[numero_pregunta]["opciones"][3]

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
        value=preguntas[numero_pregunta]["pregunta"], color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.W_800)

    opcion1 = ft.ElevatedButton(preguntas[numero_pregunta]["opciones"][0],
                                on_click=comprobar,
                                data=preguntas[numero_pregunta]["opciones"][0]
                                )
    opcion2 = ft.ElevatedButton(preguntas[numero_pregunta]["opciones"][1],
                                on_click=comprobar,
                                data=preguntas[numero_pregunta]["opciones"][1]
                                )
    opcion3 = ft.ElevatedButton(preguntas[numero_pregunta]["opciones"][2],
                                on_click=comprobar,
                                data=preguntas[numero_pregunta]["opciones"][2]
                                )
    opcion4 = ft.ElevatedButton(preguntas[numero_pregunta]["opciones"][3],
                                on_click=comprobar,
                                data=preguntas[numero_pregunta]["opciones"][3]
                                )
    texto_resultado = ft.Text(value="", size=30)

    descripcion = ft.Text(value="Aqui va la desrcipción de la respuesta")

    container = ft.Column(
        controls=[
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
