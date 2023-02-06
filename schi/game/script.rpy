# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Дівчина")
define t = Character("Ти")
define v = Character("Вона")
define p = Character("Хлопець")





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    v "You've created a new Ren'Py game."

    v "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    jump abort






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
    # d кричить
    p "Сонце, нашо ти себе мучиш?"
    d "Тобі не зрозуміти."
    p "Ну то поясни..."
    menu:
        "Ввімкнути світло":
            scene bed_lamp
            d "Ну шо пояснити? Поки я не знаю результату, в мене немає проблеми, яку треба вирішувати."
            p "Дуже дивна логіка."
            d "Дякую!"
            p "Нє, ну так ти себе мордуєш думками, тобі он вже сни почали снитись. Я ж знаю, що він був про дитину."
            # d відводить очі
            p "А там би ти знала результат, вже могли б про щось думати і вирішувати. А не на пустому місці хвилюватись. В тебе був стрес на роботі, може того затримка."
            d "Да, стрес. Я ж знаю, що все добре, це просто стрес."
            # d лягає на ліжко
            # тут буде ДОХУЯ візуалочок крч а поки що коментар (який я не буду видаляти бо в падлу + рофел великодочка)

    p "Сонце, я не хочу тиснути, але і мені теж треба знати. Я ж теж тут замішаний, а не просто повз проходив."
    d "А тобі то що?"
    p "Так, жінко, усі на нервах, але давай…"
    p "*зітхає*"
    p "Я тебе розумію, ти хвилюєшся. Я знайду роботу, буду якось з навчанням поєднувати. Або дам гроші, якшо ти вирішиш..."
    d "Вирішу що? Яке слово ти не хочеш казати?"
    p "Чому не хочу? Якщо ти вирішиш зробити аборт. Я підтримаю будь-який твій вибір."
    d "Ага, підтримаєш."

    #menu
