from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import tkinter.ttk as ttk
import random

root = Tk()
root.title("Guess the Flag")
root.iconbitmap('flag.ico')
root.attributes('-fullscreen', True)
root.configure(bg="#E3F2FD")

#dictionary that connects countries to their file names
flags = {
    'afghanistan.png': 'Afghanistan',
    'albania.png': 'Albania',
    'algeria.png': 'Algeria',
    'andorra.png': 'Andorra',
    'angola.png': 'Angola',
    'antigua_and_barbuda.png': 'Antigua and Barbuda',
    'argentina.png': 'Argentina',
    'armenia.png': 'Armenia',
    'australia.png': 'Australia',
    'austria.png': 'Austria',
    'azerbaijan.png': 'Azerbaijan',
    'bahamas.png': 'The Bahamas',
    'bahrain.png': 'Bahrain',
    'bangladesh.png': 'Bangladesh',
    'barbados.png': 'Barbados',
    'belarus.png': 'Belarus',
    'belgium.png': 'Belgium',
    'belize.png': 'Belize',
    'benin.png': 'Benin',
    'bhutan.png': 'Bhutan',
    'bolivia.png': 'Bolivia',
    'bosnia_and_herzegovina.png': 'Bosnia and Herzegovina',
    'botswana.png': 'Botswana',
    'brazil.png': 'Brazil',
    'brunei.png': 'Brunei',
    'bulgaria.png': 'Bulgaria',
    'burkina_faso.png': 'Burkina Faso',
    'burundi.png': 'Burundi',
    'cabo_verde.png': 'Cabo Verde',
    'cambodia.png': 'Cambodia',
    'cameroon.png': 'Cameroon',
    'canada.png': 'Canada',
    'central_african_republic.png': 'Central African Republic',
    'chad.png': 'Chad',
    'chile.png': 'Chile',
    'china.png': 'China',
    'colombia.png': 'Colombia',
    'comoros.png': 'Comoros',
    'congo.png': 'Congo',
    'costa_rica.png': 'Costa Rica',
    'cote_d_ivoire.png': 'Côte d’Ivoire',
    'croatia.png': 'Croatia',
    'cuba.png': 'Cuba',
    'cyprus.png': 'Cyprus',
    'czech_republic.png': 'Czech Republic',
    'democratic_republic_of_the_congo.png': 'Democratic Republic of the Congo',
    'denmark.png': 'Denmark',
    'djibouti.png': 'Djibouti',
    'dominica.png': 'Dominica',
    'dominican_republic.png': 'Dominican Republic',
    'east_timor_timor_leste.png': 'East Timor (Timor-Leste)',
    'ecuador.png': 'Ecuador',
    'egypt.png': 'Egypt',
    'el_salvador.png': 'El Salvador',
    'equatorial_guinea.png': 'Equatorial Guinea',
    'eritrea.png': 'Eritrea',
    'estonia.png': 'Estonia',
    'eswatini.png': 'Eswatini',
    'ethiopia.png': 'Ethiopia',
    'fiji.png': 'Fiji',
    'finland.png': 'Finland',
    'france.png': 'France',
    'gabon.png': 'Gabon',
    'the_gambia.png': 'The Gambia',
    'georgia.png': 'Georgia',
    'germany.png': 'Germany',
    'ghana.png': 'Ghana',
    'greece.png': 'Greece',
    'grenada.png': 'Grenada',
    'guatemala.png': 'Guatemala',
    'guinea.png': 'Guinea',
    'guinea_bissau.png': 'Guinea-Bissau',
    'guyana.png': 'Guyana',
    'haiti.png': 'Haiti',
    'honduras.png': 'Honduras',
    'hungary.png': 'Hungary',
    'iceland.png': 'Iceland',
    'india.png': 'India',
    'indonesia.png': 'Indonesia',
    'iran.png': 'Iran',
    'iraq.png': 'Iraq',
    'ireland.png': 'Ireland',
    'israel.png': 'Israel',
    'italy.png': 'Italy',
    'jamaica.png': 'Jamaica',
    'japan.png': 'Japan',
    'jordan.png': 'Jordan',
    'kazakhstan.png': 'Kazakhstan',
    'kenya.png': 'Kenya',
    'kiribati.png': 'Kiribati',
    'korea_north.png': 'Korea, North',
    'korea_south.png': 'Korea, South',
    'kosovo.png': 'Kosovo',
    'kuwait.png': 'Kuwait',
    'kyrgyzstan.png': 'Kyrgyzstan',
    'laos.png': 'Laos',
    'latvia.png': 'Latvia',
    'lebanon.png': 'Lebanon',
    'lesotho.png': 'Lesotho',
    'liberia.png': 'Liberia',
    'libya.png': 'Libya',
    'liechtenstein.png': 'Liechtenstein',
    'lithuania.png': 'Lithuania',
    'luxembourg.png': 'Luxembourg',
    'madagascar.png': 'Madagascar',
    'malawi.png': 'Malawi',
    'malaysia.png': 'Malaysia',
    'maldives.png': 'Maldives',
    'mali.png': 'Mali',
    'malta.png': 'Malta',
    'marshall_islands.png': 'Marshall Islands',
    'mauritania.png': 'Mauritania',
    'mauritius.png': 'Mauritius',
    'mexico.png': 'Mexico',
    'micronesia_federated_states_of.png': 'Micronesia, Federated States of',
    'moldova.png': 'Moldova',
    'monaco.png': 'Monaco',
    'mongolia.png': 'Mongolia',
    'montenegro.png': 'Montenegro',
    'morocco.png': 'Morocco',
    'mozambique.png': 'Mozambique',
    'myanmar_burma.png': 'Myanmar (Burma)',
    'namibia.png': 'Namibia',
    'nauru.png': 'Nauru',
    'nepal.png': 'Nepal',
    'netherlands.png': 'Netherlands',
    'new_zealand.png': 'New Zealand',
    'nicaragua.png': 'Nicaragua',
    'niger.png': 'Niger',
    'nigeria.png': 'Nigeria',
    'north_macedonia.png': 'North Macedonia',
    'norway.png': 'Norway',
    'oman.png': 'Oman',
    'pakistan.png': 'Pakistan',
    'palau.png': 'Palau',
    'panama.png': 'Panama',
    'papua_new_guinea.png': 'Papua New Guinea',
    'paraguay.png': 'Paraguay',
    'peru.png': 'Peru',
    'philippines.png': 'Philippines',
    'poland.png': 'Poland',
    'portugal.png': 'Portugal',
    'qatar.png': 'Qatar',
    'romania.png': 'Romania',
    'russia.png': 'Russia',
    'rwanda.png': 'Rwanda',
    'saint_kitts_and_nevis.png': 'Saint Kitts and Nevis',
    'saint_lucia.png': 'Saint Lucia',
    'saint_vincent_and_the_grenadines.png': 'Saint Vincent and the Grenadines',
    'samoa.png': 'Samoa',
    'san_marino.png': 'San Marino',
    'sao_tome_and_principe.png': 'Sao Tome and Principe',
    'saudi_arabia.png': 'Saudi Arabia',
    'senegal.png': 'Senegal',
    'serbia.png': 'Serbia',
    'seychelles.png': 'Seychelles',
    'sierra_leone.png': 'Sierra Leone',
    'singapore.png': 'Singapore',
    'slovakia.png': 'Slovakia',
    'slovenia.png': 'Slovenia',
    'solomon_islands.png': 'Solomon Islands',
    'somalia.png': 'Somalia',
    'south_africa.png': 'South Africa',
    'spain.png': 'Spain',
    'sri_lanka.png': 'Sri Lanka',
    'sudan.png': 'Sudan',
    'south_sudan.png': 'South Sudan',
    'suriname.png': 'Suriname',
    'sweden.png': 'Sweden',
    'switzerland.png': 'Switzerland',
    'syria.png': 'Syria',
    'taiwan.png': 'Taiwan',
    'tajikistan.png': 'Tajikistan',
    'tanzania.png': 'Tanzania',
    'thailand.png': 'Thailand',
    'togo.png': 'Togo',
    'tonga.png': 'Tonga',
    'trinidad_and_tobago.png': 'Trinidad and Tobago',
    'tunisia.png': 'Tunisia',
    'turkey.png': 'Turkey',
    'turkmenistan.png': 'Turkmenistan',
    'tuvalu.png': 'Tuvalu',
    'uganda.png': 'Uganda',
    'ukraine.png': 'Ukraine',
    'united_arab_emirates.png': 'United Arab Emirates',
    'united_kingdom.png': 'United Kingdom',
    'united_states.png': 'United States',
    'uruguay.png': 'Uruguay',
    'uzbekistan.png': 'Uzbekistan',
    'vanuatu.png': 'Vanuatu',
    'vatican_city.png': 'Vatican City',
    'venezuela.png': 'Venezuela',
    'vietnam.png': 'Vietnam',
    'yemen.png': 'Yemen',
    'zambia.png': 'Zambia',
    'zimbabwe.png': 'Zimbabwe'
} 

