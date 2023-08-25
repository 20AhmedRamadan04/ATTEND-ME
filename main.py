import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy import platform
import pandas as pd

class ATT_1(GridLayout) :
    def __init__(self, **kwargs):
        super(ATT_1 , self).__init__()
        
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        
        if platform == "android" :
            from android.permissions import Permission, request_permissions 
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
            
        self.cols = 1
        self.add_widget(Label(text = "---------- MITU AI DEPARTMENT ATTENDANCE ----------" , color = "white" , bold = True , font_size = 30))
        self.add_widget(Label(text = "Full Name: "))
        self.Full_Name = TextInput()
        self.add_widget(self.Full_Name)

        self.add_widget(Label(text = "Student Code: "))
        self.Student_Code = TextInput()
        self.add_widget(self.Student_Code)

        self.add_widget(Label(text = "Student Section: "))
        self.Student_Section = TextInput()
        self.add_widget(self.Student_Section)

        self.add_widget(Label(text = "Study Year: "))
        self.Study_Year = TextInput()
        self.add_widget(self.Study_Year)

        self.Full_Name.background_color = "white"
        self.Full_Name.foreground_color = "black"

        self.Student_Code.background_color = "white"
        self.Student_Code.foreground_color = "black"

        self.Student_Section.background_color = "white"
        self.Student_Section.foreground_color = "black"

        self.Study_Year.background_color = "white"
        self.Study_Year.foreground_color = "black"

        self.Submit_ = Button(text = "_Submit_" , color = "green" , bold = True , font_size = 30)
        try:
            self.Submit_.bind(on_press = self.Submit)
            self.add_widget(self.Submit_)
        except Exception as e:
            self.add_widget(Label(text = f"Error >> {str(e)}" , color = "green" , bold = True , font_size = 25))

    def Submit(self , instance) :
        try :
            Data = pd.read_csv("https://raw.githubusercontent.com/20AhmedRamadan04/Pro/main/AI-(2).csv")
            Data = Data.dropna()
            self.add_widget(Label(text = f"[+] Success Read Dataset " , color = "green" , bold = True , font_size = 25))
            self.Names = list(Data.iloc[:,0].values)
            self.Codes = list(Data.iloc[:,1].values)
            self.Sections = list(Data.iloc[:,2].values)
            self.Year = list(Data.iloc[:,3].values)

            if str(self.Full_Name.text) in str(self.Names) and str(self.Student_Code.text) in str(self.Codes) and str(self.Student_Section.text) in str(self.Sections) and str(self.Study_Year.text) in str(self.Year) :
                if len(self.Full_Name.text) in range(12 , 54) and len(self.Student_Code.text) == 6 and len(self.Student_Section.text) == 1 and len(self.Study_Year.text) == 1 :
                   self.file = open("Attendance.txt" , "a") 
                   self.file.write(f"\nFull Name: {self.Full_Name.text}\nStudent Code: {self.Student_Code.text}\nSection: {self.Student_Section.text}\nYear: {self.Study_Year.text}\n")
                   self.add_widget(Label(text = "---------- Your Attendance Has Been Successfully Registered :) ----------\nThank You !" , color = "green" , bold = True , font_size = 25))
                else :
                    self.add_widget(Label(text = "This Data Does'nt Exist, Please Try Again !" , color = "red" , bold = True , font_size = 25)) 
            else:
                self.add_widget(Label(text = "Failed, Please Try Again !" , color = "red" , bold = True , font_size = 25)) 

        except Exception as e:
            self.add_widget(Label(text = f"Error >> {str(e)}" , color = "red" , bold = True , font_size = 25))


class ATT_2(App) :

    def build(self):
        Window.clearcolor = (0.5 , 0 , 0 , 1)
        return ATT_1()

if __name__ == "__main__" :
    ATT_2().run()
        
