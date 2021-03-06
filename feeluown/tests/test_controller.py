# -*- coding:utf8 -*-
import asyncio
from quamash import QEventLoop
from PyQt5.QtWidgets import QApplication

import feeluown
from feeluown.glue import Glue


def test_controller_start():
    import sys
    app = QApplication(sys.argv)
    feeluown.config.load()
    app_event_loop = QEventLoop(app)
    asyncio.set_event_loop(app_event_loop)
    w = Glue()
    w.show()
