import tkinter as tk
from tkinter import ttk
from tkinter import * 
import tkinter.messagebox
import random

times = 1 # To check the number of times you use help
# Health & Score
change_health = 2 # Check the number of country change
health_value = 5 # User's health value
score = 100 # User's score
score_plus = 0 # To calculate the user's extra points as gifts

def watchers(): # Checks the player's status
    # Create the messages
    if health_value == 0:
        root.destroy()  # If the user's health = 0, the game is over
        tkinter.messagebox.showinfo("watchers", "You lost :(\nYour score in this game is 0 out of 100")
    elif health_value > 0:  # If the user's health != 0, but the answer is wrong
        tkinter.messagebox.showinfo("watchers", "Your answer is wrong!!!")
    else:  # If an unexpected error occurs
        tkinter.messagebox.showinfo("watchers", "خطایی پیش آمده \nمجدداً امتحان نمایید")
        

def countrys_list():  # Read the "CountryNames.txt" and add copy it to a list
    try:
        with open('./CountryNames.txt') as file:
            country_list = file.readlines()
            country_list = [item.rstrip() for item in country_list]
        return(country_list)
    except:   # /!\ If the names of countries are not uploaded from the external file, use this section. /!\
        country_list = [
			'Afghanistan',
			'Albania',
			'Algeria',
			'Andorra',
			'Angola',
			'Argentina',
			'Armenia',
			'Australia',
			'Austria',
			'Azerbaijan',
			'Bahamas',
			'Bahrain',
			'Bangladesh',
			'Barbados',
			'Belarus',
			'Belgium',
			'Belize',
			'Benin',
			'Bhutan',
			'Bolivia',
			'Bosnia Herzegovina',
			'Botswana',
			'Brazil',
			'Brunei',
			'Bulgaria',
			'Burkina',
			'Burundi',
			'Cambodia',
			'Cameroon',
			'Canada',
			'Cape Verde',
			'Central African Rep',
			'Chad',
			'Chile',
			'China',
			'Colombia',
			'Comoros',
			'Congo',
			'Costa Rica',
			'Croatia',
			'Cuba',
			'Cyprus',
			'Czech Republic',
			'Denmark',
			'Djibouti',
			'Dominica',
			'Dominican Republic',
			'East Timor',
			'Ecuador',
			'Egypt',
			'El Salvador',
			'Equatorial Guinea',
			'Eritrea',
			'Estonia',
			'Ethiopia',
			'Fiji',
			'Finland',
			'France',
			'Gabon',
			'Gambia',
			'Georgia',
			'Germany',
			'Ghana',
			'Greece',
			'Grenada',
			'Guatemala',
			'Guinea',
			'Guyana',
			'Haiti',
			'Honduras',
			'Hungary',
			'Iceland',
			'India',
			'Indonesia',
			'Iran',
			'Iraq',
			'Ireland',
			'Israel',
			'Italy',
			'Ivory Coast',
			'Jamaica',
			'Japan',
			'Jordan',
			'Kazakhstan',
			'Kenya',
			'Kiribati',
			'North Korea',
			'South Korea',
			'Kosovo',
			'Kuwait',
			'Kyrgyzstan',
			'Laos',
			'Latvia',
			'Lebanon',
			'Lesotho',
			'Liberia',
			'Libya',
			'Liechtenstein',
			'Lithuania',
			'Luxembourg',
			'Macedonia',
			'Madagascar',
			'Malawi',
			'Malaysia',
			'Maldives',
			'Mali',
			'Malta',
			'Marshall Islands',
			'Mauritania',
			'Mauritius',
			'Mexico',
			'Micronesia',
			'Moldova',
			'Monaco',
			'Mongolia',
			'Montenegro',
			'Morocco',
			'Mozambique',
			'Myanmar',
			'Namibia',
			'Nauru',
			'Nepal',
			'Netherlands',
			'New Zealand',
			'Nicaragua',
			'Niger',
			'Nigeria',
			'Norway',
			'Oman',
			'Pakistan',
			'Palau',
			'Panama',
			'Papua New Guinea',
			'Paraguay',
			'Peru',
			'Philippines',
			'Poland',
			'Portugal',
			'Qatar',
			'Romania',
			'Russian Federation',
			'Rwanda',
			'St Kitts & Nevis',
			'St Lucia',
			'Samoa',
			'San Marino',
			'Sao Tome & Principe',
			'Saudi Arabia',
			'Senegal',
			'Serbia',
			'Seychelles',
			'Sierra Leone',
			'Singapore',
			'Slovakia',
			'Slovenia',
			'Solomon Islands',
			'Somalia',
			'South Africa',
			'South Sudan',
			'Spain',
			'Sri Lanka',
			'Sudan',
			'Suriname',
			'Swaziland',
			'Sweden',
			'Switzerland',
			'Syria',
			'Taiwan',
			'Tajikistan',
			'Tanzania',
			'Thailand',
			'Togo',
			'Tonga',
			'Trinidad & Tobago',
			'Tunisia',
			'Turkey',
			'Turkmenistan',
			'Tuvalu',
			'Uganda',
			'Ukraine',
			'United Arab Emirates',
			'United Kingdom',
			'United States',
			'Uruguay',
			'Uzbekistan',
			'Vanuatu',
			'Vatican City',
			'Venezuela',
			'Vietnam',
			'Yemen',
			'Zambia',
			'Zimbabwe'
		]
		
