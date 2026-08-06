from kivy.core.window import Window
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.button import Button





class gameApp(App):
	
	
	def build(self):
		la = Button(text="hello" ,
		 size_hint=(0.3,0.1),
		pos_hint={"center_x":0.3,"center_y":0.2}
		,font_size=(100),on_press=self.hello)
		
		
		car = Button(text="click me")
		return la
		
		
		
		
	def hello(self,btn):
		btn.color=(1,0,0,1)
		btn.italic=True
		btn.size_hint=(0.5,0.5)
		
		
		
gameApp().run()