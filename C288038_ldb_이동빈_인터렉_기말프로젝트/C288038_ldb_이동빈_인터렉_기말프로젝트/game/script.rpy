# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define c = Character('최승빈', color ="#000000")
define ly= Character('이영숙', color = "#000000")
define ls= Character('이승환', color ="#000000")
define tm= Character('과장',color="#000000")
define pl= Character('김수아',color= "#000000")
define pl2= Character('jessy',color= "#000000")
define gr= Character('박나영', color="#000000")
define pr= Character('임성준',color="#000000")
define me= Character('약사', color="#000000")
define nw= Character('황젠슨',color="#000000")
define q= Character('퀘스트 창',color="#000000")
define qu= Character('???',color="#000000")
define dc= Character('통화하는 사람',color="#000000")
define nei=Character('이웃집 아줌마',color="#000000")
# define narrator = Character(None,kind=nvl)

define right2=Position(xalign=0.9,yaligh=0.2)
image bg_room = "bg_room.jpg"
image black = "Black.png"
image Light = "light.jpg"
image table = "table.jpg"
image man = "black man.png"
image c_tm = "gwa.png"
image quest = "Questbook.png"
image c_c = "seung.png"
image project = "NightMare.png"
image bg_pl = "ki.jpg"
image planer ="kiki.png"
image maraa ="mara.jpg"
image maraalose ="tteok.png"
image tanghuru = "tangtang.jpg"
image c_c_c = "c_c_c.png"
image gachaaa= "gachaa.jpg"
image starr= "star.jpg"
image ssrr= "ssr.jpg"
image c_nw = "jensen.png"
image officetable= "office.jpg"
image home ="billa.jpg"
image c_ly = "ly.png"
image c_nei = "nei.png"
image c_villain = "villain.png"
image tangbi = "tangbi.jpg"
image bg_news = "news.jpg"
image c_vio = "vio.jpg"
image topp ="top.png"
image gt = "nm.jpg"
# 여기에서부터 게임이 시작합니다.
label start:

    ly "아들 내려와서 밥먹어~"
    qu "아 제가 알아서 먹을게요"
    ly "(에휴, 방에서 뭐하는건지 취직을 할란가)"
    scene bg_room
    play music "audio/1st scene.Mp3"
    qu "나는 32세 겜창 백수이다. 엄마한테는 취직준비라는 명분하에 방에서 게임을 즐기고 있다."
    dc "승빈씨 오늘 나올 신작 겜 할거죠?"
    show c_c_c at left
    c "당연하죠 제가 몇년을 기대한 작품인걸요"
    "그렇다 오늘은 내가 기대한작품이 나온날이다."
    # nvl clear

    c "하 게임 드릅게 비싸네 뭔 8만원이나 해"
    c "오픈런 뛰어볼까"
    "서버에 사람이 많아 대기열에 들어갑니다"
    "대기열 9999"
    c "뭐? 대기열? 그리고 9999는 뭐야"
    c "아니, 하..."
    c "그래 기대작이니 기다려 보자.."
    c "기다리는 동안 유저들 평판이나 보자"
    "익명A: 망겜도 이런 망겜도 없다."
    "익명B: 대기열때문에 안함."
    "익명C: 돈이 아깝다"
    c "뭐야 다들 평판이 왜이래"
    c "대기열 갓겜 아니었어?"
    "대기열: 0"
    # nvl clear
    c "후..드디어 하겠네"
    "응답 없음(로딩 중)"
    # nvl clear
    c "뭐? 게임 튕겼다고? 몇 시간을 기다렸는데!!!!"
    c "그래, 다시 접속해 보자."
    "대기열: 9999"
    # nvl clear
    c "하.... 이런 X망겜을 봤나..."
    c "내가 만들어도 더 잘 만들겠다."
    stop music fadeout 1.5
    play music "audio/Death.ogg"
    "알겠다."
    "."
    "."
    "."
    "갑자기 엄청난 피로가 몰려와 눈이 감긴다."
    stop music fadeout 1.0
    scene black
    # nvl clear
    qu "으아 뭐야.. 최근에 너무 밤새 게임 했나.."
    scene Light 
    "밝은 모니터 빛에 의해 감긴 눈을 조금식 뜨기 시작한다."  
    scene table
    play music "audio/company sound.Mp3" 
    show man at left
    qu "뭐야. 이건 내 모니터가 아닌데??"
    qu "설마 나 전생한거야???"
    # nvl clear

    "전생한거라면 국룰 멘트는 외쳐야지"
    menu:
        '스테이터스 오픈':
            qu "「스테이터스 오픈」"
        '상태창 열기':
            qu "「상태창 열기」"

    "아무 일도 안일어났다."
    "그제서야 옆에 사람이 있단걸 알았다."
    show c_tm at right
    tm "승환씨 개소리하지말고 내일까지 끝내놔"
    "신기하게도 나한테 말한 사람이 과장이란걸 알았다."
    hide c_tm
    hide man
    "팀장이 간 뒤 공중에 홀로그램 화면이 보였다."
    play sound "audio/dilong.Mp3"
    show quest at right2
    stop sound fadeout 0.5
    show c_c at left
    ls "진짜로 나 전생한거야?"
    "홀로그램 화면에는 Quest라고 적혀 있었다."
    "MainQuest: 게임을 완성시키시오.(난이도: 극악)"
    "남은 기간: 3주, 패널티: ???"
    hide quest

    "그렇다. 난 환생한 것이다. 이 몸의 주인은 32세, 대기업에 취직했다가 사고를 쳐 업계에서 블랙리스트 취급당한다."
    "그렇게 중소게임회사에 들어가, 지금 일하고 있다."
    show project at right2
    "Project: NightMare"
    "맡은 업무: 이틀 후까지 게임 기획서, 캐릭터 디자인, 시스템 흐름도 짜오기."
    hide project
    ls "하... x바 이거 완전 블랙기업이네, 이걸 2일만에 어떻게 완성해"
    ls "근데 패널티를 모르니깐 하긴 해야지.."
    hide c_c
    "일단 팀원들한테 가야겠다."
    "기억 상 팀원들은 정상이 아닌걸로 알고 있는데...."
    
    menu:
        '기획자한테 가기':
            jump gopl
            stop music fadeout 1.0
        
        '그래픽한테 가기':
            jump gopl

        '프로그래머한테 가기':
            jump gopl
    
    return

