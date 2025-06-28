# Kivyライブラリから必要なコンポーネントをインポートします
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
# Web上の画像を非同期で読み込むためにAsyncImageウィジェットをインポート
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

# --- GitHubリポジトリの設定 ---
# あなたのGitHubユーザー名とリポジトリ名に書き換えてください
GITHUB_USERNAME = "Keita062"  # 例: "kivy"
GITHUB_REPOSITORY = "pre-app" # 例: "kivy"
# ブランチ名を指定します。通常は 'main' または 'master' です。
BRANCH_NAME = "main"

# 画像が保存されているフォルダのパス (リポジトリのルートからのパス)
IMAGE_FOLDER_PATH = "Images" # 元のコードの 'Images' フォルダを想定

# ベースURLを構築
BASE_IMAGE_URL = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPOSITORY}/{BRANCH_NAME}/{IMAGE_FOLDER_PATH}"

# 画像の定義
Loading_image_png = "Loading image.png"
Search_begins_png = "Search begins.png"
Searching_png = "Searching.png"
lost_glasses_png = "lost glasses.png"
# --- ここまで設定 ---


# アプリケーションの背景色を設定
Window.clearcolor = (0.95, 0.95, 0.95, 1)

# --- ベースとなる画面クラス ---
# 遷移メソッドを共通化してコードの重複を減らします
class BaseScreen(Screen):
    def switch_screen(self, screen_name, direction):
        """指定された画面に遷移する共通メソッド"""
        self.manager.transition.direction = direction
        self.manager.current = screen_name

# --- 1つ目の画面（メニュー画面）の定義 ---
class FirstScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title_label = Label(text='Firist Screan', font_size='24sp', size_hint_y=None, height=50, color=(0,0,0,1))

        # AsyncImageを使用してGitHubから画像を読み込みます
        # 注意: ファイル名にスペースが含まれていると問題が発生する可能性があります。
        app_image = AsyncImage(
            source=f"{BASE_IMAGE_URL}/{Loading_image_png}", # URLエンコードのためスペースを%20に変換
            allow_stretch=True,
            keep_ratio=True,
            # 画像が読み込めなかった場合に表示する画像
            nocache=True # デバッグ中はキャッシュを無効にすると便利
        )

        next_button = Button(text='next', font_size='20sp', size_hint_y=None, height=60)
        next_button.bind(on_press=lambda instance: self.switch_screen('second', 'left'))
        
        layout.add_widget(title_label)
        layout.add_widget(app_image)
        layout.add_widget(next_button)
        self.add_widget(layout)

# --- 2つ目の画面の定義 ---
class SecondScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title_label = Label(text='Second screan', font_size='24sp', size_hint_y=None, height=50, color=(0,0,0,1))
        
        app_image = AsyncImage(
            source=f"{BASE_IMAGE_URL}/{Search_begins_png}",
            allow_stretch=True,
            keep_ratio=True,
            nocache=True
        )

        nav_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=60)
        back_button = Button(text='back', font_size='20sp')
        back_button.bind(on_press=lambda instance: self.switch_screen('first', 'right'))
        next_button = Button(text=next, font_size='20sp')
        next_button.bind(on_press=lambda instance: self.switch_screen('third', 'left'))
        nav_layout.add_widget(back_button)
        nav_layout.add_widget(next_button)

        layout.add_widget(title_label)
        layout.add_widget(app_image)
        layout.add_widget(nav_layout)
        self.add_widget(layout)

# --- 3つ目の画面の定義 ---
class ThirdScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title_label = Label(text='Third Screan', font_size='24sp', size_hint_y=None, height=50, color=(0,0,0,1))
        
        app_image = AsyncImage(
            source=f"{BASE_IMAGE_URL}/{Searching_png}",
            allow_stretch=True,
            keep_ratio=True,
            nocache=True
        )
        
        nav_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=60)
        back_button = Button(text='back', font_size='20sp')
        back_button.bind(on_press=lambda instance: self.switch_screen('second', 'right'))
        next_button = Button(text='next', font_size='20sp')
        next_button.bind(on_press=lambda instance: self.switch_screen('fourth', 'left'))
        nav_layout.add_widget(back_button)
        nav_layout.add_widget(next_button)

        layout.add_widget(title_label)
        layout.add_widget(app_image)
        layout.add_widget(nav_layout)
        self.add_widget(layout)

# --- 4つ目の画面の定義 ---
class FourthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title_label = Label(text='Forth Screan', font_size='24sp', size_hint_y=None, height=50, color=(0,0,0,1))
        
        app_image = AsyncImage(
            source=f"{BASE_IMAGE_URL}/{lost_glasses_png}",
            allow_stretch=True,
            keep_ratio=True,
            nocache=True
        )

        nav_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=60)
        back_button = Button(text='back', font_size='20sp')
        back_button.bind(on_press=lambda instance: self.switch_screen('third', 'right'))
        menu_button = Button(text='Return to top', font_size='20sp')
        menu_button.bind(on_press=lambda instance: self.switch_screen('first', 'right'))
        nav_layout.add_widget(back_button)
        nav_layout.add_widget(menu_button)

        layout.add_widget(title_label)
        layout.add_widget(app_image)
        layout.add_widget(nav_layout)
        self.add_widget(layout)

# --- アプリケーション本体の定義 ---
class ScreenApp(App):
    def build(self):
        sm = ScreenManager()
        sm.transition = FadeTransition()
        
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        
        return sm

# --- アプリケーションの実行 ---
if __name__ == '__main__':
    ScreenApp().run()
