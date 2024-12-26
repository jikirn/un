import time

# 게임 대사 및 흐름을 담당하는 클래스
class GameCharacter:
    def __init__(self, name, intro):
        self.name = name
        self.intro = intro

    def speak(self, text):
        print(f"{self.name}: {text}")
        time.sleep(1)

    def ask_question(self, question):
        print(f"\n{self.name}: {question}")
        choice = input("예 또는 아니요로 대답하세요: ").strip().lower()
        while choice not in ['예', '아니요']:
            print("잘못된 입력입니다. '예' 또는 '아니요'로 대답하세요.")
            choice = input("예 또는 아니요로 대답하세요: ").strip().lower()
        return choice == '예'

# 게임의 주요 흐름
def game():
    # 캐릭터 생성
    character = GameCharacter("각하", "당신은 런던파 인물을 이끌고 황량한 눈밭에 나와 있습니다.")

    # 게임 시작
    print("bong hwa에 오신 것을 환영합니다!\n")
    time.sleep(1)

    # 상황 설명
    character.speak(character.intro)
    
    # 챕터 1: 정착지
    character.speak("앞에 눈이 녹아있는 공터가 있어! 이곳에 정착할까??")
    if character.ask_question("이곳에 정착할까요?"):
        character.speak("잘 정착했어! 다행히 안전하게 거점을 만들었어.")
        outcome1 = "불만이 없다!"
    else:
        character.speak("더 나아가다가 정착을 하긴 했지만 불만이 늘었어.")
        outcome1 = "불만이 늘었다!"
    
    # 챕터 2: 노동자
    character.speak("이제 자원을 모으기 위해 일꾼을 모아야해! 어떻게 할까?")
    if character.ask_question("어른만 노동에 종사하게 한다?"):
        character.speak("어른들만 노동을 하고 있어! 자원이 약간 부족하지만 무사히 넘겼어.")
        outcome2 = "불만이 잦아들었다!"
    else:
        character.speak("아이들까지 노동에 종사하게 되었어! 불만이 늘었어.")
        outcome2 = "불만이 늘었다!"
    
    # 잽터 3: 외교
    character.speak("이제 나라가 안정되었어! 노국과 교류할까?")
    if character.ask_question("노국과 교류할까요?"):
        character.speak("협상이 잘 되어 자원이 풍족해졌어.")
        outcome3 = "불만이 줄어들었다!"
    else:
        character.speak("교류를 하지 못해 자원이 부족해졌어! 국민의 불만이 증가했어.")
        outcome3 = "불만이 증가했다!"

    # 챕터 4: 자연재해
    character.speak("쓰나미가 오고 있어! 어떻게 대응할까?")
    if character.ask_question("제방을 쌓아 쓰나미를 막을까요?"):
        character.speak("제방이 쓰나미에 무너져서 더 큰 피해를 입었어!")
        outcome4 = "불만이 증가했다!"
    else:
        character.speak("피해를 입긴 했지만, 빠른 대처로 복구에 성공했어.")
        outcome4 = "불만이 줄어들었다"

    # 게임의 결말
    print("\n--- 게임 종료 ---")
    
    # 모든 결과를 출력
    print(f"결과: {outcome1}, {outcome2}, {outcome3}, {outcome4}")
    
    if outcome1 == "불만이 없다!" and outcome2 == "불만이 잦아들었다!" and outcome3 == "불만이 줄어들었다!" and outcome4 == "불만이 줄어들었다":
        print(f"{character.name}이 확고한 지지층을 확보했어.")
    else:
        print(f"{character.name}은 불안정한 상황에 놓이게 되었어.")
    
# 게임 실행
if __name__ == "__main__":
    game()