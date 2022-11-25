import customtkinter
import main
from main import *
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        def GetStartTick(self):
            return self.startTick_Entry.get()
        
        def GetEndTick(self):
            return self.endTick_Entry.get()

        def GetTimeFrame(self):
            return self.timeFrame_dropdown.get()
        self.title("Financial CSV Automation")
        self.geometry("450x350")
        self.resizable(0,0)
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        self.frame1 = customtkinter.CTkFrame(width = 400, height=700, border_color='#000000')
        self.frame1.pack(side=TOP, padx = 25, pady = 10)

        ###############frame1########################

        self.createTickerFiles_button = customtkinter.CTkButton(
                master = self.frame1,
                text="Create full ticker list",
                
                text_font="none 10",
                text_color="white",
                
                width=150,
                height=30,
                command = lambda: [main.CreateDependency()])

        self.createTickerFiles_button.place(x = 125, y = 270)

        self.createTickerFiles_label = customtkinter.CTkLabel(
                master = self.frame1,
                text="Detailed excel file ouputs",
                text_font="none 15")

        self.createTickerFiles_label.place(x = 90, y = 30)

        self.startEnd_label1 = customtkinter.CTkLabel(
                master = self.frame1,
                text="Start:End (ex: [AAPL] to [AMZN])",
                text_font="none 10")

        self.startEnd_label1.place(x = 105, y = 60)

        
        self.startEnd_label1 = customtkinter.CTkLabel(
                master = self.frame1,
                text="Detailed tickers timeframe:",
                text_font="none 12")

        self.startEnd_label1.place(x = 35, y = 160)

        self.startTick_Entry = customtkinter.CTkEntry(
                    master = self.frame1,
                    placeholder_text="Starting ticker",
                    placeholder_text_color="#cccccc",
                    
                    text_font="none 10",
                    text_color="white",
                    
                    width=150,
                    height=40,
                    border_width=2,
                    border_color= "#d3d3d3",
                    bg_color="#262626",
                    fg_color= "#262626",
                    
                    corner_radius=5)

        self.startTick_Entry.place(x=35, y= 100)

        self.endTick_Entry = customtkinter.CTkEntry(
            master = self.frame1,
            placeholder_text="Ending ticker",
            placeholder_text_color="#cccccc",
            
            text_font="none 10",
            text_color="white",
            
            width=150,
            height=40,
            border_width=2,
            border_color= "#d3d3d3",
            bg_color="#262626",
            fg_color= "#262626",
            
            corner_radius=5)

        self.endTick_Entry.place(x=210, y= 100)

        self.generateDetailed_button = customtkinter.CTkButton(
                master = self.frame1,
                text="Create detailed ticker files",
                
                text_font="none 10",
                text_color="white",
                
                width=150,
                height=30,
                command = lambda: [main.TickerInput(GetStartTick(self), GetEndTick(self), GetTimeFrame(self))])

        self.generateDetailed_button.place(x = 220, y = 220)

        self.generate_button = customtkinter.CTkButton(
        master = self.frame1,
        text="Create detailed financials report",
        
        text_font="none 10",
        text_color="white",
        
        width=150,
        height=30,
        command = lambda: [main.GetAllFinancials(GetStartTick(self), GetEndTick(self))])

        self.generate_button.place(x = 10, y = 220)

        self.timeFrame_dropdown = customtkinter.CTkOptionMenu(master=self.frame1,
                                       values=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"])
        
        self.timeFrame_dropdown.place(x = 230, y = 160)

if __name__ == "__main__":
    app = App()
    app.mainloop()