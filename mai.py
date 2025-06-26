from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Hello!')
        button = Button(text='Click me')

        button.bind(on_press=self.on_button_press)

        self.layout.add_widget(self.label)
        self.layout.add_widget(button)

        return self.layout

    def on_button_press(self, instance):
        
            button2 = Button(text="Hi!")
            button2.bind(on_press=self.onSecondButton)
            self.layout.add_widget(button2)
            
            self.label.text = 'Next'

    def onSecondButton(self, instance):
        self.label.text = "second"

if __name__ == '__main__':
    MyApp().run()