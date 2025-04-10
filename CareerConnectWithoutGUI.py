import heapq


class Career:
    def __init__(self, name, skills, preReq, careerField, connections=None, score=0):
        self.name = name  # Career name
        self.skills = skills  # List of required skills
        self.preReq = preReq if preReq else []  # List of study tracks or educational prerequisites
        self.careerField = careerField  # The field of the career
        self.connections = connections if connections else []  # Connections to other careers (could be for graph traversal, optional)
        self.score = score  # Heuristic score to be calculated

    def __lt__(self, other):
        return self.score > other.score  # Reverse the comparison for max-heap behavior

career_graph = {
    'Start':Career(
        name="Start",
        skills=["Technology","Computer", 'Python', 'Statistics', 'Critical Thinking', "Machine Learning"],
        preReq=['ICS', 'Pre-Engineering',"Pre-Medical"],
        careerField="",
        connections=["Business Analyst", 'Data Analyst','Doctor',"Psychology","Business Administration", "Electrical Engineering"]
    ),
    # Tech Careers
    'Data Scientist': Career(
        name='Data Scientist',
        skills=["Technology","Computer", 'Python', 'Statistics', 'Critical Thinking', "Machine Learning"],
        preReq=['ICS', 'Pre-Engineering'],
        careerField="Data Scientist",
        connections=['ML Engineer', 'Data Analyst'],
        score=0

    ),
    'Data Analyst': Career(
        name='Data Analyst',
        skills=["Technology","Computer", "Statistics","Mathematics",'SQL', 'Excel', 'Data Visualization'],
        preReq=['ICS', 'ICOM', 'Pre Engineering'],
        careerField="Data Scientist",
        connections=['Data Scientist', 'Business Analyst'],
        score=0
    ),
    'ML Engineer': Career(
        name='ML Engineer',
        skills=["Technology","Computer", 'Python', 'TensorFlow', 'Deep Learning', 'Statistics', 'Critical Thinking'],
        preReq=['ICS', 'Pre-Engineering'],
        careerField="Machine Learning",
        connections=['Data Scientist', 'AI Researcher'],
        score=0
    ),
    'AI Researcher': Career(
        name='AI Researcher',
        skills=["Technology","Computer", 'Machine Learning', 'Research', 'Statistics'],
        preReq=['ICS', 'Pre-Engineering'],
        careerField="Artificial Intelligence",
        connections=['ML Engineer'],
        score=0
    ),
    'Cybersecurity Specialist': Career(
        name='Cybersecurity Specialist',
        skills=["Technology","Computer", 'Network Security', 'Cryptography', 'Risk Assessment'],
        preReq=['ICS', 'Pre-Engineering'],
        careerField="Cybersecurity",
        connections=['Data Analyst', 'ML Engineer'],
        score=0
    )

,
    # Healthcare Careers
    'Doctor': Career(
        name='Doctor',
        skills=['Medical', 'Patient Care', 'Surgery'],
        preReq=['Pre-Medical'],
        careerField="Healthcare",
        connections=['Medical Researcher', "Nurse"],
        score=0
    ),
    'Nurse': Career(
        name='Nurse',
        skills=["Medical",'Patient Care'],
        preReq=['Pre-Medical'],
        careerField="Healthcare",
        connections=['Doctor', "Medical Researcher"],
        score=0
    ),
    'Medical Researcher': Career(
        name='Medical Researcher',
        skills=["Medical",'Research', "Critical Thinking"],
        preReq=['Pre-Medical'],
        careerField="Healthcare",
        connections=['Doctor', "Physiotherapist"],
        score=0
    ),
    'Physiotherapist': Career(
        name='Physiotherapist',
        skills=["Medical",'Physical Therapy', 'Patient Care', 'Rehabilitation'],
        preReq=['Pre-Medical'],
        careerField="Healthcare",
        connections=['Doctor', 'Medical Researcher', "Nurse"],
        score=0
    ),

    # Arts and Humanities Careers
    'Journalist': Career(
        name='Journalist',
        skills=['Writing', 'Communication', 'Research', "News", "Media", "Politics"],
        preReq=['FA', 'Pre-Engineering', 'Pre-Medical', 'ICOM', 'ICS'],
        careerField="Media",
        connections=['Content Writer', 'Literature Expert'],
        score=0
    ),
    'Content Writer': Career(
        name='Content Writer',
        skills=['Writing', 'Creativity',"Art", "Education", "Media"],
        preReq=['FA', 'Pre-Engineering', 'Pre-Medical', 'ICOM', 'ICS'],
        careerField="Media",
        connections=['Graphic Designer', 'Literature Expert'],
        score=0
    ),
    'Graphic Designer': Career(
        name='Graphic Designer',
        skills=['Adobe Photoshop', 'Creativity', 'Design', "Art", "Media"],
        preReq=['FA', 'Pre-Engineering', 'Pre-Medical', 'ICOM', 'ICS'],
        careerField="Design",
        connections=['UI/UX Designer', 'Content Writer'],
        score=0
    ),
    'Literature Expert': Career(
        name='Literature Expert',
        skills=["Communication",'Literature', 'Writing', 'Research'],
        preReq=['FA', 'Pre-Engineering', 'Pre-Medical', 'ICOM', 'ICS'],
        careerField="Humanities",
        connections=['Content Writer', 'Journalist'],
        score=0
    ),



    'Chemical Engineering': Career(
        name='Chemical Engineer',
        skills=["Chemistry",'Chemical Process Design', 'Material Science', 'Thermodynamics'],
        preReq=['Pre-Engineering', 'Pre-Medical'],
        careerField="Engineering",
        connections=[ 'Mechanical Engineering',"Civil Engineering"],
        score=0
    ),
    'Software Engineering': Career(
        name='Software Engineering',
        skills=["Technology","Computer", 'Programming', 'Software Design', 'Problem-Solving', 'Documentation'],
        preReq=['ICS', 'Pre-Engineering', 'Pre-Medical'],
        careerField="Engineering",
        connections=['Computer Science', 'Data Scientist', 'Information Technology'],
        score=0
    ),
    'Computer Science': Career(
        name='Computer Science',
        skills=["Technology","Computer", 'Algorithms', 'Data Structures', 'Programming'],
        preReq=['ICS', 'Pre-Engineering', 'Pre-Medical'],
        careerField="Engineering",
        connections=['Software Engineering', 'Artificial Intelligence', 'Cybersecurity'],
        score=0
    ),
    'Information Technology': Career(
        name='Information Technology',
        skills=["Technology","Computer", 'Networking', 'Problem-Solving', 'Security'],
        preReq=['ICS', 'ICOM', 'Pre-Engineering', 'Pre-Medical'],
        careerField="IT",
        connections=['Computer Science', 'Cybersecurity'],
        score=0
    ),

    # Artificial Intelligence and Data Science Fields
    'Artificial Intelligence': Career(
        name='Artificial Intelligence',
        skills=["Technology","Computer", 'Problem-Solving', 'Critical Thinking', 'Statistics'],
        preReq=['ICS', 'Pre-Engineering', 'Pre-Medical'],
        careerField="Data Scientist",
        connections=['Computer Science', 'Data Scientist'],
        score=0
    ),
    'Cybersecurity': Career(
        name='Cybersecurity',
        skills=['Network Security', 'Cryptography', 'Risk Management'],
        preReq=['ICS', 'Pre-Engineering', 'Pre-Medical'],
        careerField="IT",
        connections=['Information Technology', 'Computer Science', 'Software Engineering'],
        score=0
    ),

    # Engineering Fields
    'Electrical Engineering': Career(
        name='Electrical Engineering',
        skills=["Physics","Mathematics", 'Circuit Design', 'Electrical Systems', 'Problem-Solving'],
        preReq=['Pre-Engineering'],
        careerField="Engineering",
        connections=['Mechanical Engineering', 'Computer Science'],
        score=0
    ),
    'Mechanical Engineering': Career(
        name='Mechanical Engineering',
        skills=["Physics","Mathematics", 'Critical Thinking', 'Thermodynamics', 'Mechanics'],
        preReq=['Pre-Engineering'],
        careerField="Engineering",
        connections=['Civil Engineering', 'Electrical Engineering'],
        score=0
    ),
    'Civil Engineering': Career(
        name='Civil Engineering',
        skills=["Physics","Mathematics", 'Project Management', 'Design'],
        preReq=['Pre-Engineering'],
        careerField="Engineering",
        connections=['Mechanical Engineering'],
        score=0
    ),

    # Business and Economics Fields
    'Business Administration': Career(
        name='Business Administration',
        skills=["Business",'Leadership', 'Management', 'Finance'],
        preReq=['ICOM', 'FA'],
        careerField="Business",
        connections=['Marketing', 'Economics', 'Business Analyst'],
        score=0
    ),
    'Economics': Career(
        name='Economics',
        skills=["Business",'Statistics', 'Economic Theory', 'Critical Thinking',"Finance"],
        preReq=['ICOM', 'FA', "Pre-Engineering"],
        careerField="Business",
        connections=['Business Administration', 'Data Scientist'],
        score=0
    ),
    'Marketing': Career(
        name='Marketing',
        skills=['Market Analysis', 'Communication', 'Digital Marketing', "Media"],
        preReq=['ICOM', 'FA', 'Pre-Engineering', 'Pre-Medical', 'ICS'],
        careerField="Business",
        connections=['Business Administration'],
        score=0
    ),
    # Business Careers
    'Business Analyst': Career(
        name='Business Analyst',
        skills=["Communication", "Business", "Finance"],
        preReq=['ICOM', 'FA', 'Pre-Engineering', 'Pre-Medical'],
        careerField="Business",
        connections=['Data Analyst', "Business Administration"],
        score=0
    ),
    # Social Sciences and Humanities Fields
    'Psychology': Career(
        name='Psychology',
        skills=["Communication",'Behavior Analysis', 'Counselling', 'Research'],
        preReq=['FA', 'Pre-Medical'],
        careerField="Social Science",
        connections=['Sociology'],
        score=0
    ),
    'Sociology': Career(
        name='Sociology',
        skills=['Social Research', 'Cultural Awareness', 'Critical Thinking'],
        preReq=['ICOM', 'FA', 'Pre-Engineering', 'Pre-Medical', 'ICS'],
        careerField="Social Science",
        connections=['Psychology', 'Political Science'],
        score=0
    ),
    'Political Science': Career(
        name='Political Science',
        skills=["Politics",'Political Theory', 'Government Knowledge'],
        preReq=['ICOM', 'FA', 'Pre-Engineering', 'Pre-Medical', 'ICS'],
        careerField="Social Science",
        connections=['Sociology', 'Law'],
        score=0
    ),
    'Law': Career(
        name='Law',
        skills=["Argumentative",'Legal Research', 'Communication', 'Analysis'],
        preReq=['ICOM', 'FA', 'Pre-Engineering', 'Pre-Medical', 'ICS'],
        careerField="Social Science",
        connections=['Political Science'],
        score=0
    )
}


