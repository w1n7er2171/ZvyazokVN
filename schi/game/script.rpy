﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Ти")
define v = Character("Вона")
define p = Character("Хлопець")
define d = Character("Дівчина")
define m = Character("Мама")
define f = Character("Подруга")
define l = Character("Лікар")
define b = Character("Бармен")
define o = Character("")




#   окремі діалог бокси для всіх персів (один зверху зліва, лругий знизу зправа)

label start:

    scene city2 with dissolve

    o "В п'ятницю ввечері, коли бари відкривають ширше свої двері,"
    o "а повітря наповнюється алкоголем і сексом, на вулицю вивалюється різний збрід."
    
    scene poch2 with dissolve
    
    o "Засмальцьовані робітники заводів прилаштовують свої руки до жіночих сідниць."
    
    scene bar_outside with dissolve
    
    o "Cтуденти скидаються на дешевий алкоголь."
    
    scene bar_0 with dissolve
    show bar_1 with dissolve

    o "Бухгалтера"

    show bar_2 with dissolve

    o "Повії"

    show bar_3 with dissolve

    o "Менеджери середньої ланки"

    show bar_4 with dissolve

    o "Драг-дилери"

    show bar_5 with dissolve

    o "Дизайнери"

    show bar_6 with dissolve

    o "А, можливо, і самі боги,"

    scene bar_7 with dissolve

    o "збираються промочити горло в п'ятницю в барі."

    jump bar




label bar:

    scene bar_inside

    b "Ооо, давно тебе не бачив, любий."

    menu:

        "Мене не було з минулих вихідних":

            b "Ти знаєш, який нудний робочий тиждень в барі."
            b "Сюди всі прилізають тільки в п’ятницю і по вихідним."

            t "А ти пропонуєш пити в понеділок?"

            b "Ну да, ти ще скажи, шо тобі не хочеться."

            t "Це алкоголізм."

            b "Можна подумати, нам з тобою не знайомий цей діагноз."
            b "Це допомагає переживати дійсність."

        "Я не хотів сюди приходити":

            b "Да забий, ну перебрав останнього разу."
            b "З ким не буває?"

            t "З тобою було?"

            b "Киця, я працюю барменом вже 20 років."
            b "Ти думаєш, ти найжахливіший випадок, який я бачив?"

            t "А що ти бачив?"

            b "Я дав розписку, що не буду про це розповсюджуватись."

    scene bar_inside with Pause(1.5)

    b "Тобі як зазвичай?"
    b "Негроні?"

    t "А є щось сильніше?"

    b "Ооо, важкий тиждень?"
    b "Там, якшо шо твій барига прийшов, я не хотів йому наливати."

    t "І не треба."
    t "Я зав’язав."

    b "Кицю, шо сталось?"
    b "Побути сьогодні твоїм психологом?"

    t "Будь сьогодні моїм барменом."
    t "Налий мені вже нарешті."

    # з’являється коктейль
    # Він довго дивиться на дівчину, яка танцює, вона поступово стає ближче і підходить до нього

    b "Здається в когось сьогодні буде секс…"

    menu:

        "Мені не цікаво слухати про твоє домашнє порно, старий хрич.":
        
            b "Тобі більш нічого і не лишається."
            b "Принаймні, воно в мене є."

        "Ти ж знаєш, я не знайомлюсь в барах.":

            b "Ти хотів сказати, що в тебе не виходить знайомитись?"

    # яка ж вона гарна. Вона дивиться на мене?  Боже, чувак, тільки не налажай

    v "Привіт, чого не танцюєш?"

    t "Я ноги."
    t "Ну тобто ніяк танцюрист."
    t "Короче, я не танцюю."

    # ідіооот

    v "В тебе гарна футболка."

    t "Дякую, мама вибирала."
    t "Хочеш чогось?"

    v "Хаха, сказати “тебе” буде надто зухвало?"

    # Що вона щойно сказала?

    t "А ти вже добряче випила, правда?"

    d "Не дуже, гумор в мене просто такий."
    d "Але я б не відмовилась від Сексу на пляжі."

    t "Для цього зараз надто холодно."

    # вона сміється (бармен подає їй секс на пляжі)

    d "Так чому ти не танцюєш?"
    d "Варіант “Ти ноги” не приймається."

    t "Хто взагалі танцює в барах?"

    d "А що ще можна робити в барах?"

    t "Пити і спостерігати за людьми."
    t "Я себе більш вільно відчуваю спостерігачем."
    t "Наче щось прекрасне проноситься поруч зі мною,"
    t "наприклад, ти,"
    t "а я не хочу сполохати цю красу."

    d "Боже, да містер, да ви поет."

    t "Надто банально?"

    b "Так, любий, мене ледь не знудило ванільним рафом."

    d "А що не так з ванільним рафом?"

    b "Нічого, аби не на рослинному."

    d "Я зараз повинна як крута дівчина сказати: “Ой фу, я п’ю тільки фільтр”?"

    t "Ти в барі."
    t "Як мінімум, його тут не подають."
    t "Як максимум, де ще можна бути відвертим, як не тут?"

    d "Ми відверті тільки коли сповідаємось."

    t "Тобто тобі для відвертості треба релігія?"

    d "Для відвертості мені потрібна довіра."

    t "Ти довіряєш священнику?"

    d "Я б довіряла секрети тільки тим, кого більше ніколи не побачу."

    t "Старий, повтори нам, будь ласка, коктейлі…"


    

