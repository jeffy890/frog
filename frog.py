'''
    written by jeffy890
    2024.02.14

    visualizing pandas data
'''

from datetime import datetime
import pandas as pd
import pyxel

class App:
    def __init__(self):
        self.width = 240
        self.height = 180 + 20
        self.fps = 30
        self.app_title = "frog"
        pyxel.init(
            self.width, 
            self.height, 
            title=self.app_title, 
            display_scale=2, 
            fps=self.fps
        )


        pyxel.colors[6] = 0x66DCE9
        pyxel.colors[7] = 0xFFFFFF
        pyxel.colors[15] = 0xE03B90

        pd.set_option("display.max_columns", 5)
        pd.set_option("display.max_rows", 10)
        self.filename = "./temp.csv"
        self.data = pd.read_csv(self.filename)
        self.data_describe = self.data.describe()
        self.update_count = 0
        self.update_time = datetime.now().time()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count % (self.fps*10) == 0:
            self.data = pd.read_csv(self.filename)
            self.data_describe = self.data.describe()
            self.update_count += 1
            self.update_time = datetime.now().time()

    def draw(self):
        pyxel.cls(7)

        # file info
        pyxel.text(10, 10, "checking ", 2)
        pyxel.text(50, 10, self.filename, 2)

        pyxel.text(10, 22, "csv content", 2)
        pyxel.rectb(10, 30, 220, 140, 2)

        pyxel.text(167, 10, "last update time", 2)
        pyxel.text(170, 22, str(self.update_time), 2)

        pyxel.text(15, 35, str(self.data), 2)
        #pyxel.text(15, 135, str(self.data.dtypes), 2)

        #pyxel.text(15, 135, str(self.data.columns), 2)

        pyxel.text(160, 35, str(self.data_describe), 2)
        self.draw_color()

    

    def draw_color(self):
        distance = 14
        for i in range(16):
            pyxel.rect(10+i*distance, 185, 10, 10, i)
            #pyxel.text(23+i*distance, 185, str(i), i)

App()