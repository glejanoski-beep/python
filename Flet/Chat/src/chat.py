from dataclasses import dataclass

import flet as ft



@dataclass
class Message:
    user: str
    text: str
    message_type: str

def main(pagina: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(mensagem: Message):
        if mensagem.message_type == 'chat_message':
            chat.controls.append(ft.Text(f'{mensagem.user}: {mensagem.text}'))
        elif mensagem.message_type == 'login_message':
            chat.controls.append(ft.Text(mensagem.text, italic=True, color=ft.Colors.BLACK_45, size=12))
        pagina.update()

    pagina.pubsub.subscribe(on_message)

    def send_click(e):
        pagina.pubsub.send_all(Message(user=pagina.session.store.get('user_name'), text=new_message.value, message_type='chat_message'))
        new_message.value = ""

    user_name = ft.TextField(label='Digite o seu nome')

    def join_click(e):
        if not user_name.value:
            user_name.error = 'Informe o nome, caba...'
        else:
            pagina.session.store.set('user_name', user_name.value)
            pagina.pop_dialog()
            pagina.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f'{user_name.value} entrou no chat.',
                    message_type='login_message',
                )
            )

    pagina.show_dialog(
        ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Bem Vindo!"),
            content=ft.Column([user_name], tight=True),
            actions=[ft.Button(content='Entrar no chat', on_click=join_click)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
    )

    pagina.add(
        chat,
        ft.Row(controls=[new_message, ft.Button("Enviar", on_click=send_click)]),
    )


ft.run(main)