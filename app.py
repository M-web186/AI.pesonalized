from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ai_learning_system_key"

# ================= USERS =================
users = []

# ================= PERFORMANCE STORAGE =================
performance = {}

# ================= QUESTIONS =================
questions = {
    "ICT": [
        {"q": "What is the full meaning of ICT in computing?", "options": ["Information Communication Technology", "Internet Computer Technology", "Internal Control Tool", "Information Control Theory"], "answer": "Information Communication Technology"},
        {"q": "A computer is best defined as?", "options": ["A device that processes data into information", "A machine for typing only", "A calculator", "A storage box"], "answer": "A device that processes data into information"},
        {"q": "Which part of a computer processes instructions?", "options": ["CPU", "Monitor", "Keyboard", "Mouse"], "answer": "CPU"},
        {"q": "Which device is used for input?", "options": ["Keyboard", "Monitor", "Printer", "Speaker"], "answer": "Keyboard"},
        {"q": "Which is an output device?", "options": ["Monitor", "Mouse", "Scanner", "Keyboard"], "answer": "Monitor"},
        {"q": "RAM is used for?", "options": ["Temporary storage", "Permanent storage", "Printing", "Gaming"], "answer": "Temporary storage"},
        {"q": "ROM stores?", "options": ["Permanent instructions", "Temporary files", "Games", "Videos"], "answer": "Permanent instructions"},
        {"q": "Which is system software?", "options": ["Windows", "MS Word", "Chrome", "Excel"], "answer": "Windows"},
        {"q": "Which is a storage device?", "options": ["Hard disk", "Monitor", "Keyboard", "Mouse"], "answer": "Hard disk"},
        {"q": "LAN stands for?", "options": ["Local Area Network", "Large Area Network", "Long Access Node", "Logical Access Network"], "answer": "Local Area Network"},
        {"q": "Virus is?", "options": ["Malicious software", "Hardware", "Browser", "Game"], "answer": "Malicious software"},
        {"q": "Internet is used for?", "options": ["Communication", "Cooking", "Driving", "Painting"], "answer": "Communication"},
        {"q": "Browser example?", "options": ["Chrome", "Word", "Excel", "Paint"], "answer": "Chrome"},
        {"q": "WWW stands for?", "options": ["World Wide Web", "Web World Wide", "Wide World Web", "Web Wide World"], "answer": "World Wide Web"},
        {"q": "Printer is?", "options": ["Output device", "Input device", "Storage", "Software"], "answer": "Output device"},
        {"q": "USB is used for?", "options": ["Data storage", "Cooking", "Driving", "Gaming"], "answer": "Data storage"},
        {"q": "Operating system manages?", "options": ["Hardware and software", "Only games", "Only internet", "Only files"], "answer": "Hardware and software"},
        {"q": "Mouse is?", "options": ["Input device", "Output device", "Storage", "Software"], "answer": "Input device"},
        {"q": "Monitor is?", "options": ["Output device", "Input device", "Storage", "CPU"], "answer": "Output device"},
        {"q": "CPU stands for?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Print Unit", "Control Processing Unit"], "answer": "Central Processing Unit"},
    ],

    "Programming": [
        {"q": "Python is a?", "options": ["Programming language", "Hardware", "Game", "System"], "answer": "Programming language"},
        {"q": "HTML is used to create?", "options": ["Web pages", "Software", "Games", "Database"], "answer": "Web pages"},
        {"q": "CSS is used for?", "options": ["Styling", "Logic", "Hardware", "Storage"], "answer": "Styling"},
        {"q": "Variable stores?", "options": ["Data", "CPU", "Monitor", "Printer"], "answer": "Data"},
        {"q": "Loop is used for?", "options": ["Repetition", "Decision", "Storage", "Display"], "answer": "Repetition"},
        {"q": "IF statement is?", "options": ["Decision making", "Loop", "Function", "Variable"], "answer": "Decision making"},
        {"q": "Function is?", "options": ["Reusable code block", "Hardware", "File", "Game"], "answer": "Reusable code block"},
        {"q": "Python uses?", "options": ["Indentation", "Tags", "Tables", "Graphics"], "answer": "Indentation"},
        {"q": "JavaScript is used for?", "options": ["Web interaction", "Hardware", "Storage", "CPU"], "answer": "Web interaction"},
        {"q": "IDE stands for?", "options": ["Integrated Development Environment", "Internet Data Engine", "Input Device Editor", "Internal Design Engine"], "answer": "Integrated Development Environment"},
        {"q": "Debugging means?", "options": ["Finding errors", "Writing code", "Deleting files", "Running programs"], "answer": "Finding errors"},
        {"q": "List is?", "options": ["Collection of items", "Single value", "Loop", "File"], "answer": "Collection of items"},
        {"q": "String is?", "options": ["Text", "Number", "Image", "File"], "answer": "Text"},
        {"q": "Algorithm is?", "options": ["Step-by-step solution", "Game", "Hardware", "Software"], "answer": "Step-by-step solution"},
        {"q": "Python extension?", "options": [".py", ".html", ".css", ".exe"], "answer": ".py"},
        {"q": "Input function?", "options": ["input()", "print()", "scan()", "read()"], "answer": "input()"},
        {"q": "Output function?", "options": ["print()", "show()", "display()", "echo()"], "answer": "print()"},
        {"q": "Break is used in?", "options": ["Loops", "HTML", "CSS", "Database"], "answer": "Loops"},
        {"q": "Bug means?", "options": ["Error", "Hardware", "Game", "File"], "answer": "Error"},
        {"q": "Compiler is?", "options": ["Translator", "Browser", "Game", "Device"], "answer": "Translator"},
    ],

    "Cybersecurity": [
        {"q": "Cybersecurity protects?", "options": ["Systems and data", "Food", "Cars", "Books"], "answer": "Systems and data"},
        {"q": "Virus is?", "options": ["Malware", "Hardware", "Browser", "Game"], "answer": "Malware"},
        {"q": "Firewall is for?", "options": ["Security", "Gaming", "Typing", "Printing"], "answer": "Security"},
        {"q": "Phishing is?", "options": ["Stealing information", "Programming", "Designing", "Gaming"], "answer": "Stealing information"},
        {"q": "Strong password has?", "options": ["Letters, numbers, symbols", "Only letters", "Only numbers", "Name only"], "answer": "Letters, numbers, symbols"},
        {"q": "Antivirus is used to?", "options": ["Remove viruses", "Create viruses", "Code apps", "Print files"], "answer": "Remove viruses"},
        {"q": "Hacking is?", "options": ["Unauthorized access", "Printing", "Coding", "Gaming"], "answer": "Unauthorized access"},
        {"q": "Encryption means?", "options": ["Securing data", "Deleting data", "Copying files", "Printing"], "answer": "Securing data"},
        {"q": "Malware includes?", "options": ["Viruses", "Browsers", "Hardware", "Apps"], "answer": "Viruses"},
        {"q": "Spyware is?", "options": ["Monitoring software", "Game", "Browser", "Hardware"], "answer": "Monitoring software"},
        {"q": "Backup is?", "options": ["Copy of data", "Virus", "Software", "Game"], "answer": "Copy of data"},
        {"q": "Safe browsing means?", "options": ["Avoid unsafe sites", "Download everything", "Ignore warnings", "Click all links"], "answer": "Avoid unsafe sites"},
        {"q": "Username is?", "options": ["Identity", "Password", "Virus", "File"], "answer": "Identity"},
        {"q": "Password should be?", "options": ["Strong", "Short", "Simple", "Name"], "answer": "Strong"},
        {"q": "HTTPS means?", "options": ["Secure site", "Hardware", "Game", "Software"], "answer": "Secure site"},
        {"q": "Spam is?", "options": ["Unwanted messages", "Software", "Hardware", "Game"], "answer": "Unwanted messages"},
        {"q": "Update improves?", "options": ["Security", "Damage", "Virus", "Errors"], "answer": "Security"},
        {"q": "Cyber attack targets?", "options": ["Systems", "Food", "Books", "Cars"], "answer": "Systems"},
        {"q": "Two-factor authentication improves?", "options": ["Security", "Speed", "Graphics", "Storage"], "answer": "Security"},
        {"q": "Social engineering is?", "options": ["Tricking users", "Coding", "Printing", "Gaming"], "answer": "Tricking users"},
    ],

    "Networking": [
        {"q": "A computer network is?", "options": ["Connected computers sharing data", "Single computer", "Game", "Software"], "answer": "Connected computers sharing data"},
        {"q": "LAN stands for?", "options": ["Local Area Network", "Large Area Network", "Long Access Node", "Light Access Network"], "answer": "Local Area Network"},
        {"q": "WAN stands for?", "options": ["Wide Area Network", "Web Area Network", "Work Area Network", "Wireless Access Node"], "answer": "Wide Area Network"},
        {"q": "Router is used to?", "options": ["Connect networks", "Print", "Store files", "Code"], "answer": "Connect networks"},
        {"q": "Switch connects?", "options": ["Devices", "Games", "Apps", "Files"], "answer": "Devices"},
        {"q": "IP address is?", "options": ["Device ID", "Software", "Game", "File"], "answer": "Device ID"},
        {"q": "Modem is for?", "options": ["Internet", "Printing", "Gaming", "Coding"], "answer": "Internet"},
        {"q": "Server is?", "options": ["Provides services", "User device", "Game", "App"], "answer": "Provides services"},
        {"q": "Client is?", "options": ["Requests services", "Provides services", "Hardware", "Software"], "answer": "Requests services"},
        {"q": "Topology means?", "options": ["Network layout", "Game", "Software", "Virus"], "answer": "Network layout"},
        {"q": "Star topology uses?", "options": ["Central device", "No device", "Only cables", "Only software"], "answer": "Central device"},
        {"q": "Wi-Fi is?", "options": ["Wireless network", "Hardware", "Game", "Software"], "answer": "Wireless network"},
        {"q": "Bluetooth is?", "options": ["Short-range connection", "Internet", "Printing", "Coding"], "answer": "Short-range connection"},
        {"q": "Bandwidth means?", "options": ["Speed", "Storage", "CPU", "RAM"], "answer": "Speed"},
        {"q": "DNS is?", "options": ["Domain system", "Game", "Software", "Hardware"], "answer": "Domain system"},
        {"q": "URL is?", "options": ["Website address", "Game", "App", "File"], "answer": "Website address"},
        {"q": "Email is used for?", "options": ["Communication", "Cooking", "Driving", "Gaming"], "answer": "Communication"},
        {"q": "Firewall protects?", "options": ["Network", "Game", "Book", "Car"], "answer": "Network"},
        {"q": "Internet is?", "options": ["Global network", "Single device", "Game", "Software"], "answer": "Global network"},
        {"q": "Client-server is?", "options": ["Network model", "Game", "Hardware", "App"], "answer": "Network model"},
    ]
}

