import flet as ft

class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0


def main(pagina: ft.Page):
    def drag(evento: ft.DragUpdateEvent):
        evento.control.top = max(0, evento.control.top + evento.local_delta.y)
        evento.control.left = max(0, evento.control.left + evento.local_delta.x)
        evento.control.update()

    def start_drag(evento: ft.DragStartEvent):
        move_on_top(evento.control, controls)
        solitaire.start_top = evento.control.top
        solitaire.start_left = evento.control.left
        evento.control.update()

    def bounce_back(game, card):
        card.top = game.start_top
        card.left = game.start_left
        pagina.update()
        
    def drop(evento: ft.DragEndEvent):
        if abs(evento.control.top - slot.top) < 50 and abs(evento.control.left - slot.left) < 50:
            place(evento.control, slot)
        else:
            bounce_back(solitaire, evento.control)
            
        evento.control.update()

    def place(card, slot):
        '''  Colocar o card no slot '''
        card.top = slot.top
        card.left = slot.left
        pagina.update()

    def move_on_top(card, controls):
          controls.remove(card)
          controls.append(card)
          pagina.update()

    
    slot = ft.Container(
        width=70,
        height=100,
        left=200,
        top=0,
        border=ft.Border.all(1),       
    )

    card1 = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=5,
            on_pan_start=start_drag,
            on_pan_update=drag,
            on_pan_end=drop,
            left=0,
            top=0,
            content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
    )

    card2 = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=5,
            on_pan_start=start_drag,
            on_pan_update=drag,
            on_pan_end=drop,
            left=100,
            top=0,
            content=ft.Container(bgcolor=ft.Colors.YELLOW, width=70, height=100),
    )

    solitaire = Solitaire()

    controls = [slot, card1, card2]
    pagina.add(ft.Stack(controls= controls, width=1000, height=500))   


ft.run(main)