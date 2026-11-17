questions = {
    "What is the capital of France?": {
        "choices": ["A) Lagos", "B) Paris", "C) London", "D) Abuja"],
        "answer": "B"
    },
    "What is 5 + 3?": {
        "choices": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C"
    },
    "Which language is this?": {
        "choices": ["A) Java", "B) C++", "C) Python", "D) Ruby"],
        "answer": "C"
    },
    "How many days in a week?": {
        "choices": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    },
    "What color is the sky?": {
        "choices": ["A) Red", "B) Blue", "C) Green", "D) Yellow"],
        "answer": "B"
    }
}

score = 0
correct_list = []
wrong_list = []

for questions, data in questions.items():
    print (f"\n{questions}")
    for choice in data ["choices"]:
       print (f"{choice}")

    while True:
       answer = input("Enter your answer (A/B/C/D): ").strip().upper()
       if answer in ("A", "B", "C", "D"):
            break
       print ("Invalid Choice..Please enter A, B, C or D")

    if answer == data["answer"]:
        score += 1
        correct_list.append(questions)
        print (f"\n Correct!")
    else:
        wrong_list.append((questions, data["answer"]))
        print (f"\n Wrong answer...The correct answer:{data["answer"]}")
    
total = len(correct_list + wrong_list)
print ("\n" + "=" * 40)
print (f"\n Final Score: {score}/{total} ({score *100 //total}%)")
print ("=" * 40)


if correct_list:
    print (f"\n Correct")
    for q in correct_list:
        print (f"  -{q}" )

if wrong_list:
    print (f"\n Wrong")
    for q, ans in wrong_list:
        print (f" - {q} (correct: {ans})")
 
    
   

   
   
    


      
       


    



              
              
              
              
              
              
              
            
    
    