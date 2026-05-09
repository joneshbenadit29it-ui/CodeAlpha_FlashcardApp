import flet as ft

def main(page: ft.Page):
    page.title = "CodeAlpha Flashcard Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # List of cards (The 'Data' part)
    flashcards = [
        {"question": "What is Python?", "answer": "A popular programming language."},
        {"question": "What is IoT?", "answer": "Internet of Things."}
    ]

    state = {"index": 0}

    # UI Components
    card_text = ft.Text(flashcards[0]["question"], size=22, weight="bold", text_align=ft.TextAlign.CENTER)
    info_label = ft.Text(f"Card 1 of {len(flashcards)}", color="grey")
    
    # Input fields for adding new cards
    new_q = ft.TextField(label="New Question", width=200)
    new_a = ft.TextField(label="New Answer", width=200)

    # 1. NAVIGATION LOGIC
    def update_ui():
        if len(flashcards) > 0:
            card_text.value = flashcards[state["index"]]["question"]
            card_text.color = "black"
            info_label.value = f"Card {state['index'] + 1} of {len(flashcards)}"
        else:
            card_text.value = "No cards left!"
            info_label.value = "0 of 0"
        page.update()

    def show_answer(e):
        if flashcards:
            card_text.value = flashcards[state["index"]]["answer"]
            card_text.color = "blue"
            page.update()

    def next_card(e):
        if flashcards:
            state["index"] = (state["index"] + 1) % len(flashcards)
            update_ui()

    # 2. CUSTOMIZATION LOGIC (Add/Delete)
    def add_card(e):
        if new_q.value and new_a.value:
            flashcards.append({"question": new_q.value, "answer": new_a.value})
            new_q.value = ""
            new_a.value = ""
            update_ui()

    def delete_card(e):
        if flashcards:
            flashcards.pop(state["index"])
            state["index"] = 0 if len(flashcards) > 0 else 0
            update_ui()

    # LAYOUT
    page.add(
        ft.Column([
            info_label,
            ft.Container(
                content=card_text,
                padding=40,
                bgcolor="#F0F0F0",
                border_radius=10,
                width=350,
                height=150,
            ),
            ft.Row([
                ft.ElevatedButton("Previous", on_click=lambda _: next_card(-1)), # Simplified for stability
                ft.ElevatedButton("Show Answer", on_click=show_answer, bgcolor="blue", color="white"),
                ft.ElevatedButton("Next", on_click=next_card),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            ft.Text("Manage Cards", weight="bold"),
            ft.Row([new_q, new_a]),
            ft.Row([
                ft.ElevatedButton("Add Card", on_click=add_card, color="green"),
                ft.ElevatedButton("Delete Current", on_click=delete_card, color="red"),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)