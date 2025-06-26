# Kivyライブラリから必要なコンポーネントをインポートします
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
# 画像を表示するためにImageウィジェットをインポート
from kivy.uix.image import Image

# --- 1つ目の画面（メニュー画面）の定義 ---
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        # 画面のレイアウトを定義（今回は縦にウィジェットを並べるBoxLayout）
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # 画面タイトル用のラベル
        title_label = Label(text='1st scean', font_size='24sp', size_hint_y=None, height=50)

        # --- 画像の追加 ---
        # Imageウィジェットを作成します。
        # sourceプロパティに画像のパスを指定します。
        # この例では 'kivy_logo.png' というファイル名を指定しています。
        # この画像ファイルは、Pythonスクリプトと同じディレクトリに配置してください。
        # URLを指定することも可能です。例: 'https://kivy.org/logos/kivy-logo-black-64.png'
        # allow_stretch=True にすると、ウィジェットのサイズに合わせて画像が伸縮します。
        # keep_ratio=False にすると、アスペクト比を維持しなくなります。
        app_image = Image(
            source=r'C:\Users\sk062\Downloads\2025-05-28_220755.png', 
            allow_stretch=True,
            keep_ratio=True
        )

        # 二つ目の画面に遷移するためのボタン
        settings_button = Button(text='next scean', font_size='20sp', size_hint_y=None, height=60)
        settings_button.bind(on_press=self.go_to_settings)
        
        # レイアウトにウィジェットを追加
        layout.add_widget(title_label)
        layout.add_widget(app_image) # レイアウトに画像ウィジェットを追加
        layout.add_widget(settings_button)
        
        # 画面にレイアウトを追加
        self.add_widget(layout)

    def go_to_settings(self, instance):
        """
        設定画面に遷移する関数
        """
        self.manager.current = 'settings'
        # 画面遷移時のエフェクトも指定できます
        self.manager.transition.direction = 'left'

# --- 2つ目の画面（設定画面）の定義 ---
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
        # こちらも同様にBoxLayoutでレイアウトを定義
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # 画面タイトル用のラベル
        title_label = Label(text='setting', font_size='24sp', size_hint_y=None, height=50)
        
        # メニュー画面に戻るためのボタン
        menu_button = Button(text='back menu', font_size='20sp')
        # ボタンが押されたときに呼ばれる関数をバインド
        menu_button.bind(on_press=self.go_to_menu)
        
        # レイアウトにウィジェットを追加
        layout.add_widget(title_label)
        layout.add_widget(menu_button)
        
        # 画面にレイアウトを追加
        self.add_widget(layout)

    def go_to_menu(self, instance):
        """
        メニュー画面に遷移する関数
        """
        self.manager.current = 'menu'


# --- アプリケーション本体の定義 ---
class ScreenApp(App):
    def build(self):
        # スクリーンマネージャーのインスタンスを作成
        # これが画面遷移を管理します
        sm = ScreenManager()
        
        # 作成した画面クラスのインスタンスをスクリーンマネージャーに追加
        # name='...' で指定した名前が、遷移先を指定する際に使われます
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        
        # スクリーンマネージャーをアプリのルートウィジェットとして返す
        return sm

# --- アプリケーションの実行 ---
if __name__ == '__main__':
    ScreenApp().run()