label gopl:
    play music "audio/tender.Mp3"
    scene bg_pl
    show c_c at left
    ls "그래 일단 기획자한테 가자."
    ls "수아님 저번에 부탁했던 기획 받으러 왔어요."
    show planer at right
    pl "잠시만요 수아 말고 Jessy라고 불러주세요."
    "그렇다 기획자는 신입 MZ였다."
    ls "아...네, 제시님 기획서 주세요."
    pl2 "okay, 자 여기요."
    "기획서를 훑어본다."
    " 오픈월드 MMORPG 실제와 같은 그래픽의 AR/VR 지원하는 게임"
    ls "우리가 이걸 구현할 수 있을거라 생각하고 적은건가?"
    hide planer

    "갑자기 화면에 퀘스트 창이 떴다."
    show quest at truecenter
    q "SubQuest: 기획자를 공략하시오. (난이도: 중)"
    q "보상: ??? 패널티: ??? 남은시간: 3시간."
    ls "뭐 공략하라고?"
    menu:
        '수락':
            stop music fadeout 1.0
            jump pl_ac
            hide quest
            

label pl_ac:
    "호감도: [affection_pl]"

    menu:
        '화낸다':
            $affection_pl-= 30
            jump pl_angry
        '담담하게 말한다':
            jump pl_dam

label pl_angry:
    play music "audio/scare.Mp3"
    show c_c at left
    ls "저기 수아씨, 아니 제시씨 지금 장난쳐요? 이딴 걸 기획서라고 적은거에요?"
    "호감도: [affection_pl]"
    show planer at right
    pl2 "왜요? 완벽한 기획서인데..."
    ls "(하... 이거 답 없네, 호감도가 내려갔어.)"
    stop music fadeout 1.0
    ls "곧 점심시간인데 뭐 드실래요?"
    pl2 "그래요..."
    hide c_c
    hide planer

    menu:
        '마라탕 먹을까요?':
            $affection_pl+=20
            jump pl_mara
        
        '제육 / 돈가스 / 국밥 먹을까요?':
            $affection_pl-=70
            jump pl_out
        
        '마라로제떡볶이 먹을까요?':
            $affection_pl+=80
            jump pl_maralose