name = input("Enter your name: ")
education = ""
Program = input("You have done intermediate in:\n"
                    "a. Pre-medical\n"
                    "b. Pre-Engineering\n"
                    "c. ICS\n"
                    "d. FA\n")

if Program == 'a':
    education = "Pre-Medical"
elif Program == 'b':
    education = "Pre-Engineering"
elif Program == 'c':
    education = "ICS"
elif Program == 'd':
    education = "FA"


print("Please select your interests : \n")
Preferred_Skills = [
    "Technology", "Computer", "Medical", "Communication", "Chemistry", "Physics", "Mathematics",
    "Critical Thinking", "Python", "Statistics", "Documentation", "Critical Analysis", "Argumentative",
    "Politics", "Excel", "Data Visualization", "Network Security", "Cryptography", "Risk Management",
    "Business Acumen", "Project Management", "Medical Knowledge", "Patient Care", "Surgery", "Medication Management",
    "Physical Therapy", "Rehabilitation", "Writing", "Creativity", "SEO", "Adobe Photoshop", "Design Principles",
    "Research", "History", "Linguistics", "Language Theory", "Translation", "Literature Analysis", "Circuit Design",
    "Electrical Systems", "Thermodynamics", "Mechanics", "Structural Analysis", "Fiber Science", "Textile Machinery",
    "Chemical Process Design", "Material Science", "Programming", "Software Design", "Problem-Solving", "Algorithms",
    "Data Structures", "Networking", "System Administration", "Database Management", "Neural Networks", "Leadership",
    "Finance", "Management", "Market Analysis", "Digital Marketing", "Behavior Analysis", "Counseling", "Social Research",
    "Cultural Awareness", "Political Theory", "Legal Research", "Policy Analysis", "Government Knowledge", "Adaptability",
    "Resilience", "Networking & Relationship Building", "Innovation", "Deep Learning", "SQL", "Machine Learning",
    "UI/UX Design", "Business"
]