def choosing_random_country():  # Select a country randomly
    country = random.choice(countrys_list())
    return(country)

country = choosing_random_country()   # Put the selected name in a variable to use elsewhere

def hide_country_letter(c):  # To hide some parts of the country_name
    _len = len(c)
    if _len == 4:
        N_country = c[0] + "-" + c[2] + "-"
    elif _len == 5:
        N_country = c[0] + "--" + c[3:]
    elif _len <= 9:
        N_country = c[0] + "---" + c[4:]
    elif _len <= 17:
        N_country = "--" + c[2:4] + "-" + c[5:7] + "-" + c[8:]
    elif _len <= 20:
        N_country = c[0] + "--" + c[3] + "-" + c[5:7] + "--" + c[9:12] + "----"+ c[16:]
    return(N_country)
    
n_country = hide_country_letter(country)  # Put the hidden name in a variable to use elsewhere  
        
# Change the country randomly
def country_change():
    global change_health, country, score, times
    score -= 5  # score-=5 for each name change
    country_change_health.config(text = ". " * change_health)   # Show the number of times you are allowed to change the name to the use
    if change_health >= 0:  # If the user's opportunities to change the name are not finished, it can change the name of the country
        times = 1   # To allow the user to use help for the new name
        country = choosing_random_country()  # Choosing a new country 
        n_country = hide_country_letter(country)  
        country_label.config(text = n_country)  # Insert new name in place of previous name in label
        guess.delete(0,END)   # Clear input_text field
        guess.insert(INSERT, n_country)  # Insert new name in place of previous name in input_text_bar
        change_health -= 1  


def user_answer():   # Get answers from the user using inputbox
	user_guess = guess.get()
	return user_guess

def cal_score_plus(c):   # Counting gift points
    global score_plus
    if 5 < len(c) < 10:
        score_plus += 1
    elif 9 < len(c) < 18:
        score_plus += 2
    elif 17 > len(c) >= 20:
        score_plus += 3
        
# Check user answer 
def check_answer():
    global health_value, score, score_plus
    if user_answer() == country:   # answer is true
        cal_score_plus(country)   # If the user's answer is correct, the gift score will be checked
        if score-(score-score_plus) < score_plus:   # If the gift score is less than the logical score, it will be added
            score += score_plus
        tkinter.messagebox.showinfo("watchers", "You won :)\nYour score in this game is {} out of 100".format(score))
        root.destroy()  # Destroy the game
    else:   # answer is false, the health_value & score will be checked
        health_value -= 1
        health['value'] = health_value
        score -= 10
        watchers()   # To check the player's health_value