label pl_dam:
    play music "audio/scare.Mp3"
    show c_c at left
    ls  "3시간 뒤까지 다시 써오세요."
    show planer at right
    pl2 "저 오후에 반차 낼건데요."
    ls "왜? 무슨 일 있어요?"
    pl2 "이번에 새로생긴 카페 가려고요."
    ls "(하... 이거 답 없네.)"
    "점심시간에 공략해야겠다."
    stop Music fadeout 1.0
    ls "곧 점심시간인데 뭐 드실래요?"
    pl2 "그래요..."
    hide c_c
    hide planer

    menu:
        '마라탕 먹을래요?':
            $affection_pl+=50
            jump pl_mara
        
        '제육 먹을랜요?':
            $affection_pl-=100
            jump pl_out
        
        '마라로제떡볶이 먹을까요?':
            $affection_pl+=80
            jump pl_maralose

label pl_mara:
    play music "audio/orange.Mp3"
    show planer at right
    pl2 "음... 어제 먹었는데 먹으러 가죠"
    hide planer
    "단 둘이서 마라탕 집에 간다."
    scene maraa
    "주문하고서 약간의 공백이 생겼다."
    menu:
        '회사 일 말하기':
            $affection_pl-=20
            "호감도: [affection_pl]"
        '최신 남자아이돌 얘기한다.':
            $affection_pl+=10
            "호감도: [affection_pl]"
    "식사를 마치고 회사로 돌아가는 길, 탕후루 집이 보였다"
    scene tanghuru
    show planer at right
    pl2 "그럼 선배, 탕후루도 같이..??"
    show c_c at left
    menu:
        '그래, 내가 사줄게':
            $affection_pl=100
            "호감도: [affection_pl]"
            stop music fadeout 3.0
            jump pl_success
        '빨리 회사에 돌아가서 기획서나 써.':
            $affection_pl=-100
            stop music fadeout 3.0
            "호감도: [affection_pl]"
            jump pl_out

            
label pl_maralose:
    play music "audio/orange.Mp3"
    scene maraalose
    show planer at right
    pl2 "좋아요! 떡볶이 땡겼는데 ㅎㅎ"
    hide planer

    "단 둘이서 떡볶이 집에 간다."
    "주문하고서 약간의 공백이 생겼다."

    menu:
        '회사 일 말하기':
            $affection_pl-=20
            "호감도: [affection_pl]"
        '최신 남자아이돌 얘기한다.':
            $affection_pl+=10
            "호감도: [affection_pl]"
    "식사를 마치고 회사로 돌아가는 길, 탕후루 집이 보였다"
    scene tanghuru
    show planer at right
    pl2 "선배님 혹시 탕후루 먹어도 되나요?"
    
    menu:
        '그래, 내가 사줄게':
            $affection_pl=100
            stop music fadeout 3.0
            "호감도: [affection_pl]"
            jump pl_success
        '빨리 회사에 돌아가서 기획서나 써.':
            $affection_pl= -100
            stop music fadeout 3.0
            "호감도: [affection_pl]"
            jump pl_out
            
label pl_out:
    play music "audio/scare.Mp3"
    pl "..."
    "호감도: [affection_pl]"
    pl "저 퇴사할게요. 수고하셨습니다."
    jump pl_fail

label pl_success:
    play music "audio/win.Mp3"
    pl2 "진짜요? "
    pl2 "저 기획서 열심히 써볼게요 ㅎㅎ"
    stop music fadeout 3.0
    jump gacha

label pl_fail:
    "서브 퀘스트 실패"
    return 

label gacha:
    scene table
    show quest at truecenter
    q "모든 팀원들 공략에 성공했습니다."
    q"보상:10연차 가챠권"
    hide quest
    show c_c at left
    ls "가챠??"
    show quest at right
    q "가챠를 진행하겠습니까?"
    menu:
        '네':
            "가챠 곡 틀고 가자잇"
            jump gacha2

label gacha2:
    play music "audio/nawan.Mp3"
    scene gachaaa
    "슈우우우우우웅"
    scene star
    show quest at right
    q "축하합니다."
    hide quest
    show ssrr at center
    "ssr 황젠슨을 얻으셨습니다."
    hide ssrr
    stop music fadeout 1.5
    show c_c at left
    ls "오....! ssr. 얼마나 일 잘할까?"
    show c_tm at right
    tm "승준씨 잠깐 와보게"
    show c_nw at center
    tm "이 친구는 황젠슨이라고 하네. 신입 프로그래머야."
    nw "Hello~"
    tm "이 친구는 해외 유학파야."
    ls "아 그렇군요. 반갑습니다."
    "황젠슨 저 친구는 놀라울정도로 코딩을 잘했다."
    jump second

