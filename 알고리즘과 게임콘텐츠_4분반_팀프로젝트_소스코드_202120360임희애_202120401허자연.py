import time
num=0
print('<<우당당탕! 요리사!!>>')
print()
time.sleep(3)
print('npc: 안녕! 너의 이름은 뭐니?')
print()
time.sleep(2)
name=str(input('이름을 입력하시오(단, 숫자,기호는 제외):'))
print()
print('npc: %s! 반가워! 이 요리게임은 5라운드로 구성돼있어!'%(name))
print()
time.sleep(3)
print('npc: 게임  실패시 -5점, 성공시 +25점이 누적되고, 게임이 끝나면 너의 요리 점수와 등급을 볼 수 있어!')
print()
time.sleep(5)
print('npc: 그럼 행운을 빌게!')
print()
time.sleep(3)
print('%s: 아~! 상쾌한 아침이다~'%(name))
print()
time.sleep(2)
print('%s: 오늘은 손님이 얼마나 올까?'%(name))
print()
time.sleep(2)
print('%s: 오늘은 어제보다 더 맛있게 대접해야지~! 나는 요리사니깐!!'%(name))
print()
print()
time.sleep(2.5)
print('< 1라운드: 해장라면 > 난이도★☆☆☆')
print()
time.sleep(2.5)
print('화장한 햇살과 함께 첫번째 손님이 입장했습니다.')
print()
time.sleep(2.5)
print('띠-링')
print()
time.sleep(1.5)
print('손님: 아~ 어제 술을 과음했더니 라면이 땡기네.. 해장라면 하나 주세요~')
print()
time.sleep(2.5)
print('%s: 해장라면을 만들어보자. 단, 순서를 잘 지키야 한다.'%(name))
print()
time.sleep(2.5)
while True:
      order1 = str(input('육수, 분말 중 가장 먼저 넣어야 하는 것은?:'))
      if order1 == '육수':
       num=num+5
       print('정답! 잘했어!',num,'점')
       break
      else:
       num=num-5
       print('그 레시피는 틀렸어..',num,'점')
       time.sleep(1)
time.sleep(2)
while True:
      print()
      order2 = str(input('분말,달걀 중 가장 먼저 넣어야 하는 것은?:'))
      if order2 == '분말':
       num=num+5
       print('정답! 잘했어!',num,'점')
       break
      else:
       num=num-5
       print('그 레시피는 틀렸어..',num,'점')
       time.sleep(1)
time.sleep(2)
while True:
      print()
      order3 = str(input('파, 라면사리 중 가장 먼저 넣어야 하는 것은?:'))
      if order3 == '라면사리':
       num=num+5
       print('정답! 잘했어!',num,'점')
       break
      else:
       num=num-5
       print('그 레시피는 틀렸어..',num,'점')
       time.sleep(1)
time.sleep(2)
while True:
      print()
      order4 = str(input('치즈, 계란 중 가장 먼저 넣어야 하는 것은?:'))
      if order4 == '계란':
       num=num+5
       print('정답! 잘했어!',num,'점')
       break
      else:
       num=num-5
       print('그 레시피는 틀렸어..',num,'점')
       time.sleep(1)
time.sleep(2)
print()
print()
print('< 2라운드: 결정장애 손님을 위해 메뉴를 추천해주자! > 난이도★★☆☆')
print()
time.sleep(2)
print('손님:흠...고민이군...')
print()
time.sleep(2)
print('%s:주문하시겠어요?'%(name))
print()
time.sleep(2)
print('손님: 요리사양반. 메뉴를 못고르겠네. 너무 어려워..')
print()
time.sleep(2)
print('%s:아 그러시면 제가 메뉴를 추천해드릴까요?'%(name))
print()
time.sleep(2)
print('손님: 흠…자네 날 만족시킬 수 있겠나?')
print()
time.sleep(2)
print('%s:당연하죠! 전 요리사니깐요!'%(name))
print()
time.sleep(2)
print('손님: 그럼  떡볶이, 짜장면, 삼겹살을 주문하고 싶은데 이 3가지 음식에 어울릴 만한 궁합음식을 추천해주겠나?')
print()
time.sleep(2)
print('%s:네! 저만 믿으세요!'%(name))
print()
time.sleep(2)
print('결정장애 손님을 위해 메뉴를 추천해주자!')
print()
time.sleep(2)
print('주의사항: 입력할 때 단어사이에는 ,(컴마)를 넣고 뛰어쓰기는 하지 마시오')
print()
time.sleep(2)
foods={'떡볶이':'순대','짜장면':'탕수육','삼겹살':'상추'}
while True:
  myfood=input(str(list(foods.keys()))+'중 손님이 말한 메뉴와 궁합음식은?:')
  if myfood=='순대,탕수육,상추':
    num=num+10
    print()
    print('정답!',num,'점')
    break
  else:
    num=num-5
    print()
    print('그 레시피는 틀렸어..',num,'점')
    time.sleep(1)