for i in range(len(Preferred_Skills)):
    print(f"{i + 1}. {Preferred_Skills[i]}")

print("Select the skills you prefer by typing the number(s) separated by commas (e.g., 1, 3, 5):\n")
selected = input("\nEnter your selections: ").split(',')
selected_skills = [Preferred_Skills[int(i.strip()) - 1] for i in selected if i.strip().isdigit() and 0 < int(i.strip()) <= len(Preferred_Skills)]

def BFS(Career):

    careersforStudentByEducation = []
    careersforStudentBySkills = []
    # defining the variables
    frontier = []
    visited = []
    # here we will be having the values based on the input
    initialState = 'Start'

    # add the first element into the frontier (which is kind of the queue in this case)
    frontier = [initialState]
    while len(frontier) != 0:
        # delete the first node from frontier and mark it as visited
        currentNode = frontier.pop(0)
        visited.append(currentNode)
        for child in Career[currentNode].connections:
            # the child which is not in both of the frontier and the visited node mark its parent in the graph and if the child is the goal return the solution
            if child not in visited and child not in frontier:
                frontier.append(child)
                if education in career_graph[child].preReq:
                    careersforStudentByEducation.append(child)



    print("Careers suggested to \n")
    for careers in careersforStudentByEducation:
        print(careers)

    return careersforStudentByEducation

