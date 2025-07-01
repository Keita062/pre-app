# kivyをインポートする
import kivy

# kivyのバージョン指定
kivy.require('2.2.0')

# Kivyライブラリから必要なコンポーネントをインポートします
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# windowsizeを指定する
# 一般的なスマホの縦長比率(9:16)に合わせて設定しています。
Window.size = (405 , 720)

# 背景色の色の定義
# RGBA
Window.clearcolor = (0.15, 0.15, 0.15, 1)

# レイアウトの設定
Layout_setting = "vertical" # レイアウトを垂直に並べる

# アプリケーションの状態変数
transition = ["Loding", "Search begins", "Search", "lostglasses"]

# fontsizeの定義
font_size_1st = "40sp"

# メインの画面となるレイアウトを定義するクラスです。
# BoxLayoutを継承しており、ウィジェット（部品）を縦か横に並べることができます。
class MainScrean( BoxLayout ):
    def __init__( self , **kwargs ):
        super( MainScrean , self ).__init__( **kwargs )
        self.orientation = Layout_setting

        self.screen_index = 0
        self.screen_text = transition

        self.main_label = Label(
            text = self.screen_texts[self.screen_index],
            font_size = font_size_1st
        )
        self.next_botton = Button(
            
        )

        # ボタンが押されたときに呼び出す関数（メソッド）を紐付けます。
        self.next_button.bind(on_press=self.go_to_next_screen)