#converts the dictionary into a list
flag_list = list(flags.keys())
country_list = list(flags.values())
current_flag_index = 0

score = 0

#shuffles flag list
random.shuffle(flag_list)

 #function that updates the displayed flag
def update_flag():
    global current_flag_index, my_img, new_pic
    if current_flag_index < len(flag_list):  #checks for flags
        current_flag = flag_list[current_flag_index]  #grabs flags
        my_img = Image.open(current_flag)
        resized = my_img.resize((500, 325), Image.LANCZOS)
        new_pic = ImageTk.PhotoImage(resized)
        my_label.config(image=new_pic)
        combo.set('')
    else:
        messagebox.showinfo("Game Over", f"Your final score is: {score}")
        root.destroy()

#function that checks for the user's guess
def check_guess():
    global score, current_flag_index
    guess = combo.get()  #gets the user's guess from the combobox
    correct_answer = flags[flag_list[current_flag_index]]  #gets the correct country name for the current flag
    
    if guess == correct_answer:  #checks if the user's guess is correct
        result_label.config(text="Correct!", fg="green")
        score += 1
    else:
        result_label.config(text=f"Incorrect! The correct answer is {correct_answer}.", fg="red")
    
    score_label.config(text=f"Score: {score}")
    current_flag_index += 1
    update_flag()