label second:
    scene officetable
    "그렇게 회사 프로젝트는 순조롭게 진행되고 있었다."
    "앞으로 메인퀘스트 완료까지 절반이 지났다."
    "문득 궁금해졌다. 원래 몸이었던 최승빈은 지금 어떻게 지내고 있을까."
    menu:
        '찾아간다.':
            jump back_home
        '찾아가지 않는다':
            ls "나는 지금 만족해. 찾아간다고 해서 돌아갈 수 있는것도 아니고."
            ls "돌아갈 생각도 없고.."
            ls "분명 부모님도 이런 나를 원할거야...."
            ls "하지만 이게 진짜 나일까???"
            menu:
                '그래. 찾아가야겠어!!':
                    jump back_home

label back_home:
    play music "audio/sad.Mp3"
    scene home
    "원래 내가 살던 집 앞에 도착했다."
    "막상 찾아오니 뻘쭘하니 근처를 돌아댕겼다."
    "멀리서 익숙한 목소리가 들려왔다."
    show c_nei at right
    nei "승환 엄마, 그래서 아들은 취직할거 같어?"
    show c_ly at left
    ly "한 2주 전에 취직 준비한다고 8만원 달라해서 줬지."
    ly "왠지 이번엔 될거 같아."
    nei "그게 사실이야? 잘 됬음 좋겠네~"
    nei "몇년을 맘 썩혔는데.. 이제는 할 때 됬지."
    hide c_nei
    ly "그러게 말이야. 됬음 좋겠네.."
    hide c_ly
    "사실 취직준비 한다면서 8만원 받은건 사실 게임 살려고 거짓말 친거다.."
    "엄청난 죄악감이 찾아온다."
    "나는 이대로 괜찮은건가.. 돌아갈 수 있는건가.."
    "퀘스트 창이 나오면서 변화가 생겼다."
    show quest at truecenter
    q "MainQuest: 게임을 완성하시오. 패널티: 현실로 돌아가기"
    hide quest
    show c_c
    ls "패널티가 바꼈어.."
    "나는 선택해야만 해"
    "팀원들을 뒤로 한채 게임 완성을 포기할 것인지"
    "아니면 팀원들과 함께 게임을 완성할 것인지"
    stop music fadeout 3.0
    menu:
        '그래 난 빌런이 되겠어.':
            hide c_c
            jump villain
        '난 게임을 완성시키겠어.':
            hide c_c
            jump comp

label villain:
    play music "audio/vill.Mp3"
    show c_c at left
    ls "조금만 기다려 엄마. 내가 곧 돌아갈게"
    hide c_c
    show c_villain at left
    "그러기 위해선 미움받더라도 빌런이 되겠어."
    hide c_villain
    "게임 출시 1주일 전"
    menu:
        '기획자를 부른다':
            jump call_pl

        '그래픽을 부른다':
            jump call_gr

        '프로그래머를 부른다':
            jump call_pr

label comp:
    scene officetable
    show c_c at left
    ls "내 뒤에는 많은 팀원들이 있어. 그들을 버릴 순 없어."
    "게임 출시 1주일 전"
    ls "여러분들 출시까지 1주 남았습니다. 화이팅 합시다."
    pr "저기... 드릴 말씀이 있습니다."
    pr "지금까지 해놓은 코드가 절반 이상 날라갔어요...."
    ls "네???? 그게 말이 되요?"
    ls "굿 허브 안썼어요??"
    pr "제가 사실... 굿 허브를 쓸 줄 몰라서요.."
    "너무 어이 없었다."
    "어떻게 프로그래머가 굿 허브 하나 쓸줄 모르는가.."
    "이 상황을 어떻게 타파하지?"
    menu:
        '황젠슨한테 도와달라 한다.':
            jump nw2
        '비켜봐, 내가 직접 코드 친다.':
            jump coding

