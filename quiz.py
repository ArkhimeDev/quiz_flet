import flet as ft
import json
import random


def main(page: ft.Page):
    page.title = "Quiz"
    page.bgcolor = ft.Colors.WHITE

    # Funciones:
    def mostrar_resultado():
        page.controls.clear()
        page.add(container_resultado)

    def seleccion_pregunta(e):
        data = e.control.data
        mostrar_preguntas(data)

    def reinicio(e):
        mostrar_inicio()

    def mostrar_preguntas(archivo):
        page.controls.clear()
        nonlocal preguntas
        nonlocal total_preguntas
        nonlocal contador_preguntas
        nonlocal preguntas_aleatorias
        nonlocal contador_preguntas
        contador_preguntas = 0
        preguntas = cargar_preguntas(archivo)
        total_preguntas.value = str(len(preguntas))
        preguntas_aleatorias = random.sample(
            range(int(total_preguntas.value)), 10)
        print(preguntas_aleatorias)
        total_preguntas.value = str(len(preguntas_aleatorias))
        puntuacion.value = "0"
        numero_pregunta.value = "1"
        cuestion.value = preguntas[preguntas_aleatorias[contador_preguntas]]["pregunta"]
        opcion1.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][0]
        opcion1.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][0]
        opcion2.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][1]
        opcion2.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][1]
        opcion3.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][2]
        opcion3.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][2]
        opcion4.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][3]
        opcion4.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][3]

        page.add(container_preguntas)

    def mostrar_inicio():
        page.controls.clear()
        page.add(container_inicio)

    def cargar_preguntas(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def comprobar(e):
        data = e.control.data
        nonlocal texto_resultado
        descripcion.value = preguntas[preguntas_aleatorias[contador_preguntas]]["descripcion"]

        if data == preguntas[preguntas_aleatorias[contador_preguntas]]["respuesta"]:
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
        nonlocal contador_preguntas
        if contador_preguntas < len(preguntas_aleatorias)-1:
            contador_preguntas += 1
            numero_pregunta.value = str(int(numero_pregunta.value)+1)
            siguiente_pregunta()
            page.update()
        else:
            mostrar_resultado()

    def siguiente_pregunta():
        cuestion.value = preguntas[preguntas_aleatorias[contador_preguntas]]["pregunta"]
        opcion1.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][0]
        opcion1.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][0]
        opcion2.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][1]
        opcion2.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][1]
        opcion3.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][2]
        opcion3.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][2]
        opcion4.text = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][3]
        opcion4.data = preguntas[preguntas_aleatorias[contador_preguntas]]["opciones"][3]

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

    # preguntas = cargar_preguntas("preguntas.json")

    numero_pregunta = ft.Text(
        value="1", color=ft.Colors.PINK_600, size=20, weight=ft.FontWeight.BOLD)
    puntuacion = ft.Text(value="0", color=ft.Colors.GREEN_600,
                         size=20, weight=ft.FontWeight.BOLD)
    preguntas = ""
    preguntas_aleatorias = ""
    contador_preguntas = 0

    cuestion = ft.Text(
        value="", color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.W_800)
    opcion1 = ft.ElevatedButton(on_click=comprobar)
    opcion2 = ft.ElevatedButton(on_click=comprobar)
    opcion3 = ft.ElevatedButton(on_click=comprobar)
    opcion4 = ft.ElevatedButton(on_click=comprobar)
    descripcion = ft.Text(value="")
    texto_resultado = ft.Text(value="", size=30)
    total_preguntas = ft.Text(color=ft.Colors.PINK_600,
                              size=20, weight=ft.FontWeight.BOLD)

    barra_estado = ft.Row(controls=[
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.QUESTION_ANSWER_OUTLINED,
                            color=ft.Colors.PINK_600),
                    ft.Container(
                        content=numero_pregunta
                    ),
                    ft.Text(value="/", color=ft.Colors.PINK_600,
                            size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=total_preguntas
                    )
                ]
            ),
            margin=10
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.LIBRARY_ADD_CHECK_OUTLINED,
                            color=ft.Colors.GREEN_600),
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

    container_inicio = ft.Column(
        controls=[
            ft.Container(
                content=ft.Image(src="assets/images/quiz_quest.png",
                                 width=200, height=200),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.Text(value="Selecciona temática",
                                size=30, color=ft.Colors.LIGHT_BLUE_900),
                alignment=ft.alignment.center
            ),
            ft.Divider(),
            ft.Container(
                content=ft.ElevatedButton(
                    "Cultura general", on_click=seleccion_pregunta, data="cult_gen.json", icon=ft.Icons.EMOJI_OBJECTS_OUTLINED, icon_color=ft.Colors.PINK_600, color=ft.Colors.PINK_600),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.ElevatedButton(
                    "Futbol", on_click=seleccion_pregunta, data="futbol.json", icon=ft.Icons.SPORTS_SOCCER, icon_color=ft.Colors.PINK_600, color=ft.Colors.PINK_600),
                alignment=ft.alignment.center
            )

        ]
    )

    container_preguntas = ft.Column(
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

    container_resultado = ft.Column(
        controls=[
            ft.Container(
                content=ft.Image(
                    src="assets/images/felicidades.png", width=400, height=400),
                alignment=ft.alignment.top_center,
            ),
            ft.Container(
                content=puntuacion,
                alignment=ft.alignment.top_center
            ),
            ft.Container(
                content=ft.ElevatedButton(
                    "Inicio", on_click=reinicio, icon=ft.Icons.HOME, icon_color=ft.Colors.PINK_600, color=ft.Colors.PINK_600),
                alignment=ft.alignment.center,
                padding=30
            )

        ],
        width=float("inf"),
        alignment=ft.alignment.center

    )

    mostrar_inicio()


ft.app(target=main)