#function to skip the current flag
def skip_flag():
    global current_flag_index
    current_flag_index += 1
    result_label.config(text="")
    update_flag()

#setup for displaying the flag
my_img = Image.open(flag_list[current_flag_index])
resized = my_img.resize((500, 325), Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)

#widgets and buttons
my_label = Label(root, image=new_pic, bg="#f0f0f0", bd=10, relief=RIDGE)
combo = ttk.Combobox(root, values=country_list, font=('Arial', 16), state='readonly', justify=CENTER)
combo.set("Select a country")
combo.config(width=30)
guess_button = Button(root, text="Guess", command=check_guess, font=('Arial', 14, 'bold'), bg="#4CAF50", fg="white", padx=20, pady=10)
skip_button = Button(root, text="Skip", command=skip_flag, font=('Arial', 14, 'bold'), bg="#f44336", fg="white", padx=20, pady=10)
result_label = Label(root, text="", font=('Arial', 18), bg="#f0f0f0")
score_label = Label(root, text=f"Score: {score}", font=('Arial', 16, 'bold'), bg="#f0f0f0")
exit_button = Button(root, text="Exit", command=root.destroy, font=('Arial', 14, 'bold'), bg="#9E9E9E", fg="white", padx=20, pady=10)

#configures the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)

#places the widgets of the grid layout
score_label.grid(row=0, column=0, columnspan=3, pady=20)
my_label.grid(row=1, column=0, columnspan=3, pady=20)
combo.grid(row=2, column=0, columnspan=3, pady=20)
guess_button.grid(row=3, column=1, pady=20)
skip_button.grid(row=3, column=0, pady=20)
exit_button.grid(row=3, column=2, pady=20)
result_label.grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()