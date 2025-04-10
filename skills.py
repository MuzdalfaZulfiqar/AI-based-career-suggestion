# Module for skill based recommendation
#
# def calculate_score(career, education, interests):
#     # Education match score
#     education_score = 0
#     for preReq in career.preReq:
#         # print(preReq)
#         if preReq in education:  # Call lower() on the preReq string
#             education_score += 1  # Increase score for matching education
#
#     # Interest match score
#     interest_score = 0
#     for skill in career.skills:
#         if skill in interests:
#             interest_score += 1  # Increase score for matching skills
#
#     # Combine education and interest scores with weights
#     alpha = 0.6  # Education weight
#     beta = 0.4  # Interest weight
#     final_score = alpha * education_score + beta * interest_score
#     return final_score
#
#
# def best_first_search(user_education, user_skills, career_graph):
#     # Priority queue to explore nodes with best heuristic score first
#     frontier = []
#     heapq.heappush(frontier, (0, 'Start'))  # Starting point (could be customized)
#     explored = set()
#     career_scores = {}
#
#     while frontier:
#         _, current_career_name = heapq.heappop(frontier)
#         if current_career_name in explored:
#             continue
#         explored.add(current_career_name)
#
#         current_career = career_graph.get(current_career_name)
#         if not current_career:
#             continue
#
#         # Calculate the score based on education and skills (user interests)
#         score = calculate_score(current_career, user_education, user_skills)
#         career_scores[current_career_name] = score
#
#         # Explore connected careers and add them to frontier
#         for connection in current_career.connections:
#             if connection not in explored:
#                 heapq.heappush(frontier, (0, connection))
#
#     # Sort careers based on the score (descending)
#     sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)
#
#     # Filter top recommendations (for example, top 3)
#     # top_careers = sorted_careers[:3]
#     print("Top Career Recommendations:")
#     for career_name, score in sorted_careers:
#         print(f"{career_name}: Heuristic Score = {score}")
#
#
# best_first_search(educationBasedSkills, selected, career_graph)

# def calculate_heuristic(career, educationInput, skills):
#     # Education match score (how many preReq match)
#     education_score = sum(1 for preReq in career.preReq if preReq.lower() in educationInput.lower())
#
#     # Skills match score (how many skills match)
#     skill_score = sum(1 for skill in career.skills if skill.lower() in skills.lower())
#
#     # Weighted sum for heuristic score (can adjust alpha and beta for importance of each factor)
#     alpha = 0.6  # Education weight
#     beta = 0.4  # Skills weight
#     return alpha * education_score + beta * skill_score
#
#
# # Best First Search function
# def best_first_search(user_education, user_skills, career_graph):
#     # Start BFS with education-based careers (no heuristic yet)
#     matched_careers = []
#     for career_name, career in career_graph.items():
#         # Calculate heuristic score for each career
#         score = calculate_heuristic(career, user_education, user_skills)
#         matched_careers.append((career_name, score))
#
#     # Sort careers by the highest heuristic score
#     matched_careers.sort(key=lambda x: x[1], reverse=True)
#
#     # Recommend the career with the highest score
#     best_career = matched_careers[0]
#     return best_career
# recommended_career = best_first_search(education,selected, career_graph)
#
# print(f"Recommended Career: {recommended_career[0]} with score {recommended_career[1]:.2f}")




# def calculate_score(career, user_education, user_skills):
#     # Education match score
#     education_score = 0
#     for preReq in career.preReq:
#         if preReq.lower() in user_education.lower():
#             education_score += 1  # Increase score for matching education
#
#     # Skills match score
#     interest_score = 0
#     for skill in career.skills:
#         if skill.lower() in user_skills.lower():
#             interest_score += 1  # Increase score for matching skills
#
#     # Combine education and interest scores with weights
#     alpha = 0.6  # Education weight
#     beta = 0.4  # Skill weight
#     final_score = alpha * education_score + beta * interest_score
#     return final_score
#
#
# def best_first_search(career_graph, user_education, user_skills):
#     # Use a priority queue (min-heap) to always explore the career with the highest heuristic score
#     frontier = []
#     visited = set()  # To avoid re-exploring careers
#
#     # Initialize the frontier with all careers and calculate their scores
#     for career_name, career in career_graph.items():
#         score = calculate_score(career, user_education, user_skills)
#         career.score = score  # Assign the score to the career
#         heapq.heappush(frontier, (-score, career))  # Use negative score for max-heap
#
#     # Process the careers based on their scores
#     while frontier:
#         # Get the career with the highest score
#         _, current_career = heapq.heappop(frontier)
#
#         # If the career has already been visited, skip it
#         if current_career.name in visited:
#             continue
#
#         visited.add(current_career.name)  # Mark career as visited
#
#         # Here, we simply return the first career in the priority queue (highest score)
#         print(f"Career: {current_career.name}, Score: {current_career.score}")
#
#     # Optionally, return the best career (the one with the highest score)
#     best_career = max(career_graph.values(), key=lambda c: c.score)
#     print(f"Best Career Recommendation: {best_career.name} with score: {best_career.score}")
#     return best_career


# # Example user input
# user_education = "Pre Engineering"
# user_skills = "Programming, Machine Learning, Data Structures"
