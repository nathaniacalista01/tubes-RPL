"""BudgetWise's navigation bar"""
from typing import Any, Callable, Optional, List

from flet_core import (
    UserControl,
    Ref,
    Image,
    Text,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors,
    GestureDetector,
    MouseCursor,
    FontWeight,
    ControlEvent,
    Column,
)


class NavbarItem(UserControl):
    """Navbar Item component"""

    def __init__(self, img_src: str, text: str, on_item_selected: Any = None, **kwargs):
        super().__init__(**kwargs)
        self.img_src = img_src
        self.text = text
        self.image_ref = Ref[Image]()
        self.text_ref = Ref[Text]()
        self.on_item_selected = on_item_selected

    def build(self):
        return Row(
            alignment=MainAxisAlignment.START,
            vertical_alignment=CrossAxisAlignment.START,
            spacing=20,
            controls=[
                Image(
                    ref=self.image_ref,
                    src=self.img_src,
                    color="white"
                    if self.data == 0
                    else colors.with_opacity(0.4, "white"),
                ),
                GestureDetector(
                    mouse_cursor=MouseCursor.CLICK,
                    on_tap_down=self.on_item_selected,
                    data=self.data,
                    content=Text(
                        ref=self.text_ref,
                        value=self.text,
                        font_family="Istok Web",
                        size=20,
                        weight=FontWeight.W_700,
                        color="white"
                        if self.data == 0
                        else colors.with_opacity(0.4, "white"),
                    ),
                ),
            ],
        )


class Navbar(UserControl):
    """BudgetWise Navigation Bar"""

    def __init__(
        self,
        on_item_selected: Callable[[int], Any],
        items: Optional[List[NavbarItem]] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.selected_index = 0
        self.items = [] if items is None else items
        self.item_refs: List[Ref[NavbarItem]] = [
            Ref[NavbarItem]() for _ in range(len(self.items))
        ]
        self.on_item_selected = on_item_selected

    def item_selected(self, evt: ControlEvent):
        """Event handler on navbar item selected"""
        item = self.item_refs[self.selected_index].current
        item.image_ref.current.color = colors.with_opacity(0.4, "white")
        item.text_ref.current.color = colors.with_opacity(0.4, "white")
        item.update()
        self.selected_index = evt.control.data
        item = self.item_refs[self.selected_index].current
        item.image_ref.current.color = "white"
        item.text_ref.current.color = "white"
        item.update()
        self.on_item_selected(self.selected_index)

    def build(self):
        return Column(
            alignment=MainAxisAlignment.START,
            spacing=15,
            controls=[
                NavbarItem(
                    ref=self.item_refs[i],
                    data=i,
                    img_src=x.img_src,
                    text=x.text,
                    on_item_selected=self.item_selected,
                )
                for i, x in enumerate(self.items)
            ],
        )
