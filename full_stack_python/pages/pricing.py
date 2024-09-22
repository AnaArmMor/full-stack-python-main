import reflex as rx 

from ..ui.base import base_page

#icono de check azul al lado de la palabra herramientas de la card

def feature_item(feature: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "check", color=rx.color("blue", 9), size=21
        ),
        rx.text(feature, size="4", weight="regular"),
    )

#declaracion de funciones de cada card

def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("Herramientas:"),
        feature_item(" 7-Zip;Advanced IP Scanner;AES Crypt	;Autopsy	;BIA (Business Impact Analysis)	;CCleaner	;CPU-Z	;CrystalDiskInfo	;ISO	;ISO 27001 e ISO 27002	;MAGERIT	;Metasploitable	;Nmap	;PILAR Basic	;PowerShell	;RockYou.txt	;SQLite	;SuperScan	;Sysinternals	VirtualBox	;Visual Studio Code (VS Code)	;Visual Trace Route"),
        spacing="3",
        width="25%",
        align_items="start",
    )
def pricing_card_popular() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Modulo",
                    trim="both",
                    as_="s",
                    size="2",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "MF0486",
                    trim="both",
                    size="5",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
           
            align_items="center",
            justify="between",
            height="35px",
            width="100%",
        ),
        rx.text(
            "Seguridad en equipos informaticos.",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        popular_features(),
        rx.spacer(),
        rx.button(
            "Click aqui",
            size="3",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("red", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )
def normal_features() -> rx.Component:
    return rx.vstack(
        feature_item("Herramientas:"),
        feature_item("ARP Spoof (o ARP Poisoning);Brave Browser:	;Burp Suite:	;Greenbone OpenVAS:	;HTTrack:	;Man in the Middle (MITM):	;Metasploit:	;MongoDB:	;Nessus:	;PHP:	;Robo 3T:	;Studio 3T:	;OpenVAS (Open Vulnerability Assessment System):	;Pentesting (Pruebas de penetración):	;Python:	;TLS (Transport Layer Security);Wireshark;XAMPP	;Zphisher:	"),
        spacing="3",
        width="25%",
        align_items="start",
    )
def pricing_card_normal() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Modulo",
                    trim="both",
                    as_="s",
                    size="2",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "MF0487",
                    trim="both",
                    size="5",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "Auditoria de seguridad informática.",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        normal_features(),
        rx.spacer(),
        rx.button(
            "Click aqui",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("green", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )
def critical_features() -> rx.Component:
    return rx.vstack(
        feature_item("Herramientas:"),
        feature_item("Backdoor;Getmac;JSON (JavaScript Object Notation);Jupyter;Keylogger;Matplotlib;NumPy;Pandas;Python;PyWin32;Snort;Socket;Wine	"),
        spacing="3",
        width="25%",
        align_items="start",
    )
def pricing_card_critical() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Modulo",
                    trim="both",
                    as_="s",
                    size="2",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "MF0488",
                    trim="both",
                    size="5",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "gestion de incidentes de seguridad informática.",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        critical_features(),
        rx.spacer(),
        rx.button(
            "Click aqui",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )
def standard_features() -> rx.Component:
    return rx.vstack(
        feature_item("Herramientas:"),
        feature_item("Incluir contenido AQUI al finalizar el modulo"),
        spacing="3",
        width="25%",
        align_items="start",
    )
def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Modulo",
                    trim="both",
                    as_="s",
                    size="2",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "MF0489",
                    trim="both",
                    size="5",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "Sistemas seguros de acceso y transmision de datos",
            weight="bold",
            size="7",
            
            text_align="left",
        ),
        standard_features(),
        rx.spacer(),
        rx.button(
           "Click aqui",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        sspacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("yellow", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )

def real_features() -> rx.Component:
    return rx.vstack(
        feature_item("Herramientas:"),
        feature_item("Incluir contenido AQUI al finalizar el modulo"),
        spacing="3",
        width="25%",
        align_items="start",
    )
def pricing_card_real() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Modulo",
                    trim="both",
                    as_="s",
                    size="2",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "MF0490",
                    trim="both",
                    size="5",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "Gestion de servicios en el sistema informatico",
            weight="bold",
            size="7",
            
            text_align="left",
        ),
        real_features(),
        rx.spacer(),
        rx.button(
            "Click aqui",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        sspacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("pink", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )
def pricing_cards() -> rx.Component:
    return rx.flex(
        pricing_card_popular(),
        pricing_card_normal(),
        pricing_card_critical(),
        pricing_card_standard(),
        pricing_card_real(),
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="center",
    )

def pricing_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contenido/Modulos", size="9"),
            pricing_cards(),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)