label nw3:
    ls "젠슨씨 그렇게 됬는데 가능하겠어?"
    nw "No Problem"
    "그렇게 이틀이 지나 젠슨은 모든 코드를 복구해 왔다."
    ls "역시 이 친구는 크게 될 사람이야."
    ls "게임은 출시 1일전에 완성되었다."

    "게임은 정상적으로 출시가 되었다."
    "커뮤니티와 여러 스트리머, bj들이 게임을 플레이하며 인기를 얻었다."
    "그렇게 나는 성공한 개발자로 불리며, 성공한 삶을 살게 되었다."
    jump credit

label coding:
    # 초기 메시지들
    show c_c at left
    ls "비겨봐요. 내가 직접 하게."
    play music "audio/company sound.Mp3"
    "#include ~~$@#$"
    "class #$!@"
    ls "후.. 거의 복구 했어."
    ls "이제 마지막 일만 남았어."
    hide c_c
    # 사용자 입력을 받습니다.
    $ giti = renpy.input("git.import 또는 git.ignore을 치시오", length=32)

    # 입력값에 따라 분기 처리합니다.
    if giti == "git.import":
        jump sc
    elif giti == "git.ignore":
        jump fl
    else:
        "잘못된 입력입니다. 다시 시도해 주세요."
        jump coding  # 다시 입력을 받기 위해 처음으로 돌아갑니다.
        
label sc:
    "게임은 정상적으로 출시가 되었다."
    show quest at truecenter
    q "MainQuest 성공"
    q "지금부터 보상을 주겠습니다."
    hide quest
    play music "audio/end.Mp3"
    "커뮤니티와 여러 스트리머, bj들이 게임을 플레이하며 인기를 얻었다."
    "그 뒤 나는 초고속 승진을 하면 따로 팀을 꾸려 회사를 차리게 되었다."
    "그렇게 나는 성공한 개발자로 불리며, 성공한 삶을 살게 되었다."
    jump credit
    

label fl:
    "게임 출시일이 되었고 게임을 출시 되지 않았다."
    scene table
    show quest at truecenter
    play music "audio/serious.Mp3"
    q "MainQuest 실패"
    q "지금부터 패널티를 실행하겠습니다."
    hide quest
    "하지만 아무 일도 일어나지 않았다.."
    "대중들은 게임이 안나오자 불만을 토했다."
    "커뮤니티는 화제의 영상으로 인해 불탔고 뉴스까지 나오기 시작했다."
    scene bg_news
    show c_vio at truecenter
    "'중소 블랙기업 상사의 횡포'"
    "그렇다 내가 팀원을 화냈던게 cctv에 녹화가 되었고. 이걸 유출한 것이다."
    "이미 내 신원, 집, 가족 모든 정보가 인터넷에 뿌려졌다."
    "밖에는 이미 기자, 노조, 시위하는 사람들로 가득 찼다."
    hide c_vio
    scene topp
    stop music fadeout 1.5
    "정신이 없던 나는 어느샌가 회사 옥상에 올라와 있었다."
    "더이상 자신의 의지가 아닌 누군가가 나를 조종하듯이 난간에 올라섰다."
    "그리고 공중에 뛰어 들었다"
    scene black
    play music "audio/acc.Mp3"
    "쾅"
    stop music fadeout 0.5
    jump badending

label call_pl:
    scene bg_pl
    show c_villain at left
    ls"수아씨 잠시 와보세요"
    scene tangbi
    show c_villain at left
    show planer at right
    pl"(뭐지? 왜 갑자기 내 본명으로 말하는 거지?)"
    pl "ㄴㅔ..."
    ls "제가 왜 불렀는지 알아요?"
    pl "아뇨.. 잘 모르겠습니다."
    menu:
        '회사에서 에어팟 끼는 걸 화낸다.':
            jump airpot
        
        '기획서 엉망으로 써오는 걸 화낸다.':
            jump planner