print()
time.sleep(2)
print('npc:좋았어~다음단계로~')
print()
print()
time.sleep(2)
print('< 3라운드: 장인 만두 > 난이도★★★☆')
print()
time.sleep(2)
print('%s: 벌써 저녁이 되어가는구나…'%(name))
print()
time.sleep(2)
print('띠-링')
print()
time.sleep(2)
print('%s: 어서오...헉...! 당신은...!'%(name))
print()
time.sleep(2)
print('50년전통만두요리사: 음..허름하군..')
print()
time.sleep(2)
print('%s: 당신은 50년동안 만두만 빚었다는 그 전설의…!'%(name))
print()
time.sleep(2)
print('50년 전통만두 요리사: 됐고! 요리부터 가져오지. 메뉴는 만두! 날 실망시키지 않는 게 좋을거야.')
print()
time.sleep(2)
print('%s: 넵..!'%(name))
print()
time.sleep(2)
print('최고 조합의  만두를 만들어 대접하자!')
print()
time.sleep(2)
print('주의사항: 입력할 때 단어사이에는 ,(컴마)를 넣고 뛰어쓰기는 하지 마시오')
print()
time.sleep(2)
print ('반죽 재료: 돼지고기, 두부, 양파, 배추, 계란, 참기름, 매운고추, 마늘, 치즈, 대파, 고추장')
time.sleep(2)
while True:
      order5 = str(input('반죽 재료 6개를 골라 입력하시오:'))
      if order5 == '돼지고기,두부,양파,계란,마늘,대파':
       num=num+15
       print()
       print('정답!',num,'점')
       break
      else:
       num=num-5
       print()
       print('그 레시피는 틀렸어..',num,'점')
time.sleep(1)
print()
print ('만두피 반죽: 쌀가루, 밀가루, 콩가루, 물, 쥬스, 와인')
while True:
      order5 = str(input('반죽 재료 2개를 골라 입력하시오:'))
      if order5 == '밀가루,물':
       num=num+15
       print()
       print('정답!',num,'점')
       break
      else:
       num=num-5
       print()
       print('그 레시피는 틀렸어..',num,'점')
time.sleep(1)
print()
print ('조리: 긴발달 모양-굽기, 또아리 모양-찌기, 쭈그리 모양-삶기')
while True:
      order5 = str(input('조리 조합 1개를 골라 입력하시오:'))
      if order5 == '긴발달 모양-굽기':
       num=num+15
       print()
       print('정답! 최고의 레시피야!',num,'점')
       break
      else:
       num=num-5
       print()
       print('그 레시피는 틀렸어..',num,'점')
print()
print()
time.sleep(2)
print('< 4라운드: 최고의  튀김 > 난이도★★★★')
print()
time.sleep(2)
print('%s: 벌써 저녁이네! 술 마시러 많이들 오시겠네!'%(name))
print()
time.sleep(2)
print('띠링')
print()
time.sleep(2)
print('사회초년생: 하….')
print()
time.sleep(2)
print('%s: 주문 도와드릴까요?'%(name))
print()
time.sleep(2)
print('사회초년생: 치킨이랑 맥주 주세요..')
print()
time.sleep(2)
print('%s: 기분이 안 좋아 보이신다…최고의 튀김으로 손님을 기쁘게 해드리자!'%(name))
print()
time.sleep(2)
while True:
    print('바삭한 튀김을 만들기 위해 정확히 10초뒤에 꺼내자! (*단, 소수점은 무시하시오) ')
    input('엔터를 누르고 10초를 셉니다.')
    start=time.time()
    print()
    input('10초 후에 다시 엔터를 누릅니다.')
    end=time.time()
    print()
    time.sleep(1)
    et=end-start
    print('실제시간:',et,'초')
    print()
    time.sleep(2)
    if et>=10 and et<11:
       num=num+25
       print('완벽한 튀김이야!',num,'점')
       break
    else:
       num=num-5
       print('실패야….',num,'점')
       print()
time.sleep(2)
print()
print()
print('%s: 후.. 끝난건가..'%(name))
print()
time.sleep(2)
print('npc: 수고했어!%s!'%(name))
print()
time.sleep(1)
print('npc: 총점은',num,'점!')
print()
if num == 100:
    print('A+ 만점이야!! 훌륭해! 최고의 요리사인걸?!')
elif num >= 90:
    print('너의 요리실력은 A권이야! 아주 잘했어! 조금만 더 노력하면 최고의 요리사가 되겠는걸?')
elif num >= 80:
    print('너의 요리실력은 B권이야! 잘했어! 조금만 더 노력하면 최고의 요리사가 되겠는걸?')
elif num >= 70:
    print('너의 요리실력은 C권이야! 아쉽다... 좀 더 노력해보자!')
elif num >= 60:
    print('너의 요리실력은 D권이야! 아쉽다... 좀 더 노력해보자!')
else:
    print('너의 요리실력은 F권이야! 아쉽다... 좀 더 노력해보자!')
time.sleep(2)
print()
print('npc: 새로운 요리의 발견이 새로운 별의 발견보다 인간을 더 행복하게 만든다.라는 말이있지!')
print()
time.sleep(3.5)
print('npc: 너에게 요리가 그런 의미였으면 좋겠어!!')
print()
time.sleep(2.5)
print('< END >')
