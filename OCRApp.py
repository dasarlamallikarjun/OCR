import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup        
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from OCR_API import OCR_API
from OCR_TES import OCR_TES

from OCR3 import OCR3
Window.clearcolor = (77/255,176/255,147/255, 0)
kivy.require("1.10.1")



class MyPopup(Popup):
    def selected(self, instance):
        try:
            app.start_page.ids.txtbx.text=instance[0]
            app.start_page.ids.img.source=instance[0]
        except:pass

class StartPage(FloatLayout):
    
    def pressed_button(self, instance):
        if self.ids.img.source!='':
            app.screen_manager.current='next'
            if instance.text=='Online': 
                a=OCR_API() 
            else:
                a=OCR_TES()
            #a=OCR3() 
            app.text=a.result(self.ids.img.source,instance.text)
            app.next_page.ids.output.text=app.text
        else:
            content = BoxLayout(orientation='vertical', spacing=5) 
            background_color= (77/255,176/255,147/255, 0)
            self.popup = popup = Popup(title='Warning',content=content, size_hint=(.7, .5))
            content.add_widget(Label(text='Selct the Image',font_size=20))
            self.btn=Button(text='Close',size_hint_y=.5)
            self.btn.bind(on_release=popup.dismiss)
            content.add_widget(self.btn)
            self.popup.open()
            
        
    def browse_button(self, instance):
        MyPopup().open()
        
    def selected(self, instance):
        self.ids.img.source=instance[0]
class NextPage(FloatLayout):
    def close(self,instance):
        try:
            inf = open('{}.txt'.format(self.txt.text.replace(" ","_")),'w') 
            inf.write(self.ids.output.text)
            inf.close()
        except:
           content = BoxLayout(orientation='vertical', spacing=5)
           popup = Popup(title='save',content=content, size_hint=(.7, .5))
           content.add_widget(Label(text='Text is not Clear to save',font_size=20)) 
           self.btn=Button(text='Close',size_hint_y=.1)
           self.btn.bind(on_release=popup.dismiss)
           content.add_widget(self.btn)
           popup.open()
        self.popup.dismiss()
    def pressed_button(self, instance):
        app.screen_manager.current='start' 
    def selected1(self,instance):
        content = BoxLayout(orientation='vertical', spacing=5)
        self.popup = popup = Popup(title='save',content=content, size_hint=(.7, .5))
        content.add_widget(Label(text='Filename(without extension)')) 
        self.txt=TextInput(multiline=False) 
        content.add_widget(self.txt)
        self.btn=Button(text='Close')
        self.btn.bind(on_release=self.close)
        content.add_widget(self.btn)
        self.popup.open()
        
         

class OCR(App):
    def build(self):
        self.icon="Images/icon-2.png"
        Window.bind(on_dropfile=self._on_file_drop)
        self.text=""
        self.start_page = StartPage()
        self.screen_manager = ScreenManager()
        self.next_page = NextPage()
        screen1 = Screen(name='start')
        screen2 = Screen(name='next')
        screen1.add_widget(self.start_page)
        screen2.add_widget(self.next_page)
        self.screen_manager.add_widget(screen1)
        self.screen_manager.add_widget(screen2)
        return self.screen_manager
    def _on_file_drop(self, window, file_path):
        self.start_page.ids.img.source='%s'%file_path 
        self.start_page.ids.txtbx.text='%s'%file_path
if __name__ == "__main__":
    app = OCR()
    app.run()
    