# ================= CHATBOT KNOWLEDGE =================
chatbot_knowledge = {
    "python": "Python is a programming language used for AI, web development, and data science.",
    "ict": "ICT stands for Information Communication Technology.",
    "cpu": "CPU is the brain of the computer.",
    "lan": "LAN is a Local Area Network used in small areas like schools.",
    "wan": "WAN is a Wide Area Network covering large areas.",
    "cybersecurity": "Cybersecurity protects systems and data from attacks.",
    "virus": "A virus is malicious software that damages systems.",
    "html": "HTML is used to create web pages.",
    "css": "CSS is used to style web pages.",
    "router": "A router connects different networks."
}

# ================= HOME =================
@app.route('/')
def home():
    return redirect('/register')

# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = {
            "username": request.form['username'],
            "age": request.form['age'],
            "course": request.form['course'],
            "email": request.form['email'],
            "password": request.form['password']
        }
        users.append(user)
        return redirect('/login')

    return render_template("register.html")

# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        for user in users:
            if user['email'] == email and user['password'] == password:
                session['user'] = user
                return redirect('/dashboard')

        return "Invalid login"

    return render_template("login.html")

# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect('/login')

    user_perf = performance.get(user['username'], [])

    return render_template("dashboard.html", user=user, performance=user_perf)

