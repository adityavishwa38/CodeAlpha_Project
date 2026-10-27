import random
from datetime import datetime
import json
import os

#new question and answer will saved
MEMORY_FILE = "chatbot_memory.json"

#remember the user name
user_name = ""

#Load saved question and answer 
def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE,"r",encoding="utf-8")as file:
                data=json.load(file)

                if isinstance(data,dict):
                    return data

        except (json.JSONDecodeError,OSError):
            print("Warning!! Could not load chatbot memory.")
    return {}

#save question and answer 
def save_memory(memory):
    with open(MEMORY_FILE,"w",encoding="utf-8") as file:
        json.dump(memory,file,indent=4,ensure_ascii=False)
        

#load memory when the program strat
memory = load_memory()
    
#chatbot responce function
def chatBot_responce(user):
    
    user = user.lower().strip()
    
    if user in memory:
        return memory[user]
    
    if user in ["hello", "hi", "hii","hiii", "hey", "hlo", "good morning", "good afternoon", "good evening"]:
        return random.choice([ "Hello! Welcome to my chatbot.", 
                              "Hi! How can I help you today?", 
                              "Hey! Nice to see you!", 
                              "Hello there! What would you like to know?" 
                              ])
        
    elif user in ["how are you",
                  "how are you?"
                  ]:
        return "I'm fine thanks! how can i help you?"
    
    elif user in [ "what is your name",
                  "tell me your name", 
                  "whats you name", 
                  "what's your name", 
                  "your name?", 
                  "your name" 
                  ]:
        return "Ohh..! I'm python bot."
    
    elif user in ["what can you do",
                  "help",
                  "what can you do?"
                  ]:
        return "I can respond to greeting and simple queation. "
    
    elif user in ["thanks",
                  "thank you",
                  "thank",
                  "dhanyvad.",
                  "thanks"
                  ]:
        return random.choice([ "You're welcome!", 
                              "Happy to help!", 
                              "Anytime!😊" 
                              ])
    
    elif user in ["what is python", 
                  "define python"
                  ]: 
        return "Python is a popular programming language used in AI, web development, and data analysis."
    
    elif user in ["who created you", 
                  "who is your creator"
                  ]: 
        return "I was created by Aditya using Python."
    
    elif "joke"in user or "jokes"in user:
        return random.choice(["Why do programmers prefer dark mode? Because light attracts bugs!", 
                              "Why was the computer cold? Because it left its Windows open!", 
                              "Why do Python programmers wear glasses? Because they cannot C!",
                              "Why did the programmer quit his job?\nBecause he didn't get arrays! ", 
                              "Teacher: Who invented the telephone?\nStudent: Alexander Graham Bell.\nTeacher: Correct! Who invented the mobile phone?\nStudent: His son, Mobile Graham Bell! ", 
                              "Why don't programmers like nature?\nIt has too many bugs! ", "What did one wall say to the other wall?\nI'll meet you at the corner! ", 
                              "Why was the student sitting on his clock?\nBecause he wanted to be on time! ", "What do you call fake spaghetti?\nAn impasta! ", 
                              "Why did the bicycle fall over?\nBecause it was two-tired! ", "What did the zero say to the eight?\nNice belt! ", 
                              "Why did the computer get glasses?\nTo improve its website! ", 
                              "What do you call a bear with no teeth?\nA gummy bear! "
                              ])
    
    elif "motivation" in user or "motivate me" in user :
        return random.choice([ "Believe in yourself. Every expert was once a beginner.", 
                       "Small steps every day lead to big achievements.", 
                       "Never give up. Great things take time.",
                       "One day, your hard work will become your success story.", 
                       "Believe in yourself, even when nobody else does.", 
                       "Failure is not the opposite of success. It's part of success.", 
                       "Small progress every day leads to big results.", 
                       "Be stronger than your excuses and bigger than your fears.", 
                       "Every morning is another chance to become a better version of yourself.", 
                       "Pressure creates diamonds. Difficult times can make you stronger."
                       ])
    
    elif "date" in user or "time" in user:
        now = datetime.now()
        return (f"Today's date is {now:%d-%m-%Y} time is {now:%I:%M:%S %p}.")
    
    else:
        return None

def main():
    print("="*35)
    print("    .. Welcome to python bot..")
    print("="*35)
    print("     Type 'bye' to exit the chatbot\n")

    while True:
        
        try:
            
            user = input("You: ").strip()
            
            if user.lower() in ["by","bye","byee","goodbye","good bye","exit"]:
                print("\n\tWelcome..!! Have a great day ADITYA..\n")
                break
            
            responce = chatBot_responce(user)
            
            if responce is not None:
                print("Bot:",responce,"\n")
                
            else:
                #ask user to teach the chatbot
                print("Bot: I don't know the answer to that question yet.\n")
                
                teach = input("Would you like to teach me the answer? (yes/no): ").strip().lower()
                
                if teach in ["yes","y","Yes","Y"]:
                    answer = input("Enter the answer I should remember: ").strip()
                    
                    if answer:
                        memory[user.lower().strip()] = answer
                        save_memory(memory)
                        
                        print("Bot: Thank you! I have learned this answer.")
                        print("Bot:",answer,"\n")

                    else:
                        print("Bot: Empty answers cannot be save.\n")
                    
                else:
                    print("Bot: Okay! You can teach me next time.\n")
                    
        except KeyboardInterrupt:
            print("\nBot: Chat ended. See you next time!")
            break
        
        except OSError as error:
            print("Bot: A file error occurred:",error)

        
if __name__=="__main__":
    main()