label abort:
    scene bed_day
    p "Та ми ж наче..."

    d "Презерватив не рвався?"

    p "Ну я б тобі сказав."

    d "Ну а я тобі кажу, що в мене затримка."

    p "Ну зроби тест, а там буде видно."

    d "Угу…"
    
    p "Сонце, чим раніше ти будеш знати, тим краще, тим менше надумаєш і так далі, добре? Мені купити?"

    d "Ні, я зроблю."

    scene black with dissolve
    show text "Через два дні" with Pause(1.5)
    scene black with dissolve
    scene hands with dissolve
    scene hands with Pause(10)
    scene black with Pause(1.5)
    # d кричить
    scene bed_night

    p "Сонце, нашо ти себе мучиш?"

    d "Тобі не зрозуміти."

    p "Ну то поясни..."

    menu:
        "Ввімкнути світло":
            scene bed_lamp
            d "Ну шо пояснити? Поки я не знаю результату, в мене немає проблеми, яку треба вирішувати."

            p "Дуже дивна логіка."

            d "Дякую!"

            p "Нє, ну так ти себе мордуєш думками, тобі он вже сни почали снитись."
            p "Я ж знаю, що він був про дитину."

            # d відводить очі

            p "А там би ти знала результат, вже могли б про щось думати і вирішувати."
            p "А не на пустому місці хвилюватись,"
            p "в тебе був стрес на роботі, може того затримка."

            d "Да, стрес. Я ж знаю, що все добре, це просто стрес."

            # d лягає на ліжко
            # тут буде ДОХУЯ візуалочок крч а поки що коментар (який я не буду видаляти бо в падлу + рофел великодочка)

    p "Сонце, я не хочу тиснути, але і мені теж треба знати."
    p "Я ж теж тут замішаний, а не просто повз проходив."

    d "А тобі то що?"

    p "Так, жінко, усі на нервах, але давай…"
    p "*зітхає*"
    p "Я тебе розумію, ти хвилюєшся."
    p "Я знайду роботу, буду якось з навчанням поєднувати,"
    p "або дам гроші, якшо ти вирішиш..."

    d "Вирішу що? Яке слово ти не хочеш казати?"

    p "Чому не хочу? Якщо ти вирішиш зробити аборт."
    p "Я підтримаю будь-який твій вибір."

    d "Ага, підтримаєш."

    scene bed_lamp

    menu:
        
        "Шо ти взагалі розумієш?":
            d "Шо ти взагалі розумієш?"
            d "Розумієш, який то зв’язок з дитиною?"
            d "Отоді, коли ти носиш її під серцем, а вона буквально без тебе не виживе, розумієш?"
            d "Ти як чоловік хоч колись це зрозумієш?"
            d "Та і я поки не розумію."
            d "Я взагалі нічого не розумію..."

            p "Заспокойся, будь ласка."

            d "Вся відповідальність на мені, всі наслідки."
            d "Це не тобі доведеться не спати ночами від токсикозу, опухлості ніг і всяких інших штук."
            d "Розуміє він..."
            d "Не в тебе буде вилазити волосся, і не ти будеш ненавидіти свою власну дитину, партнера і себе під час післяродової депресії."
            d "А мені!"
            d "Я сама буду це все розгрібати."
            d "І мене це бісить."
            d "Просто бісить!"

            p "Слухай, все може бути не так страшно, як ти описуєш."

            d "А може бути так!"
            d "І до цього треба бути готовим."
            d "Бо не тобі буде у снах приходити ненароджена дитина!"

            p "І шо ти від мене хочеш?"

            d "Нічого."

            p "Я в це не лізу. Ти сама розпоряджаєшся своїм тілом, ти сама робиш вибір."

            d "Отож, ти не лізеш."
            d "Я сама роблю вибір від якого залежить моє життя, твоє життя і ще одне життя."

            p "Що ти від мене хочеш?"

            d "Сонце, я знаю, що ти будеш допомагати, дякую."
            d "Але ти ніколи не зрозумієш всіх цих переживань."
            d "Просто тому що ти чоловік, мене це просто дратує."

            p "Дратує, що я чоловік?"

            d "Дратує, що до тебе немає таких очікувань, як до жінок."
            d "Є інші, але не такі..."
            d "Вибач."

            scene bed_night

            p "Йди до мене."

            # ВТИКАЄТЬСЯ В НЬОГО

        "Дякую тобі...":
            d "Дякую тобі..."
            d "Рибка, мені подобається, що ти такий свідомий і хвилюєшся, і максимально правильно реагуєш, як по книжці прямо."
            d "Але вибір повинна робити я, розумієш?"
            d "Не всі оці порадники, не всі пролайфери і чайлдфрішники, а я."

            p "Тобі вирішувати, що робити зі своїм тілом..."

            d "Так, але і вся відповідальність на мені, всі наслідки."
            d "Я втомилась від цього."
            d "Суспільство постійно каже жінці, як краще."
            d "І це настільки полярні думки..."
            d "Аборт це не гріх, звісно, але ембріон живий."
            d "Це вимушене зло, але це вбивство."

            p "Тоді і вбивство комара, теж вбивство."

            d "А де я казала, що ні? Це живий організм."
            d "І ти вирішуєш забрати життя."

            p "Сонце, але аборт це не погано."

            d "Це не погано."
            d "Він повинен бути доступним."
            d "Жінка повинна розпоряджатись своїм тілом."
            d "Але якшо дивитись більш широко..."

            p "Як широко?"
            
            d "Нас вчать, що життя священне."
            d "Зародок життя теж життя."
            d "Але моє життя важливіше, ніж життя ще ненародженого?"

            p "Ти не повинна його перекреслювати через дитину."

            d "Я знаю."
            d "Я сама буду це все розгрібати."
            d "Суспільство тисне."
            d "А вибір робити мені."
            d "Я сама приймає рішення від якого залежить моє життя, твоє життя і ще одне життя."
            d "І я не справлюсь, це надто висока відповідальність…"

            p "Сонце..."
            p "Ти будеш з усім цим не сама, я буду поруч."

    scene black with dissolve
    show text "Через день" with Pause(1.5)
    scene black with dissolve
    scene test with dissolve
    scene test with Pause(10)
    scene black with Pause(1.5) 

    scene phone with dissolve

    menu:
        "Зателефонувати мамі":

            scene ma_roz with dissolve

            m "А як так сталось?"

            d "Мамо, тобі треба пояснювати, як це може статись?"

            m "Я не про те..."
            m "Добре, шо з пустого в порожнє."
            m "І шо ти думаєш?"

            d "Втопитись, шо я думаю..."

            m "Доню..."
            m "От зараз взагалі не смішно."

            d "Ну а шо я можу думати?"
            d "Я тобі зателефонувала розказати!"
            d "Поки не думала."

            m "Ти ж знаєш, що ми з батьком поможемо."

            d "Знаю."

            m "І квартиру допоможемо купити, і помагати будемо перший час."

            d "Знаю."

            m "Аби здоровеньке виросло."
            m "А чоловік, що каже?"

            d "А що він може казати?"
            d "Вибір за мною, він підтримає будь-яке моє рішення."

            m "Доцю, ну яке рішення…"
            m "Нє, звичайно вибір за тобою, але ти ж знаєш, що кажуть..."
            m "Он Людка зробила аборт і дітей вже мати не може."
            m "Ну то думає зараз за усиновлення."
            m "То добре, але ж то не своє, гени, кров рідненька, зв’язок."

            d "Мамо..."

            m "Не знаю, правда, як в неї рука піднялась, воно ж живе…"

            d "Мамо, досить..."

            m "Ну але куди їй, хлопця немає, роботи немає, та й батьки не допоможуть,"
            m "а шо вони ні города не мають, ні дачі, він на заводі, вона касиркою."
            m "А ми допоможемо, доця, ти повинна пам’ятати."
            m "З батьком якось разом..."
            m "Нічого, якось буде..."

            d "Мамо, дитина не повинна бути якось."

            m "Ну да небагато."
            m "Але й ти в нас небагато росла, і нічого, виросла."
            m "Ти навіть уявити не можеш, що я відчула, коли мені тебе дати."
            m "Такі оченята маленькі, ручки."
            m "А ти відразу кричати почала, але як тільки я тебе взяла, то заспокоїлась, і дивишся на мене так здивовано."
            m "Доця, це таке відчуття, ти б знала, наче оцей пуп’янок то найрідніше, що може бути."
            m "Ти ж все життя жаліти будеш..."

            d "Мамо…"

            m "Ну то да, не батьки-мільйонери, головне, аби любов була, аби турбувались."

            d "Мамо…"

            scene ma_roz with Pause(1.5)

            d "Досить, ти не допомагаєш!"

            m "Ой, рибонька, аби ж я могла чим зарадити…"
            m "Але ти повинна зробити вибір, і вже зараз, бо потім не можна буде."
            m "Треба чим скоріше."
            m "Я нічого не буду казати, маєш сама прийняти рішення."



        "Зателефонувати подрузі":

            scene pod_roz with dissolve

            d "Мені треба тобі дещо сказати..."

            f "Тільки не кажи, що ти вагітна."

            d "..."

            f "Серйозно? Я ж пожартувала, ти шо..."

            d "А я ні."

            f "Ти вже ходила до лікаря?"

            d "Завтра запис."

            f "Єбааать, подруго, оце ти даєш."
            f "А твій шо?"

            d "Нічо, сказав, шо вибір за мною."

            f "І шо ти думаєш?"

            d "Да що ж мене постійно всі питають, що я думаю?!"

            f "Ну чого ти гніваєшся?"
            
            d "А шо мені ще робити?"
            d "Сміятись і радіти дитині?"
            d "Плакати?"
            d "Що?"
            d "Звичайно я гніваюсь."
            d "Щоб ти робила на моєму місці?"
            
            f "Не думаю, що я можу радити."
            
            d "А я не прошу поради, я прошу думку свою висловить."
            
            f "Зайка, ти вчишся."
            f "Твій теж вчиться."
            f "Ви, звичайно, можете забити на все і піти працювати, але…"
            f "Ну це хрест на твоїй кар’єрі, на його кар’єрі."
            f "Та все одно на нього."
            f "Ти ж все життя прагнеш працювати, бути такою бізнес-леді,"
            f "а зараз перекреслювати це все через дитину?"
            
            d "..."
            
            f "Але на своєму б не змогла…"
            f "Але на твоєму місці зробила аборт."
            f "Мені завжди була важлива сім’я, ти знаєш, як я дітей хочу, а для тебе це не головне."
            
            d "І потім з цим жити?"
            
            f "Ну слухай, ти ж знаєш, що це соціумом дуже нав’язано…"
            
            d "Але воно вже нав’язано і вже в мені сидить."
            
            f "Ну тобі вирішувати."
            f "Ну ти казала, що батьки допоможуть."
            f "Я теж можу сидіти інколи, мені тільки в радість."
            
            d "Та я знаю, що мені вирішувати!"
            
            f "Не кричи, я знаю, що знаєш."
            
            d "І знаю, що це вже треба вирішити."
            d "Вже і негайно, бо термін вже…"
            d "І знаю, що цей вибір за мене ніхто не зробить."
            
            f "Зайка…"
            
            d "Суспільство не хоче нести відповідальність за дітей, але чомусь воно диктує, що діти це здорово,"
            d "що аборт це гріх."
            d "І з цими установками, здаєш, вже дуже важко зробити вибір."
            
            f "Слухай, ну чого ти…"
            f "Сходи завтра до лікаря, він більш детально все розкаже."
            
            d "Що розкаже?"
            d "Він буде переконувати…"
            d "Мене дратує це все."
            d "Мені вже сняться діти, розумієш?"
            
            f "Ти своїми думками себе до могили заженеш."
            f "Сходиш завтра до лікаря, а далі буде видно."
            
            d "Чому ніхто не може зробити вибір за мене?"
            
            f "Котик…"
            
            d "Ну я не хочу його робити, не хочу нести відповідальність, не хочу всієї цієї ситуації."
            
            f "Я тобі казала, що секс з чоловіками не вартує переляку, коли в тебе затримка навіть на один день."
            
            d "Люблю тебе."
            d "Як тільки мене зацікавлять дівчата, я тебе наберу."

    # Наша героїня в центрі, поруч з нею лого хлопця, мами і подруги. Ми ж не зробимо так, аби воно вертілось?
    # Але треба якось зробити, аби воно все було на кучу, можна, аби вони знову накладались одна на одну

    p "Вирішуй, я підтримаю будь-який вибір, але його треба зробити..."

    m "Подумай, зваж все, я знаю, що це складно, ти впораєшся..."

    f "Знаю, що складно, але ти повинна прийняти рішення..."

    p "Вирішуй..."

    m "Подумай..."

    f "Ти повинна прийняти рішення..."

    p "Вибір треба зробити..."

    show black with dissolve
    show black with Pause(3)

    # плач дитини

    # по центру діалог бокс
    l "Дівчино, дівчино, ви мене чуєте?"

    scene cabinet with dissolve

    # ліпає очима

    d "Що?"

    l "З вами все гаразд?"

    d "Так…"
    d "Я просто..."
    d "Так."

    l "Я вам кажу, що ви не вагітні."

    d "Що?"

    l "Я кажу, що не спостерігаю у вас ознак вагітності."

    d "Тобто як?"
    d "Тест показав, що…"

    l "Тест це не 100 відсоткової гарантії."
    l "Є декілька можливих варіантів, чому він схибив."
    l "Ви приймаєте зараз якісь препарати?"

    d "Що?"

    l "Ліки якісь приймаєте?"

    d "Так, я обстежуюсь у психіатра."
    d "В мене нещодавно був стрес, тому він виписав мені щось легеньке."

    l "Ну тоді зрозуміло."
    l "Це одна з причин."
    l "Але на вашому місці, я б все одно пройшов обстеження."
    l "Розумієте…"

    scene black with dissolve
    show text "Я не вагітна." with Pause(1)
    scene black with dissolve
    show text "Не вагітна." with Pause(1)
    scene black with dissolve
    show text "Не вагітна." with Pause(3)
    scene black with dissolve

    scene background
    