def help_btn(c):
    global score, health_value, times
    help = selected_option.get()
    _len = len(c)   # Check the country_name length
    if times == 1:   # Check the times can be use help
        times += 1
        if help == 1:   # Option 1
            if health_value > 1:   # Checking the health_value for to reduce health_value
                if _len == 4:
                    New_country = c[0:3] + "-"
                    score -= 15
                    health_value -= 1
                    return New_country
                elif _len == 5:
                    New_country = c[0] + "-" + c[2:]
                    score -= 15
                    health_value -= 1
                    return New_country
                elif _len <= 9:
                    New_country = c[0:3] + "-" + c[4:]
                    score -= 20
                    health_value -= 1
                    return New_country
                elif _len <= 17:
                    New_country = c[0:4] + "-" + c[5:7] + "-" + c[8:]
                    health_value -= 1
                    score -= 25
                    return New_country
                elif _len <= 20:
                    New_country = c[0:2] + "-" + c[3] + "-" + c[5:6] + "--" + c[9:12] + "--" + c[15] + "-"+ c[16:]
                    health_value -= 1
                    score -= 25
                    return New_country
            else:
                tkinter.messagebox.showinfo("watchers", "شما یک جان دارید و نمی توانید از کمک استفاده کنید")
                times -= 1
        
        if help == 2:   # Option 2
            if health_value > 3:   # Checking the health_value for to reduce health_value
                if _len > 9:
                    if _len <= 17:
                        New_country = c[0:7] + "-" + c[8:]
                        health_value -= 3
                        score -= 35
                        return New_country
                    elif _len <= 20:
                        New_country = c[0:2] + "-" + c[3] + "-" + c[5:7] + "--" + c[9:13] + "-" + c[14] + "-"+ c[16:]
                        health_value -= 3
                        score -= 30
                        return New_country
                else:
                    tkinter.messagebox.showinfo("watchers", "تعداد حروف باید بیشتر از نُه باشد")   
                    times -= 1  
            else:
                tkinter.messagebox.showinfo("watchers", "شما سه جان یا کمتر دارید و نمی توانید از این کمک استفاده کنید")
                times -= 1
    else:
        tkinter.messagebox.showinfo("watchers", "فقط یک بار میتوانید از کمک استفاده کنید")
    
def help_btn_run():   # To run the Help button
    global times
    new_country_name = help_btn(country)
    if new_country_name:   # If the user has the advantage of using the help button, some will be returned and the help will be displayed to the user.
        country_label.config(text = new_country_name)
        guess.delete(0,END)
        guess.insert(INSERT, new_country_name)
        health['value'] = health_value


def user_guide():   # user_guide
    tkinter.messagebox.showinfo("watchers", "'برخی از نام ها دارای فاصله (وایت اسپیس) و امکان دارند این فاصله به عنوان جای خالی قرار بگیرد '\n'عواملی که باعث کم شدن امتیاز میشود: استفاده از کمک، عوض کردن نام کشور'\n'عواملی ک باعث افزایش امتیاز میشود: بسته به تعداد حروف قابل حدس؛ بین 1 تا 3 امتیاز به امتیاز شما اظافه میگردد'\n'برای هر کلمه فقط یک بار میتوان از کمک استفاده کرد '\n'برای وارد کردن نام ها بجای هر خط یک حرف وارد کنید ، توجه داشته باشید که برنامه به حروف کوچک و بزرگ حساس است'")

# Cheat:
def cheat():   
    if admin_input.get() == '000111000':
        tkinter.messagebox.showinfo("***CHEAT***", "country_name: {}".format(country))
        admin_label.destroy()
        admin_input.destroy()
        submit_btn.destroy()
    	

