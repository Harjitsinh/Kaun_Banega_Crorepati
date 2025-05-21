import threading
import queue
import time

questions = [
    ["Who is Elon Musk?", "WWE Wrestler", "Plumber", "Entrepreneur", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

dhanraashi = [10, 10000, 25000, 50000, 100000, 2500000, 5000000, 7500000, 10000000, 35000000, 70000000]

def timed_input(prompt, timeout):
    q = queue.Queue()

    def get_input():
        q.put(input(prompt))

    t = threading.Thread(target=get_input)
    t.daemon = True
    t.start()

    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        return None

i = 0
for question in questions:
    print(f"\nQ{i+1}. {question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    print("⏳ Aapke paas 45 seconds hain uttar dene ke liye...")

    answer = timed_input("Meri Taraf matt dekhiye uttar bataiye. 1 for a, 2 for b, 3 for c, 4 for d: ", 45)

    if answer is None:
        print("⏰ Samay samapt! Aapne samay par jawab nahi diya.")
        if i == 0:
            print("Dekh liya laparvahi ka anjaam.")
        print("Iss taraf..")
        break

    try:
        a = int(answer)
        if question[5] == a:
            print("✅ Sahi javab!")
            print(f"Aapne jeete hain ₹{dhanraashi[i]}")
            i += 1
        else:
            print(f"❌ Galat javab! Sahi uttar tha option {question[5]}")
            if i == 0:
                print("Dekh liya laparvahi ka anjaam.")
            print("Iss taraf..")
            break
    except ValueError:
        print("⚠️ Kripya sahi sankhya dalein (1 to 4).")
        break

if i == len(questions):
    print("\n🎉 Saaaat crore! Kya karenge aap itni dhanraashi ka?")
    player = input("Bataiye apne vichaar: ")
    print(f"Bahut badhiya! Aapka yeh plan sunke acha laga: \"{player}\"")
