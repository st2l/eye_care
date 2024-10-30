import flet as ft
from apscheduler.schedulers.background import BackgroundScheduler
from win10toast import ToastNotifier

scheduler = BackgroundScheduler()

def notify():
    ToastNotifier().show_toast(
        title="EYES NEED REST U, BASTARD!",
        msg="Do the eyes exercises right now. Please >:3. U know the rules = 2 mins of rest and we are done",
        duration=120,
        threaded=True
    )

def main(page: ft.Page):

    def on_approve_btn_clicked(e):
        try:
            scheduler.shutdown()
        except Exception as e:
            pass
        scheduler.remove_all_jobs()  # clear all jobs
        scheduler.add_job(notify, trigger='interval', minutes=int(txt_number.value))
        scheduler.start()

    page.title = "Eye care"
    page.vertical_aligment = ft.MainAxisAlignment.CENTER

    h2_txt = ft.Text(
        value="Eye care!",
        size=24,
        font_family='JetBrainsMono Nerd Font',
        color=ft.colors.RED_200
    )
    mini_txt = ft.Text(
        value="Get your eyes healthy pls :3",
        size=16,
        font_family='JetBrainsMono Nerd Font',
        color=ft.colors.RED_300
    )
    help_text = ft.Text(
        value="Insert the amount of the minutes between notifications",
        size=14,
        font_family='JetBrainsMono Nerd Font',
        color=ft.colors.GREEN_300
    )
    txt_number = ft.TextField(
        value='120',
        text_align='right',
        width=100
    )
    approve_btn = ft.ElevatedButton(
        text='Update the sheduler',
        icon=ft.icons.ADD,
        icon_color=ft.colors.GREEN_300,
        color=ft.colors.GREEN_100
    )
    approve_btn.on_click = on_approve_btn_clicked

    page.add(
        ft.Row(
            [
                h2_txt
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )
    page.add(
        ft.Row(
            [
                mini_txt
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )
    page.add(
        ft.Row(
            [
                help_text
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )
    page.add(
        ft.Row(
            [
                txt_number, approve_btn
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )
 

if __name__ == "__main__":
    ft.app(main)
    scheduler.add_job(
        notify,
        trigger='interval',
        minutes=120
    )
    scheduler.start()