root = Tk()

# Cheat:
def admin(): 
    admin_input.insert(INSERT, "****")
    admin_input.place(x=422, y=417)	
    admin_label.pack()
    admin_label.place(x=250, y=415)
    submit_btn.place(x=555, y=416)
admin_label = Label(root, text='Enter access code =>', bg='#7FFFD4', fg='#FF2B20', font=('verdana', 10, 'normal'))
admin_input=Entry(root)
submit_btn = Button(root, text='SUBMIT', bg='#FF8C00', font=('arial', 7, 'bold'), command=cheat)
    

# This is the section of code which creates the main window
root.geometry('894x562')
root.resizable(0, 0) # Don't allow resizing in the x or y direction
root.configure(background='#7FFFD4')
root.title('Country_Guess')

# This is the section of code which creates the label
Label(root, text=':نام کشور', bg='#7FFFD4', font=('arial', 25, 'normal')).place(x=645, y=124)
Label(root, text=':حدس شما', bg='#7FFFD4', font=('arial', 25, 'normal')).place(x=646, y=208)
Label(root, text=':کمک', bg='#7FFFD4', font=('verdana', 10, 'italic')).place(x=848, y=55)
Label(root, text=':جان', bg='#7FFFD4', font=('arial', 10, 'normal')).place(x=847, y=12)
# Making label for countries' name
country_label = Label(root, text=n_country, bg='#7FFFD4', font=('courier', 20, 'bold'))
country_label.pack()
country_label.place(x=190, y=126)

# Determine the number of times you can change the name of the country
country_change_health = Label(root, text='. . .', bg='#7FFFD4', fg='#FF2B20', font=('verdana', 30, 'bold'))
country_change_health.pack()
country_change_health.place(x=7, y=105)

# This is the section of code which creates a button
Button(root, text='راهنما', bg='#B0F70E', font=('arial', 7, 'normal'), command=user_guide).place(x=7, y=5)
# Admin button:
Button(root, text='ادمین', bg='#B0F70E', font=('arial', 7, 'normal'), command=admin).place(x=7, y=30)
# Help_submit button:
Button(root, text='+', bg='#FF8C00', font=('arial', 7, 'bold'), command=help_btn_run).place(x=835, y=56)
# Answer_submit button:
Button(root, text='چک', bg='#ff73e0', font=('arial', 15, 'bold'), command=check_answer).place(x=325, y=205)
# Change_country button:
Button(root, text='عوض کردن کشور', bg='#F5F5DC', font=('arial', 10, 'normal'), command=country_change).place(x=87, y=131)

# Radio buttons:
selected_option = tk.IntVar()
# option1:
help_1 = Radiobutton(root, text="نشان دادن یک الی دو حرف و گرفتن یک جان", variable=selected_option, value=1, bg='#F0F8FF', font=('arial', 12, 'normal'))
help_1.pack
help_1.place(x=520, y=75)
# optio21:
help_2 = Radiobutton(root, text=" نشان دادن سه حرف و گرفتن سه جان (فقط برای تعداد حروف بالای 9)", variable=selected_option, value=2, bg='#F0F8FF', font=('arial', 12, 'normal'))
help_2.pack
help_2.place(x=420, y=45)

# Create an input box for user response
guess=Entry(root)
guess.place(x=422, y=217)
guess.insert(INSERT, n_country)

# Health_value:
# This is the section of code which creates a color style to be used with the progress bar (health_value_style)
health_style = ttk.Style()
health_style.theme_use('clam')
health_style.configure('health.Horizontal.TProgressbar', foreground='#DC143C', background='#DC143C')
# This is the section of code which creates a progress bar
health=ttk.Progressbar(root, style='health.Horizontal.TProgressbar', orient='horizontal', length=116, mode='determinate', maximum=5, value=5)
health.place(x=730, y=13)


root.mainloop()