# BFS for education
educationBasedSkills = BFS(career_graph)



def calculate_score(career, user_education, user_skills):
    # Education match score
    education_score = sum(1 for preReq in career.preReq if preReq.lower() in user_education.lower())

    # Skills match score
    interest_score = sum(1 for skill in career.skills if skill.lower() in (s.lower() for s in user_skills))

    # Combine education and interest scores with weights
    alpha = 0.6  # Education weight
    beta = 0.4  # Skill weight
    final_score = alpha * education_score + beta * interest_score
    return final_score


def best_first_search(career_graph, user_education, user_skills, start_career_name):
    # Use a priority queue (min-heap) to always explore the career with the highest heuristic score
    frontier = []
    visited = set()  # To avoid re-exploring careers

    # Initialize the frontier with all careers and calculate their scores
    for career_name, career in career_graph.items():
        # Skip the start node by checking if the career is the start career
        if career_name == start_career_name:
            continue  # Don't add the start node to the frontier

        score = calculate_score(career, user_education, user_skills)
        career.score = score  # Assign the score to the career
        heapq.heappush(frontier, (-score, career))  # Push negative score to create max-heap behavior

    # Get the top 3 careers based on their scores
    top_careers = []
    while frontier:
        # Pop the career with the highest score
        _, current_career = heapq.heappop(frontier)

        # If the career has not been visited, process it
        if current_career.name not in visited:
            visited.add(current_career.name)  # Mark this career as visited
            top_careers.append(current_career)

    top_n = 3
    top_careers_to_display = top_careers[:top_n]

    print("Top Careers:")
    for i, career in enumerate(top_careers_to_display, 1):
        print(f"{i}. Career: {career.name}, Score: {career.score}")

    return top_careers_to_display


start_career_name = 'Start'  # Name of the career that is the start node
best_career = best_first_search(career_graph, education, selected_skills, start_career_name)



