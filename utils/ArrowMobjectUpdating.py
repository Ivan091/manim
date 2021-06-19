from abc import ABC

from manim import *


class ArrowMobjectUpdating(Arrow, ABC):
    def __init__(
            self,
            begin: Mobject,
            finish: Mobject,
            **kwargs
    ):
        super().__init__(begin, finish, **kwargs)
        self.add_updater(lambda x: update_arrow(x, begin, finish))


def update_arrow(arrow: Arrow, source: Mobject, destination: Mobject):
    arrow.set_start_and_end_attrs(source, destination)
    arrow.put_start_and_end_on(arrow.start, arrow.end)
    arrow.generate_points()
    arrow.tip.width = arrow.get_default_tip_length()
    arrow.reset_endpoints_based_on_tip(arrow.tip, False)
