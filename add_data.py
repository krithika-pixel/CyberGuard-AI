import mysql.connector


connection = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    database = 'cybersecurity',
    password = 'krithika123'
)
print("Connected to:", connection.database)
print("Server:", connection.server_host)
print("Port:", connection.server_port)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS cybersecurity (username VARCHAR(200) UNIQUE NOT NULL," \
" password VARCHAR(200) NOT NULL)")

users = [
    ("aarav.sharma", "Aarav@2026"),
    ("ananya.verma", "Ananya@2026"),
    ("rohan.mehta", "Rohan@2026"),
    ("priya.shah", "Priya@2026"),
    ("rahul.kapoor", "Rahul@2026"),
    ("neha.malhotra", "Neha@2026"),
    ("arjun.reddy", "Arjun@2026"),
    ("ishita.rao", "Ishita@2026"),
    ("karan.gupta", "Karan@2026"),
    ("meera.iyer", "Meera@2026"),

    ("aditya.singh", "Aditya@2026"),
    ("simran.kaur", "Simran@2026"),
    ("vikas.jain", "Vikas@2026"),
    ("riya.mehra", "Riya@2026"),
    ("siddharth.patel", "Siddharth@2026"),
    ("tanvi.sharma", "Tanvi@2026"),
    ("nikhil.verma", "Nikhil@2026"),
    ("kavya.nair", "Kavya@2026"),
    ("manish.agarwal", "Manish@2026"),
    ("shruti.rao", "Shruti@2026"),

    ("dev.iyer", "Dev@2026"),
    ("anika.kapoor", "Anika@2026"),
    ("rohit.bansal", "Rohit@2026"),
    ("sakshi.gupta", "Sakshi@2026"),
    ("varun.shah", "Varun@2026"),
    ("aisha.khan", "Aisha@2026"),
    ("yash.mehra", "Yash@2026"),
    ("pallavi.joshi", "Pallavi@2026"),
    ("akshay.patel", "Akshay@2026"),
    ("diya.singh", "Diya@2026"),

    ("vivek.chopra", "Vivek@2026"),
    ("simran.mehta", "Simran@2027"),
    ("harsh.verma", "Harsh@2026"),
    ("nisha.sharma", "Nisha@2026"),
    ("aman.kumar", "Aman@2026"),
    ("preeti.nair", "Preeti@2026"),
    ("mohit.gupta", "Mohit@2026"),
    ("rhea.malhotra", "Rhea@2026"),
    ("sahil.agarwal", "Sahil@2026"),
    ("kriti.jain", "Kriti@2026"),

    ("ayush.reddy", "Ayush@2026"),
    ("muskan.shah", "Muskan@2026"),
    ("abhishek.rao", "Abhishek@2026"),
    ("sonal.mehta", "Sonal@2026"),
    ("kunal.verma", "Kunal@2026"),
    ("lavanya.iyer", "Lavanya@2026"),
    ("deepak.singh", "Deepak@2026"),
    ("navya.kapoor", "Navya@2026"),
    ("rajat.gupta", "Rajat@2026"),
    ("simran.joshi", "Simran@2028"),

    ("aryan.sharma", "Aryan@2026"),
    ("isha.verma", "Isha@2026"),
    ("varsha.nair", "Varsha@2026"),
    ("tarun.patel", "Tarun@2026"),
    ("mansi.shah", "Mansi@2026"),
    ("gaurav.mehta", "Gaurav@2026"),
    ("pooja.rao", "Pooja@2026"),
    ("devansh.kumar", "Devansh@2026"),
    ("ritika.jain", "Ritika@2026"),
    ("sameer.kapoor", "Sameer@2026"),

    ("akanksha.gupta", "Akanksha@2026"),
    ("rohit.sharma", "Rohit@2027"),
    ("naman.verma", "Naman@2026"),
    ("shreya.patel", "Shreya@2026"),
    ("abhay.singh", "Abhay@2026"),
    ("monika.iyer", "Monika@2026"),
    ("karishma.rao", "Karishma@2026"),
    ("vivek.mehta", "Vivek@2027"),
    ("harini.nair", "Harini@2026"),
    ("manav.shah", "Manav@2026"),

    ("atul.gupta", "Atul@2026"),
    ("nidhi.sharma", "Nidhi@2026"),
    ("saurabh.verma", "Saurabh@2026"),
    ("riya.patel", "Riya@2027"),
    ("anmol.singh", "Anmol@2026"),
    ("divya.rao", "Divya@2026"),
    ("karan.mehta", "Karan@2027"),
    ("shraddha.nair", "Shraddha@2026"),
    ("varun.kapoor", "Varun@2027"),
    ("neel.jain", "Neel@2026"),

    ("aakash.sharma", "Aakash@2026"),
    ("swati.verma", "Swati@2026"),
    ("rishabh.patel", "Rishabh@2026"),
    ("komal.singh", "Komal@2026"),
    ("manish.rao", "Manish@2027"),
    ("shubham.gupta", "Shubham@2026"),
    ("payal.mehta", "Payal@2026"),
    ("omkar.nair", "Omkar@2026"),
    ("isha.kapoor", "Isha@2027"),
    ("rahul.jain", "Rahul@2027"),

    ("arvind.shah", "Arvind@2026"),
    ("sakshi.verma", "Sakshi@2027"),
    ("madhav.rao", "Madhav@2026"),
    ("kiran.patel", "Kiran@2026"),
    ("shweta.sharma", "Shweta@2026"),
    ("vishal.mehta", "Vishal@2026"),
    ("aarti.nair", "Aarti@2026"),
    ("rohan.gupta", "Rohan@2027"),
    ("megha.singh", "Megha@2026"),
    ("devika.jain", "Devika@2026")
]

query = "INSERT INTO cybersecuritylogin (username, password) VALUES (%s, %s)"


cursor.executemany(query, users)
connection.commit()

print("Users added successfully!")

cursor.execute("SELECT COUNT(*) FROM cybersecurity")
print("Total users:", cursor.fetchone()[0])

cursor.close()
connection.close()