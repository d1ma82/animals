"""
    Модуль примера реализации алгоритма 'дерева решений'
    Компьютер учиться отгадывать животных.
"""
class TreeElement:
        
    def __init__(self, question="", answear="", p_yes=None, p_no=None):
        self.question = question
        self.answear = answear
        self.p_yes = p_yes
        self.p_no = p_no



def yes():
    return input() == 'y'


def next_play():
    print("Continue?")
    return yes()

def create_next(current_answear:str):
        result = TreeElement();
        result.answear = input("OK! Who is it? ")
        format_str = "What the difference between {} and {} ?"
        print(format_str.format(result.answear, current_answear))
        result.question = input() + "?"
        return result


def main():
    init = TreeElement("it catch mice?", "cat", None, None)
    
    while True: 
        current = init
        print("Think an animal, and I will try to guess by asking leading questions.")
        while True:
            print(current.question)
            if yes():
                print("This is " + current.answear + ". Guess?")
                if yes():
                    print("I am win!!!")
                    break  # Прерываем если выиграли
                else:
                    if current.p_yes == None:
                        current.p_yes = create_next(current.answear)
                        break  # Прерываем если закончились наводящие вопросы
                    else:
                        current = current.p_yes
                    
            else:
                if current.p_no == None:
                    current.p_no = create_next(current.answear)
                    break  # Прерываем если закончились наводящие вопросы
                else: 
                    current = current.p_no
                    
        if not next_play(): break
                
main()           