# ================= QUIZ =================
@app.route('/quiz/<unit>')
def quiz(unit):
    user = session.get('user')
    if not user:
        return redirect('/login')

    quiz_questions = []

    for q in questions[unit]:
        options = [q["answer"]]

        all_answers = [x["answer"] for x in questions[unit] if x["answer"] != q["answer"]]
        random.shuffle(all_answers)

        options += all_answers[:3]
        random.shuffle(options)

        quiz_questions.append({
            "q": q["q"],
            "options": options,
            "answer": q["answer"]
        })

    random.shuffle(quiz_questions)

    session['quiz'] = quiz_questions

    return render_template("quiz.html", questions=quiz_questions, unit=unit)

# ================= SUBMIT =================
@app.route('/submit/<unit>', methods=['POST'])
def submit(unit):
    quiz = session.get('quiz', [])

    score = 0
    wrong_questions = []

    for i in range(len(quiz)):
        selected = request.form.get(f"q{i}")
        correct = quiz[i]["answer"]

        if selected == correct:
            score += 1
        else:
            wrong_questions.append(quiz[i]["q"])

    total = len(quiz)
    percentage = (score / total) * 100

    if percentage < 40:
        level = "Beginner"
        message = "You need more practice."
    elif percentage < 80:
        level = "Intermediate"
        message = "Good improvement!"
    else:
        level = "Advanced"
        message = "Excellent performance!"

    user = session.get('user')
    username = user['username']

    if username not in performance:
        performance[username] = []

    performance[username].append({
        "unit": unit,
        "score": score,
        "total": total,
        "level": level
    })

    return render_template(
        "result.html",
        score=score,
        total=total,
        level=level,
        message=message,
        wrong_questions=wrong_questions,
        unit=unit
    )

# ================= CHATBOT =================
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    response = ""

    if request.method == 'POST':
        msg = request.form['message'].lower()

        response = "Sorry, I don't understand that yet."

        for key in chatbot_knowledge:
            if key in msg:
                response = chatbot_knowledge[key]
                break

    return render_template("chat.html", response=response)

# ================= LOGOUT =================
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)