label airpot:
    ls "수아씨. 회사가 장난이에요?"
    ls "어느 누가 일하는데 에어팟 껴요?"
    ls "상사 말은 듣기 싫다는 거에요?"
    pl "아뇨.. 그게 아니라.."
    ls "아니면 뭐죠? 대답해보세요."
    pl "그게... 에어팟을 껴야 업무 능률이 올라가요."
    ls "그래서 하루에 6시간 쓴 기획서가 그거에요? A4 2장?"
    pl "...."
    ls "게다가 수아씨는 회사 출근시간도 지킨 적 없잖아요."
    pl "갑자기 그건 왜...."
    ls "수아씨 이럴거면 회사 다니지 마세요."
    pl "네??? 그게 무슨..."
    ls "남한테 피해만 주잖아요. 정말 쓸모 없네"
    hide c_villain
    "그녀는 흐느껴 울기 시작한다."
    "그녀는 눈물을 멈추고 하이힐로 회사를 뛰쳐 나갔다."
    hide planer
    "며칠이 지나도 그녀가 오는 일은 없었다."
    jump badthird

label planner:
    ls "수아씨는 왜 기획자해요?"
    ls "기획서 하나 못쓰는데, 기획자가 우스워요? 만만해보여요?"
    pl "아닙니다... 죄송합니다.."
    ls "죄송해서 되는거에요? 그게? 회사가 학원인줄 알아요?"
    ls "솔직히 말할게요. 수아씨 기획자 재능 없어요."
    ls "그렇다고 수아씨 노력도 안하잖아요."
    ls "회사 오면 브이로그 찍는다고 촬영만 하고."   
    pl "죄송합니다. 지송합니다. 죄송합니다."
    hide c_villain
    hide c_planer
    "그녀의 MZ모습은 사라지고 울기 시작했다."
    "그녀는 눈물을 멈추고 하이힐로 회사를 뛰쳐 나갔다."
    "며칠이 지나도 그녀가 오는 일은 없었다."
    jump badthird

label badthird:
    show c_c
    ls "그래.. 이거면 된거야."
    ls "이거면.. 나만 악인이고 나만 미움 받으면 되는거야."
    hide c_c

    "그렇게 회사에서 빌런이 되고 아무도 나를 의지하지 않았다. 그리고 팀원들은 일을 안하기 시작했고, 결국 프로젝트 팀은 터졌다."
    "게임 출시일이 되었고 게임을 출시 되지 않았다."
    scene table
    show quest at truecenter
    stop music fadeout 1.0
    play music "audio/serious.Mp3"
    q "MainQuest 실패"
    q "지금부터 패널티를 실행하겠습니다."
    hide quest
    "하지만 아무 일도 일어나지 않았다.."
    "대중들은 게임이 안나오자 불만을 토했다."
    "커뮤니티는 화제의 영상으로 인해 불탔고 뉴스까지 나오기 시작했다."
    scene bg_news
    show c_vio at truecenter
    "'중소 블랙기업 상사의 횡포'"
    "그렇다 내가 팀원을 화냈던게 cctv에 녹화가 되었고. 이걸 유출한 것이다."
    "이미 내 신원, 집, 가족 모든 정보가 인터넷에 뿌려졌다."
    "밖에는 이미 기자, 노조, 시위하는 사람들로 가득 찼다."
    hide c_vio
    scene topp
    stop music fadeout 1.5
    "정신이 없던 나는 어느샌가 회사 옥상에 올라와 있었다."
    "더이상 자신의 의지가 아닌 누군가가 나를 조종하듯이 난간에 올라섰다."
    "그리고 공중에 뛰어 들었다"
    scene black
    play music "audio/acc.Mp3"
    "쾅"
    stop music fadeout 0.5
    jump badending

label badending:
    scene light
    "밝은 빛이 나를 비췄다."
    play music "audio/end.Mp3"
    show black man at left
    qu "뭐야 눈 부셔..."
    scene bg_room
    qu "눈을 떠보니 눈 앞에는 익숙한 모니터가 있었다."
    hide black man
    "현실의 나로 돌아온 것이다."
    show c_c_c at left

    c "나 돌아온거구나..."
    "모니터에는 익숙한 게임 이름이 있었다."
    hide c_c_c
    c "..."
    scene gt
    "NightMare"
    jump credit

label credit:
    # define narrator = Character(None,kind=nvl)
    # define Character(None)
    scene black
    "기획자: 이동빈"
    "프로그래머: 이동빈"
    "그래픽: AI"
    "이미지 출처"
    "The End"
    "여러분 개발자도 사람입니다. 욕하지 말아주세요"
    stop music fadeout 3.0
init:
    # 캐릭터별 호감도 변수를 선언합니다.
    $ game_develop= 0
    $ affection_pl = 0
    $ affection_gr = 0
    $ affection_pg =0