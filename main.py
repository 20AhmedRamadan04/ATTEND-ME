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
            self.Names = ['Ibrahim Basem Gideon Escarus', 'Ibrahim Hassan Khalaf Mohammed', 'Ahmed Amir Salim Abdel Muttalib', 'Ahmed Amin Abdel Nabi Amin', 'Ahmed Ehab Hussein Saqr', 'Ahmed Thabet Ahmed Mustafa', 'Ahmed Zaki Jabr Al -Shafi’i', 'Ahmed Shawky Kamal Othman', 'Ahmed Sobh Mukhtar Ali Mahmoud', 'Ahmed Adel Sayed Mohammed Al -Wasimi', 'Ahmed Mohammed Hamad Ismail', 'Ahmed Mohammed Ramadan Al -Sayed', 'Ahmed Mohammed Abdel Qader Eid', 'Ahmed Mahmoud Khalil Abdel -Fattah', 'Ahmed Nasser Al -Din Ahmed Al -Issawi', 'Ahmed Hani Abu Hashem Abdo Awad', 'Ahmed Wael Mustafa Hassan', 'Ahmed Walid Abdel Ghaffar Abdel Wahab Al -Deeb', 'Adham Ramadan Shehata Ramadan', 'Isra Mohammed Maher Ali Ibrahim', 'Afram Osama Fathi Merid', 'Amal Magdy Mahmoud Metwally', 'A wish that Mohammed knows it', 'Amir Escarus Gideon Escarus', 'Aya Mohammed Abdul Jalil Abdo Al -Sudani', 'Ehab Ahmed Mohammed Hassan Ali Arafa', 'Jihad Samih Saeed Abu Fatima', 'John Sami George Salama', 'Hazem Mansour Misr Youssef', 'Hassan Mohammed Hassan Mohammed', 'Hamza Wael Mohammed Hassan', 'Ramzy Mohsen Ramzi Istiklal', 'Rana Saeed Al -Sayed Moselhi Badr', 'Rana Mohammed Farouk Abdel -Qader', 'Rowan Ahmed Mohammed Hassan', 'Rowan Khaled Hussein Amin Mohammed', 'Raymonda Ashraf Ishaq Awad', 'Ziad Al -Sayed Ibrahim Al -Desouki Mohammed Hassan', 'Ziad Rashad Hassan Rashad', 'Ziad Sayed Mohammed Ahmed Ali', 'Ziad Sharif Mohsen Hanafi', 'Zainab Mustafa Abdel Naeem Abbas', 'Saeed Amr Saeed Mahfouz Ahmed', 'Saif Al -Din Hatem Abdel -Wahab Mohammed', 'Saif Al -Din Salim Abdel -Azim Mohammed', 'Saif Al -Din Mohammed Sayed Hassan Faraj', 'Sherif Yousry Ibrahim Ali', 'Shams Ahmed Abdel Hamid Mohammed Musa', 'Shahd Abdel Moneim Mustafa Ahmed', 'Shahd Mohammed Mohammed Al - Sawy', 'Shahd Mohammed Mohammed Bakry', 'Adel Mahfouz Jawdah Moselhi', 'Abdul Rahman Ahmed Mohammed Salah Abdul Qadir', 'Abdul Rahman Anwar Mustafa Abdullah', 'Abdul Rahman Shaban Sultan Salem', 'Abdul Rahman Hindi, congratulations to him, Baz', 'Abdullah Mohammed Salah Shaban', 'Ammar Hamid Sayed', 'Omar Ahmed Faraj Abdul Shafi', 'Omar Amin Jaber Ibrahim', 'Omar Ehab Mohammed Fahmy', 'Omar Hani Saber Al -Saghir', 'Amr Bilal Al -Saeed Abdul Rahman Arab', 'Ghada Ahmed Prince Mahmoud Hamad Allah', 'Fatima Magdy Mahmoud Metwally', 'Karim Ashraf Issawi Abu Al -Fath', 'Cyril Ayyad Labib Iskandar', 'Martin Imad Maher Gerges', 'Mazen Hussein Munir Ahmed Al -Mashlawi', 'Mazen Khaled Badr Mohammed Hassan', 'Mohammed Ibrahim Abdel -Al Ibrahim', 'Mohammed Ahmed Saeed Mohammed Noir', 'Mohammed Ahmed Mohammed Abdel Aziz Abdel Halim', 'Mohammed Jamal Mohammed Ibrahim', 'Mohammed Khaled Hussein Mohammed Issa', 'Mohammed Reda Atef Hosni Ezzat', 'Mohammed Shaban Mohammed Mahrous', 'Mohammed Abdullah Youssef Abdullah', 'Mohammed Abdul Majeed Mohammed Saleh Karat', 'Mohammed Imad Ibrahim Basyouni Mohammed', 'Mohammed Omar Jawdah Sultan', 'Mohammed Amr Mohammed Kamel', 'Mohammed Haitham Mohammed Jamal Omar', 'Mohammed Waheed Faraj Allah Mahmoud Mohammed', 'Mahmoud Hussein Ali Abdul Hamid Al -Sawy', 'Mahmoud Khaled Mahmoud Tawfiq', 'Mahmoud Labib Mahmoud Ahmed Al -Sobky', 'Mahmoud Hisham Farraj Hashem', 'Marwan Hatem Ahmed Al -Burai', 'Marwa Ahmed Abdel Dayem Shehata', 'Maryam Sayed Ahmed Mahmoud', 'Maryam Mohammed Jalal Mohammed Awad', 'Mustafa Ibrahim Safwat Al -Rashash', 'Mustafa Abdel Nasser Mustafa Othman', 'Mustafa Amr Mustafa Kamal', 'Mustafa Nasser Anwar Salem', 'Mustafa Wageah Ali Al - Fallahah', 'Musab Mohammed Abdel -Ghani Ahmed', 'Malak Mohammed Abdel Hamed Mohammed', 'Mennatullah Tamer Mohammed Muslim Omar', 'Mirna Mustafa Ibrahim Mohammed', 'Mina Giorgios Ayoub Georgius', 'Nagy Abdel Jaber Nady Abdel Jaber', 'Nader Amir Abdel Halim Taha', 'Nora Mahmoud Abdel Hakim Morsi', 'Hajar Suleiman Hamdan Suleiman', 'Hajar Mahmoud Barakat Taghyan', 'Hadeer Samir Musa Mohammed', 'Here Hani Fathi Ali', 'Wafa Hashem Amin Mohammed', 'Yasmine Moawad Jamal Mohammed Al -Saeed', 'Youstina Samy Thabit Haroon', 'Youssef Ibrahim Shehat Mohammed', 'Youssef Salim Amer Salim', 'Youssef Abdel Jaber Nady Abdel Jaber', 'Youssef Imad Sayed Abdel Hamid Mabrouk', 'Youssef Omar Abdel Hamid Abdel -Gawad Zayed', 'Youssef Mohammed Hany Abdel Baset Al -Maghazi']
            self.Codes = [220318, 220319, 220320, 220321, 220322, 220323, 220324, 220325, 220326, 220327, 220328, 220329, 220330, 220331, 220332, 220333, 220334, 220335, 220336, 220337, 220338, 220339, 220340, 220341, 220342, 220343, 220344, 220345, 220346, 220347, 220348, 220349, 220350, 220351, 220352, 220353, 220354, 220355, 220356, 220357, 220358, 220359, 220360, 220361, 220362, 220363, 220364, 220365, 220366, 220367, 220368, 220369, 220370, 220371, 220372, 220373, 220374, 220375, 220376, 220377, 220378, 220379, 220380, 220381, 220382, 220383, 220384, 220385, 220386, 220387, 220388, 220389, 220390, 220391, 220392, 220393, 220394, 220395, 220396, 220397, 220398, 220399, 220400, 220401, 220402, 220403, 220404, 220405, 220406, 220407, 220408, 220409, 220410, 220411, 220412, 220413, 220414, 220415, 220416, 220417, 220418, 220419, 220420, 220421, 220422, 220423, 220424, 220425, 220426, 220427, 220428, 220429, 220430, 220431, 220432, 220433, 220434, 220435]
            self.Sections = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
            self.Year = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            
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
        