# ---------------------------------------------------------------------------------------------------------
career_steps = {
    'Data Scientist': [
        'BS Data Science or Related Field',
        'Internships in Data Science',
        'Build a Portfolio with ML Projects',
        'Learn and Apply ML Algorithms',
        'Work on Real-World Data Science Projects'
    ],
    'Data Analyst': [
        'BS Data Science or Related Field',
        'Internships in Data Analysis',
        'Master SQL and Databases',
        'Develop Data Visualization Skills',
        'Create a Data Analysis Portfolio'
    ],
    'ML Engineer': [
        'BS Data Science or Computer Science',
        'Take Machine Learning Courses',
        'Work on ML Projects',
        'Participate in Kaggle Competitions',
        'Apply for ML Engineer Jobs'
    ],
    'AI Researcher': [
        'BS AI, Computer Science, or Related Field',
        'Pursue an MS or PhD in AI or Related Areas',
        'Gain Research Experience in AI',
        'Contribute to AI Research Publications',
        'Work on Cutting-Edge AI Projects'
    ],
    'Cybersecurity Specialist': [
        'BS Cybersecurity or Related Field',
        'Complete Internships in Cybersecurity',
        'Obtain Cybersecurity Certifications (e.g., CISSP)',
        'Work on Security Projects (Penetration Testing)',
        'Apply for Cybersecurity Specialist Jobs'
    ],
    'Doctor': [
        'Complete Pre-Medical Studies',
        'Enroll in Medical School',
        'Complete Clinical Rotations',
        'Pass Licensing Exams',
        'Start Residency Program'
    ],
    'Nurse': [
        'Complete Nursing School Program',
        'Pass Licensing Exam (NCLEX-RN)',
        'Gain Clinical Experience',
        'Work as a Registered Nurse',
        'Pursue Advanced Nursing Roles (Optional)'
    ],
    'Medical Researcher': [
        'Earn an MD or Medical Degree',
        'Gain Experience in Research Internships',
        'Pursue PhD (Optional) for Advanced Research Roles',
        'Contribute to Scientific Publications',
        'Continue Research in Medical Field'
    ],
    'Physiotherapist': [
        'Earn a BS in Physiotherapy',
        'Complete Clinical Training',
        'Pass Licensing Exam for Physiotherapists',
        'Begin Full-Time Employment as a Physiotherapist',
        'Specialize in Specific Physiotherapy Areas (Optional)'
    ],
    'Journalist': [
        'Earn a BS in Journalism or Communications',
        'Complete Internships with Media Outlets',
        'Build a Writing Portfolio',
        'Contribute to News Stories or Blogs',
        'Apply for Journalism Jobs or Freelance'
    ],
    'Content Writer': [
        'Earn a BS in English or Related Field',
        'Build a Writing Portfolio',
        'Gain Freelance Writing Experience',
        'Specialize in Content Marketing',
        'Look for Full-Time Content Writing Jobs'
    ],
    'Graphic Designer': [
        'Earn a BS in Graphic Design or Related Field',
        'Build a Design Portfolio',
        'Complete Internships in Design Studios',
        'Work on Freelance or Client Projects',
        'Apply for Graphic Design Jobs'
    ],
    'Literature Expert': [
        'Earn a BA in Literature or Related Field',
        'Complete a Master’s in Literature (Optional)',
        'Gain Writing Experience in Literary Fields',
        'Publish Articles, Stories, or Novels',
        'Look for Academic or Publishing Jobs'
    ],
    'Chemical Engineering': [
        'Earn a BS in Chemical Engineering',
        'Complete Internships in Chemical Engineering',
        'Obtain Relevant Certifications',
        'Gain Experience in Chemical Industry Projects',
        'Apply for Chemical Engineering Jobs'
    ],
    'Software Engineering': [
        'Earn a BS in Software Engineering or Computer Science',
        'Complete Internships in Software Development',
        'Build a Portfolio with Software Projects',
        'Master Programming Languages (Java, Python, etc.)',
        'Apply for Software Engineering Jobs'
    ],
    'Computer Science': [
        'Earn a BS in Computer Science',
        'Develop Programming Skills',
        'Work on Programming Projects',
        'Complete Internships in Software Development',
        'Apply for Software Development Jobs'
    ],
    'Information Technology': [
        'Earn a BS in Information Technology',
        'Complete Internships in IT Support',
        'Obtain IT Certifications (e.g., CompTIA, Cisco)',
        'Work on IT Projects (Network Management)',
        'Apply for IT Support or Network Administration Jobs'
    ],
    'Artificial Intelligence': [
        'Earn a BS in AI, Computer Science, or Related Field',
        'Pursue a Master’s in Artificial Intelligence',
        'Work on AI Projects (e.g., NLP, Computer Vision)',
        'Get Experience in AI Research or Industry',
        'Apply for AI Developer or Researcher Jobs'
    ],
    'Cybersecurity': [
        'Earn a BS in Cybersecurity or Related Field',
        'Complete Certifications (e.g., CEH, CISSP)',
        'Gain Experience in Penetration Testing',
        'Work on Security Projects and Threat Analysis',
        'Apply for Cybersecurity Specialist Jobs'
    ],
    'Electrical Engineering': [
        'Earn a BS in Electrical Engineering',
        'Complete Internships in Electrical Engineering',
        'Obtain Relevant Certifications',
        'Work on Electrical Design or Circuit Projects',
        'Apply for Electrical Engineer Jobs'
    ],
    'Mechanical Engineering': [
        'Earn a BS in Mechanical Engineering',
        'Complete Internships in Mechanical Engineering',
        'Obtain Relevant Certifications',
        'Work on Mechanical Design or CAD Projects',
        'Apply for Mechanical Engineer Jobs'
    ],
    'Civil Engineering': [
        'Earn a BS in Civil Engineering',
        'Complete Internships in Civil Engineering',
        'Obtain Certifications (e.g., FE, PE)',
        'Work on Civil Infrastructure Projects',
        'Apply for Civil Engineer Jobs'
    ],
    'Business Administration': [
        'Earn a BS in Business Administration',
        'Complete Internships in Business Management',
        'Develop Leadership and Communication Skills',
        'Pursue Full-Time Business Administration Roles',
        'Climb the Corporate Ladder (Manager/Director)'
    ],
    'Economics': [
        'Earn a BS in Economics',
        'Complete Internships in Finance or Economics',
        'Work on Research Projects or Data Analysis',
        'Apply for Economic Analyst Jobs',
        'Pursue Advanced Studies (MS/PhD) if Desired'
    ],
    'Marketing': [
        'Earn a BS in Marketing or Related Field',
        'Complete Internships in Marketing Agencies',
        'Build a Marketing Portfolio',
        'Gain Experience in Digital Marketing or SEO',
        'Apply for Marketing Specialist Jobs'
    ],
    'Business Analyst': [
        'Earn a BS in Business Administration or Related Field',
        'Complete Internships in Business Analysis',
        'Develop Business Analysis Skills (SWOT, Data Analysis)',
        'Work on Business Projects (Process Improvement)',
        'Apply for Business Analyst Jobs'
    ],
    'Psychology': [
        'Earn a BS in Psychology',
        'Complete Internships in Counseling or Therapy',
        'Pursue a Master’s in Psychology (Optional)',
        'Gain Experience in Clinical or Counseling Roles',
        'Apply for Psychology Jobs'
    ],
    'Sociology': [
        'Earn a BS in Sociology',
        'Complete Internships in Research or Social Services',
        'Work on Social Research Projects',
        'Apply for Social Work or Research Jobs',
        'Pursue Advanced Studies in Sociology (Optional)'
    ],
    'Political Science': [
        'Earn a BS in Political Science',
        'Complete Internships in Government or Policy',
        'Gain Research Experience in Politics',
        'Apply for Policy Analyst or Political Research Jobs',
        'Pursue Master’s in Political Science (Optional)'
    ],
    'Law': [
        'Earn a BS in Law or Related Field',
        'Complete Law School',
        'Pass the Bar Exam',
        'Start Practicing as a Lawyer',
        'Pursue Specialization in Law (Optional)'
    ]
}
# List of best career options (could be dynamically generated based on some criteria)
# best_careers = ['Data Scientist', 'Data Analyst', 'ML Engineer']

# Step 1: Display the best career options to the user
print("Here are the top 3 career options for you to explore:\n")

# Step 1: Print the best careers (use the career's name, not the object)
for index, career in enumerate(best_career, 1):
    print(f"{index}. {career.name} (Score: {career.score})")

# Step 2: Ask the user to choose one of the careers
while True:
    try:
        choice = int(input("\nPlease select the number of the career you want to explore (1-3): "))
        if 1 <= choice <= 3:
            selected_career = best_career[choice - 1]
            break
        else:
            print("Please select a valid number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

# Step 3: Retrieve and display the future steps for the selected career
print(f"\nFuture steps for becoming a {selected_career.name}:")
for step in career_steps[selected_career.name]:  # Using the career's name for lookup
    print(f"- {step}")

