

label Group_Strip_Study(BO=[], QuizOrder=[]):
    $ Count = 0
    $ between_event_count = 1
    $ counter = 0
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    $ renpy.random.shuffle(QuizOrder)
    if EmmaX in Party and Party[0] != EmmaX:

        $ Party.reverse()
        call shift_focus (Party[0])


    if Party[0] == RogueX:
        if not RogueX.top and not RogueX.legs and RogueX.PantiesNum <= 5:

            $ RogueX.change_face("sly")
            ch_r "Well, I did consider suggesting we do some \"strip studying,\". . ."
            $ RogueX.eyes = "down"
            ch_r "but it looks like I got ahead of myself. . ."
            $ RogueX.eyes = "squint"
            ch_r "Did you have anything else in mind?"
            call Rogue_SexMenu
            return
        "[RogueX.name] moves a bit closer to you, and then suggests \"strip studying.\""
        ch_r "Alright, [RogueX.player_petname], I'll make this simple. I'll ask you a quiz question, get it right, I take something off. . ."
        ch_r "Get three wrong, and we're done for the night. Good luck."
    elif Party[0] == KittyX:
        "[KittyX.name] takes the book from your hand, and sets it aside."
        if not KittyX.top and not KittyX.legs:

            $ KittyX.change_face("sly")
            ch_k "I was[KittyX.like]thinking about maybe \"strip studying,\". . ."
            $ KittyX.eyes = "down"
            ch_k "but it would be a pretty short game. . ."
            $ KittyX.eyes = "squint"
            ch_k "Was there something you'd rather do?"
            call Kitty_SexMenu
            return
        "She then asks if maybe you want to do some \"strip studying?\""
        $ KittyX.change_face("perplexed", 2)
        ch_k "Ok, so[KittyX.like]if you get a question right. . . I'll take off a piece of clothing. . ."
        ch_k "But you only get three tries."
        $ KittyX.change_face("sly", 1)
    elif Party[0] == EmmaX:
        call Emma_StripStudy_Intro
        if not _return:

            return
        ch_e "I take the education process very seriously."
        $ EmmaX.change_face("bemused", Eyes="side")
        ch_e "So you get a question right. . . "
        ch_e ". . ."
        $ EmmaX.change_face("sly")
        ch_e "I'll take off a piece of clothing. . ."
        ch_e "But you only get three tries."
    elif Party[0] == LauraX:

        $ LauraX.change_face("sly", 1)
        "[LauraX.name] takes the book from your hand, and sets it aside."
        ch_l "I'm kinda bored, did you just wanna feel me up or something?"
        menu:
            "Sure?":
                ch_l "Good."
                "[LauraX.name] grabs your hand and presses it against her breast."
                call Date_Sex_Break (LauraX, Second)
                if _return == 4:
                    "[LauraX.name] stops what she's doing."
                    ch_l "Be that way."
                    return
                if _return == 3:

                    menu:
                        ch_l "Keep going?"
                        "Go ahead.":
                            ch_l "Un."
                        "We should stop.":
                            ch_l "Grr."
                            return
                call Laura_FB_Prep
                if action_context:

                    jump Laura_SexMenu
            "I really think we should be studying.":
                $ LauraX.change_face("perplexed", 1)
                ch_l "?"
                $ LauraX.change_stat("love", 80, -5)
                $ LauraX.change_stat("obedience", 70, 10)
                $ LauraX.change_stat("inhibition", 70, -5)
                if approval_check(LauraX,600,"L"):
                    $ LauraX.change_face("sadside", 1)
                else:
                    $ LauraX.change_face("angry", 1)
                ch_l "Huh. Ok. Be that way."
        return
    elif Party[0] == JeanX:

        "[JeanX.name] takes the book from your hand, and sets it aside."
        ch_j "This is -boring!-"
        $ JeanX.change_face("sly", 1)
        ch_j "How about we just fool around a bit?"
        menu:
            "Sure?":
                ch_j "Good."
                "[JeanX.name] grabs your hand and presses it against her breast."
                call Date_Sex_Break (JeanX, Second)
                if _return == 4:
                    "[JeanX.name] stops what she's doing."
                    ch_j "Ok, ok, hands off. . ."
                    return
                if _return == 3:

                    menu:
                        ch_j "Keep going?"
                        "Go ahead.":
                            ch_j "Cool."
                        "We should stop.":
                            ch_j "Fine."
                            return
                call Jean_FB_Prep
                if action_context:

                    jump Jean_SexMenu
            "I really think we should be studying.":
                $ JeanX.change_face("perplexed", 1)
                ch_j "Seriously?"
                $ JeanX.change_stat("love", 80, -5)
                $ JeanX.change_stat("obedience", 70, 10)
                $ JeanX.change_stat("inhibition", 70, -5)
                if approval_check(JeanX,600,"L"):
                    $ JeanX.change_face("sadside", 1)
                else:
                    $ JeanX.change_face("angry", 1)
                ch_j "Huh. Ok. Fine."
                "It was not fine. . ."
        return
    elif Party[0] == StormX:
        ch_s "I suppose that you may need some encouragment. . ."
        $ StormX.change_face("bemused", Eyes="side")
        ch_s "If you do get a question right. . . "
        ch_s ". . ."
        $ StormX.change_face("sly")
        ch_s "I could remove an article of clothing. . ."
        ch_s "You get three mistakes, make them count."
    elif Party[0] == JubesX:
        "[JubesX.name] takes the book from your hand, and sets it aside."
        if not JubesX.top and not JubesX.legs:

            $ JubesX.change_face("sly")
            ch_v "I was thinking of maybe doing some \"strip studying,\". . ."
            $ JubesX.eyes = "down"
            ch_v "but where would be the fun in that? . ."
            $ JubesX.eyes = "squint"
            ch_v "Was there anything else you'd wanna do instead?"
            call Jubes_SexMenu
            return
        "Hey, would you maybe be interested in \"strip studying?\""
        $ JubesX.change_face("perplexed", 2)
        ch_v "I mean, you can figure out the rules, right?"
        ch_v "I ask a question, you answer. . ."
        ch_v "-but you only get three strikes and you're out."
        ch_v "Get a question -right,- and maybe I get more naked. . ."
        $ JubesX.change_face("sly", 1)


    $ BO = Party[:]
    while BO:
        $ BO[0].AddWord(1,0,"stripstudy",0,"stripstudy")
        $ BO.remove(BO[0])

    if len(Party) >= 2:
        if counter == 3:

            pass
        elif approval_check(Party[1], 1300) or approval_check(Party[1], 500,"I"):
            if Party[1] == RogueX:
                ch_r "I guess we'll take turns."
            elif Party[1] == KittyX:
                ch_k "So[KittyX.like]I guess we take turns?"
            elif Party[1] == EmmaX:
                "Let Oni know that Emma was in second please."
            elif Party[1] == LauraX:
                ch_l "I will also take a turn."
            elif Party[1] == JeanX:
                ch_j "Sure, ok, give me a shot."
            elif Party[1] == StormX:
                ch_s "I suppose I could join in as well. . ."
            elif Party[1] == JubesX:
                ch_v "So we take turns, right?"
        else:

            if Party[1] == JeanX:
                ch_j "Nah, seems lame."
                "She just sits back and watches."
                $ Party.remove(JeanX)
            else:
                if Party[1] == RogueX:
                    ch_r "I'm not comfortable with this."
                elif Party[1] == KittyX:
                    ch_k "Um, I'm not really into this?"
                elif Party[1] == EmmaX:
                    "Let Oni know that Emma was in second please."
                elif Party[1] == LauraX:
                    ch_l "I don't think so."
                elif Party[1] == StormX:
                    ch_s "I do not want to take part. . ."
                elif Party[1] == JubesX:
                    ch_v "Sorry, guys, this is -your- party. . ."
                "[Party[1].name] leaves the room"
                call Remove_Girl (Party[1])


    while between_event_count:

        call expression Party[0].Tag + "_Quiz_Question"

        $ between_event_count += 1

        if _return:
            call Strip_Study_Right
        else:
            $ Count += 1
            call Strip_Study_Wrong
            if between_event_count == 0 and len(Party) >= 2 and not Party[1].ClothingCheck:

                menu:
                    "Well, [Party[1].name], you and I could still have some fun. . .":
                        $ approval_bonus = 50
                        call expression Party[0].Tag + "_SexMenu"
                    "Bummer":
                        pass

        if len(Party) >= 2 and counter != 3 and Party[1].ClothingCheck:

            $ Party.reverse()
            call shift_focus (Party[0])


    return






label Strip_Study_Right:
    if Party[0].hose:

        $ Line = Party[0].hose
        $ Party[0].hose = 0
        "She slowly removes her [Line]. . ."
        $ Party[0].change_stat("lust", 50, 3)
        return

    if Party[0].top:

        if Party[0] == StormX or Party[0].SeenChest or (Party[0].bra and approval_check(Party[0], 300)) or approval_check(Party[0], 850):
            $ Party[0].change_stat("inhibition", 25, 1)
            $ Party[0].change_stat("inhibition", 50, 1)
            $ Line = Party[0].top
            $ Party[0].top = 0
            "She pulls her [Line] off and throws it aside."
            if not Party[0].bra:
                call expression Party[0].Tag + "_First_Topless"
        else:
            if Party[0] == RogueX:
                ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].player_petname]. I shouldn't have led you on."
            elif Party[0] == KittyX:
                ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."
            elif Party[0] == EmmaX:
                ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."
            elif Party[0] == LauraX:
                $ LauraX.change_face("sly", 2)
                ch_l "Heh, got you going, right?."
                $ LauraX.change_face("bemused", 1)
            elif Party[0] == JeanX:
                ch_j "Kidding."


            elif Party[0] == JubesX:
                ch_v "I'm, uh. . . I'm kinda done for now. . ."
            $ between_event_count = 0
        return

    if Party[0].legs:

        if Party[0] == StormX or (Party[0].SeenPanties and Party[0].SeenPussy) or (Party[0].underwear and (approval_check(Party[0], 700) or Party[0].SeenPanties)) or approval_check(Party[0], 950):
            $ Party[0].change_stat("lust", 50, 5)
            $ Party[0].change_stat("inhibition", 30, 1)
            $ Party[0].change_stat("inhibition", 50, 1)
            $ Line = Party[0].legs
            $ Party[0].legs = 0
            "She unfastens her [Line] and slides them down her legs."
            if Party[0].underwear:
                if not Party[0].SeenPanties:
                    $ Party[0].change_stat("inhibition", 200, 2)
                    $ Party[0].change_stat("inhibition", 50, 3)
                    $ Party[0].SeenPanties = 1
            else:

                $ Party[0].blushing = 1
                "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                call expression Party[0].Tag + "_First_Bottomless"
        else:
            if Party[0] == RogueX:
                ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].player_petname]. I shouldn't have led you on."
            elif Party[0] == KittyX:
                ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."
            elif Party[0] == EmmaX:
                ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."
            elif Party[0] == LauraX:
                ch_l "Nah, that's all for now."
            elif Party[0] == JeanX:
                ch_j "Kidding."
            elif Party[0] == JubesX:
                ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
            $ between_event_count = 0
        return

    if Party[0].bra:
        if Party[0] == StormX or approval_check(Party[0], 900) or (Party[0].SeenChest and approval_check(Party[0], 600)):
            $ Party[0].change_stat("lust", 60, 5)
            $ Party[0].change_stat("inhibition", 50, 2)
            $ Party[0].change_stat("inhibition", 200, 1)
            $ Line = Party[0].bra
            $ Party[0].bra = 0
            "She pulls her [Line] over her head and tosses it aside."
            if not Party[0].SeenChest:
                $ Party[0].change_stat("inhibition", 200, 3)
                $ Party[0].change_stat("inhibition", 50, 1)
                call expression Party[0].Tag + "_First_Topless"
            $ Player.change_stat("focus", 80, 15)
        else:
            if Party[0] == RogueX:
                ch_r "I know a deal's a deal, but I'd like to keep my top on, ok [Party[0].player_petname]? Sorry about that."
            elif Party[0] == KittyX:
                ch_k "So. . . I know this is a bit late to mention it, but I'd like to keep my top on?"
            elif Party[0] == EmmaX:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Hmm. . . better than I thought."
                $ EmmaX.change_face("sly", 1)
                ch_e "But I doubt you're ready for this yet."
            elif Party[0] == LauraX:
                ch_l "Yeah, that's enough for now."
            elif Party[0] == JeanX:
                ch_j "Kidding."
            elif Party[0] == JubesX:
                ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
            $ between_event_count = 0
        return

    if Party[0].underwear:
        if Party[0] == StormX or approval_check(Party[0], 950) or (Party[0].SeenPussy and approval_check(Party[0], 600)):
            $ Party[0].change_stat("lust", 70, 10)
            $ Party[0].change_stat("inhibition", 70, 2)
            $ Party[0].change_stat("inhibition", 200, 2)
            $ Line = Party[0].underwear
            $ Party[0].underwear = 0
            "She slides her [Line] off, leaving her pussy bare."
            if not Party[0].SeenPussy:
                $ Party[0].change_stat("inhibition", 50, 4)
                $ Party[0].change_stat("inhibition", 200, 4)
                call expression Party[0].Tag + "_First_Bottomless"
            $ Player.change_stat("focus", 75, 20)
        else:
            if Party[0] == RogueX:
                ch_r "Look, this has gone a bit far, [Party[0].player_petname]. I'd like to call it a night."
            elif Party[0] == KittyX:
                ch_k "Wow, I. . . I'm not really ready for this sort of thing, I'm sorry!"
            elif Party[0] == EmmaX:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Hmm. . . better than I thought."
                $ EmmaX.change_face("sly", 1)
                ch_e "But I doubt you're ready for this yet."
            elif Party[0] == LauraX:
                $ LauraX.change_face("perplexed", 2)
                ch_l "I think you've had enough."
                $ LauraX.change_face("perplexed", 1)
            elif Party[0] == JeanX:
                ch_j "Kidding."
            elif Party[0] == JubesX:
                ch_v "Yeah, sorry, I don't think I wanna go further than this. . ."
            $ between_event_count = 0
        return

    if Party[0] == RogueX:
        $ KittyX.change_face("sly", 1)
        ch_r "Well, that's another right answer, but I don't have a stitch left to take off. . ."
    elif Party[0] == KittyX:
        ch_k "So. . . you got that one right. . ."
        $ KittyX.eyes = "down"
        ch_k ". . . but I'm not[KittyX.like]wearing anything else. . ."
        $ KittyX.change_face("sly", 1)
    elif Party[0] == EmmaX:
        $ EmmaX.change_face("sly", 1)
        ch_e "Hmm. . . another correct answer. . ."
        $ EmmaX.eyes = "down"
        ch_e ". . . but I don't have anything else to remove. . ."
        $ EmmaX.change_face("sly", 1)
    elif Party[0] == LauraX:
        $ LauraX.change_face("sly", 1)
        ch_l "So. . . you got that one right. . ."
        $ LauraX.eyes = "down"
        ch_l ". . . but it looks like I'm out of clothes. . ."
        $ LauraX.change_face("sly", 1)
    elif Party[0] == JeanX:
        $ JeanX.change_face("sly", 1, Eyes="down")
        ch_j "Well, looks like you got all of them."
        $ JeanX.change_face("sly", 1)
        ch_j "What're you planning to do to me now? . . "
    elif Party[0] == StormX:
        $ StormX.change_face("sly", 1)
        ch_s "Hmm. . . you answer correctly. . ."
        $ StormX.eyes = "down"
        ch_s ". . . but as you can see, I am already naked. . ."
        $ StormX.change_face("sly", 1)
    elif Party[0] == JubesX:
        ch_v "Well, what have we here. . ."
        $ JubesX.change_face("sly", 1, Eyes="down")
        ch_v "I seem to have run out of \"tokens.\" . ."
        $ JubesX.change_face("sly", 1)
        ch_v "And ideas what we could do next?"


    if len(Party) >= 2:
        menu:
            "Well I could think of something else you could do. . .":
                pass
            "It looks like [Party[1].name] has some questions for me. . ." if Party[1].ClothingCheck:

                return
    $ between_event_count = 0
    $ approval_bonus = 50
    call expression Party[0].Tag + "_SexMenu"
    if Party[0] == RogueX:
        ch_r "Well I sure enjoyed that."
    elif Party[0] == KittyX:
        ch_k "I think I learned a few things there. . ."
    elif Party[0] == EmmaX:
        ch_e "I hope you picked up a few things. . ."
    elif Party[0] == LauraX:
        ch_l "Well, better than studying. . ."
    elif Party[0] == JeanX:
        ch_j "Well that killed some time."
    elif Party[0] == StormX:
        ch_s "That was an entertaining diversion. . ."
    elif Party[0] == JubesX:
        ch_v "That's how I like to end an evening of studying. . ."
    $ between_event_count = 0
    return




label Strip_Study_Wrong:
    $ Party[0].change_face("sly", 1)
    if Count == 1:
        if Party[0] == RogueX:
            ch_r "Bzzt, too bad, [RogueX.player_petname]."
        elif Party[0] == KittyX:
            ch_k "Nope."
        elif Party[0] == EmmaX:
            ch_e "Unfortunately. . . no."
        elif Party[0] == LauraX:
            ch_l "What?"
        elif Party[0] == JeanX:
            ch_j "Nope."
        elif Party[0] == StormX:
            ch_s "Hmm. . . I am afraid not."
        elif Party[0] == JubesX:
            ch_v "Ooo, strike -one-. . ."
    elif Count == 2:
        if Party[0] == RogueX:
            ch_r "Oh, you're really not good at this. Come on, you've only got one more shot."
        elif Party[0] == KittyX:
            ch_k "{i}So{/i} close. One more try."
        elif Party[0] == EmmaX:
            ch_e "I'm afraid not, one more try."
        elif Party[0] == LauraX:
            ch_l ". . . how did you even. . ."
        elif Party[0] == JeanX:
            ch_j "Way off."
        elif Party[0] == StormX:
            ch_s "Disappointing. . ."
        elif Party[0] == JubesX:
            ch_v "Ouch, strike -two-, [JubesX.player_petname]. . ."
    elif Count > 2:
        if Party[0] == RogueX:
            ch_r "And you are out of here! Sorry, [RogueX.player_petname], thanks for playing, you're done."
        elif Party[0] == KittyX:
            ch_k "Aw, too bad, so sad. Maybe next time."
        elif Party[0] == EmmaX:
            ch_e "Pity, I expected better of you."
        elif Party[0] == LauraX:
            ch_l "What? Fuck this."
        elif Party[0] == JeanX:
            ch_j "Have you evne been paying attention to your lectures?"
        elif Party[0] == StormX:
            ch_s "Oh, that is unfortunate. No. . ."
        elif Party[0] == JubesX:
            ch_v "Oh -no!- That's strike -three!-"
            ch_v "The crowd does -not- like -that- one. . ."
        $ between_event_count = 0
    return





label Rogue_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_r "Who was the first person who I used my powers on?"
            "A. Colby":
                return 0
            "B. Renly":
                return 0
            "C. Remy":
                return 0
            "D. Cody":
                return 1
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_r "Where did I live before moving to Xaviers?"
            "A. Lousiana":
                return 0
            "B. Mississippi":
                return 1
            "C. Connecticut":
                return 0
            "D. Tennessee":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_r "What was the first power I. . . borrowed?"
            "A. Mystique's shape shifting":
                return 0
            "B. Shadowcat's phasing":
                return 0
            "C. Nightcrawler's teleport":
                return 1
            "D. Cyclops's eyebeams":
                return 0
    if QuizOrder[between_event_count] == 4:
        menu:
            ch_r "What mutant raised me as my parent before my powers manifested."
            "A. Magneto":
                return 0
            "B. Mystique":
                return 1
            "C. Xavier":
                return 0
            "D. Belasco":
                return 0
    if QuizOrder[between_event_count] == 5:
        menu:
            ch_r "I eventually joined the X-Men after Mystique attacked me, where?"
            "A. At school":
                return 0
            "B. At the beach":
                return 0
            "C. In the mountains":
                return 1
            "D. In the bayou":
                return 0
    if QuizOrder[between_event_count] == 6:
        menu:
            ch_r "When Magneto was selecting the fittest mutants for Asteroid M, I was captured after beating which member of the Brotherhood?"
            "A. Blob":
                return 0
            "B. Avalanche":
                return 0
            "C. Toad":
                "That's right, [RogueX.player_petname], I slammed that frog tongue in a car door"
                "Better not make me angry."
                return 1
            "D. Quicksilver":
                return 0


    "She asked an obscure question but you answer the question correctly."
    return 1




label Kitty_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_k "Ok, do you[KittyX.like]know where I come from? What's my home town?"
            "A. Chicago, Illinois":
                return 0
            "B. Deerfield, Illinois":
                return 1
            "C. New York City, New York":
                return 0
            "D. St. Louis, Missouri":
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_k "What's my mutant power called?"
            "A. Disappearing":
                return 0
            "B. Ghosting":
                return 0
            "C. Phasing":
                return 1
            "D. Shifting":
                return 0
    if QuizOrder[between_event_count] == 3:
        ch_k "So. . . don't laugh, but I have this stuffed animal I sleep with[KittyX.like]every night."
        menu:
            ch_k "Know his name?"
            "A. Draco":
                return 0
            "B. Flipper":
                return 0
            "C. Lockheed":
                return 1
            "D. N'gari":
                return 0

    if QuizOrder[between_event_count] == 4:
        ch_k "Okay. Did you know that Dr. McCoy takes a handful of students on a private tutoring retreat?"
        menu:
            ch_k "Know where he takes them?"
            "A. The Great Redwood Forest, California":
                return 1
            "B. Mount McKinley, Alaska":
                return 0
            "C. Mount Rushmore, South Dakota":
                return 0
            "D. Yellowstone National Park, Wyoming":
                return 0
    if QuizOrder[between_event_count] == 5:
        ch_k "One of the worst threats we have to worry about as mutants are the giant robots called Sentinels."
        menu:
            ch_k "Do you know who built them?"
            "A. Arcade":
                return 0
            "B. Bolivar Trask":
                return 1
            "C. Magneto":
                return 0
            "D. Unus the Untouchable":
                return 0
    if QuizOrder[between_event_count] == 6:
        ch_k "Y'know, we didn't always have classes here at the Institute."
        ch_k "For a while, all the students here went to a local public school."
        menu:
            ch_k "Know which one?"
            "A. Bayville High School":
                return 1
            "B. King Memorial High School":
                return 0
            "C. Riverside High School":
                return 0
            "D. Seth Paine High School":
                return 0
    if QuizOrder[between_event_count] == 7:
        menu:
            ch_k "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
            "A. Jean Grey":
                return 0
            "B. Lance Alvers":
                return 1
            "C. Mystique":
                return 0
            "D. Professor Xavier":
                return 0
    if QuizOrder[between_event_count] == 8:
        ch_k "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
        ch_k "Even though it was a lot of fun, we ended up disbanding after that."
        menu:
            ch_k "Anyway, know what the name we chose for the group was?"
            "A. The Bayville Avengers":
                return 0
            "B. The Bayville Brawlers":
                return 0
            "C. The Bayville Harpies":
                return 0
            "D. The Bayville Sirens":
                return 1
    if QuizOrder[between_event_count] == 9:
        menu:
            ch_k "Okay[KittyX.like].not that I'd know, but do you know the remedy for stink bomb aroma?"
            "A. A hot shower":
                return 0
            "B. Methyl Ethyl Ketone":
                return 0
            "C. Isolation":
                return 1
            "D. Tomato Juice":
                return 0
    if QuizOrder[between_event_count] == 10:
        ch_k "When I'm using my powers, I'm not[KittyX.like]{i}totally{/i} invulnerable."
        menu:
            ch_k "Who has powers that can still affect me?"
            "A. Blob":
                return 0
            "B. Magneto":
                return 0
            "C. Quicksilver":
                return 0
            "D. Scarlet Witch":
                return 1


    "She asked an obscure question but you answer the question correctly."
    return 1


label Emma_Quiz_Question:
    ch_e "Question [between_event_count]. . ."
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_e "So, do you know where I lived as a child?"
            "A. Manchester, England":
                return 0
            "B. New York City, New York":
                return 0
            "C. Boston, Massachusetts":
                return 1
            "D. London, England":
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_e "What's my mutant power?"
            "A. Telekinesis":
                return 0
            "B. Ice Powers":
                return 0
            "C. Telepathy":
                return 1
            "D. Baking":
                return 0
    if QuizOrder[between_event_count] == 3:
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was the name of that club?"
            "A. Akatsuki":
                return 0
            "B. The Pride":
                return 0
            "C. The Hellfire Club":
                return 1
            "D. The Sinister Six":
                return 0

    if QuizOrder[between_event_count] == 4:
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was my title in that organization?"
            "A. The Black Queen":
                return 0
            "B. The White Queen":
                return 1
            "C. The Red Queen":
                return 0
            "D. Princess Powerful":
                return 0
    if QuizOrder[between_event_count] == 5:
        ch_e "I have some clones wandering around. . . somewhere."
        menu:
            ch_e "What are they called?"
            "A. Kagebunshin":
                return 0
            "B. The Stepford Cuckoos":
                return 1
            "C. Jamie Maddrox":
                return 0
            "D. The Spice Girls":
                return 0
    if QuizOrder[between_event_count] == 6:
        menu:
            ch_e "What is it called when a mutant develops a new ability, unrelated to their original one?"
            "A. Secondary Mutation":
                return 1
            "B. Level-Up":
                return 0
            "C. Digivolution":
                return 0
            "D. Super-Mutant":
                return 0
    if QuizOrder[between_event_count] == 7:
        ch_e "I used to teach on an island nation of all mutants."
        menu:
            ch_e "What was it called?"
            "A. Australia":
                return 0
            "B. Genosha":
                return 1
            "C. Martinique":
                return 0
            "D. Whole Cake Island":
                return 0
    if QuizOrder[between_event_count] == 8:
        menu:
            ch_e "When we first met, how did I trim my pubic hair?"
            "A. Left natural":
                return 0
            "B. Shaved into an \"X\"":
                return 0
            "C. I don't know":
                $ EmmaX.change_face("sadside", 1)
                if not EmmaX.SeenPussy:
                    ch_e "Boo, I thought you might at least take a guess. . ."
                else:
                    ch_e "Clearly you weren't paying enough attention."
                $ EmmaX.change_face("normal")
                return 0
            "D. Waxed clean":
                $ EmmaX.change_face("sly", 1)
                ch_e "Someone was paying attention. . ."
                return 1
    if QuizOrder[between_event_count] == 9:
        menu:
            ch_e "name one of my horrible sisters."
            "A. Drucilla":
                return 0
            "B. Elsa":
                return 0
            "C. Adrienne":
                return 1
            "D. Cordelia":
                return 1
    if QuizOrder[between_event_count] == 10:
        menu:
            ch_e "My previous teaching experience was at which Ivy League school?"
            "A. Deerfield Community College":
                return 0
            "B. Princeton":
                return 0
            "C. Empire State University":
                return 0
            "D. The Massachusetts Academy":
                return 1


    "She asked an obscure question but you answer the question correctly."
    return 1



label Laura_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_l "I don't know. . . what color are my eyes?"
            "A. Blue":
                return 0
            "B. Green":
                return 1
            "C. Brown":
                return 0
            "D. Red":
                return 0
    if QuizOrder[between_event_count] == 2:
        $ LauraX.change_face("perplexed",1,Eyes="side")
        ch_l "Um. . ."
        $ LauraX.change_face("sly")
        menu:
            ch_l "Say my name."
            "A. [LauraX.petname]":
                ch_l "Close enough."
                return 1
            "B. Esme":
                return 0
            "C. Laura":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_l "What do you think about my ass?"
            "A. Kind of flat?":
                return 0
            "B. Tight?":
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                return 0

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_l "What number am I thinking of?"
            "A. 23?":
                $ LauraX.change_face("surprised")
                ch_l "How did you guess?"
                $ LauraX.change_face("sly")
                return 1
            "B. 2?":
                $ LauraX.change_face("sly")
                ch_l "Mmmm, you and me?"
                return 1
            "C. 8?":
                $ LauraX.change_face("perplexed")
                ch_l ". . . What? Why?"
                $ LauraX.change_face("bemused")
                return 0
            "D. Green?":
                ch_l ". . ."
                return 0









































































    ch_l ". . . I can't think of anything, skip my turn."
    return 1





label Jean_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_j "I don't know. . . what color are my eyes?"
            "A. Blue":
                return 0
            "B. Green":
                return 1
            "C. Brown":
                return 0
            "D. Red":
                return 0
    if QuizOrder[between_event_count] == 2:
        $ JeanX.change_face("perplexed",1,Eyes="side")
        ch_j "Um. . ."
        $ JeanX.change_face("sly")
        menu:
            ch_j "Say my name."
            "A. [JeanX.petname]":
                ch_j "Close enough."
                return 1
            "B. Esme":
                return 0
            "C. Jean":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_j "What do you think about my ass?"
            "A. Kind of flat?":
                return 0
            "B. Tight?":
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                return 0

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_j "What number am I thinking of?"
            "A. 3?":
                $ JeanX.change_face("surprised")
                ch_j "No?"
                $ JeanX.change_face("sly")
                return 0
            "B. 2?":
                $ JeanX.change_face("sly")
                ch_j "Mmmm, you and me?"
                return 1
            "C. 8?":
                $ JeanX.change_face("perplexed")
                ch_j ". . . What? Why?"
                $ JeanX.change_face("bemused")
                return 0
            "D. Green?":
                ch_j ". . ."
                return 0









































































    ch_j ". . . I can't think of anything, skip my turn."
    return 1

label Storm_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_s "So what color are my eyes?"
            "A. Blue":
                return 1
            "B. Green":
                return 0
            "C. Brown":
                return 0
            "D. White?":
                ch_s ". . . sometimes."
                return 1
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_s "Where was I born?"
            "A. Kenya":
                return 0
            "B. New York":
                return 1
            "C. Egypt":
                return 0
            "D. Honolulu":
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_s "What do you think about my body?"
            "A. Kind of flat?":
                $ StormX.change_face("confused")
                return 0
            "B. Thicc?":
                $ Party[0].change_stat("love", 80, 2)
                $ Party[0].change_stat("inhibition", 80, 2)
                return 1
            "C. Hot?":
                return 1
            "D. I don't know?":
                ch_s "A fair response."
                return 1

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_j "In what city was I a thief?"
            "A. Detroit?":
                return 0
            "B. Rome?":
                return 0
            "C. New York?":
                return 0
            "D. Cairo?":
                return 1









































































    "She asked an obscure question but you answer the question correctly."
    return 1




label Jubes_Quiz_Question:
    if QuizOrder[between_event_count] == 1:
        menu:
            ch_v "Where did I grow up?"
            "A. Hong Kong":
                ch_v "My -parents,- maybe. . ."
                return 0
            "B. Beverly Hills":
                return 1
            "C. Shenzhen":
                return 0
            "D. Bel Air":
                ch_v "So close. . ."
                return 0
    if QuizOrder[between_event_count] == 2:
        menu:
            ch_v "What is my full first name?"
            "A. Jubilation":
                if JubesX.name == "Jubilation":
                    ch_v "Ok, that one was too easy."
                return 1
            "B. Jubal":
                return 0
            "C. Jubilant":
                return 0
            "D. Jabroni":
                ch_v ". . . no."
                return 0
    if QuizOrder[between_event_count] == 3:
        menu:
            ch_v "Where did I live after losing my parents?"
            "A. With your uncle Bruce":
                return 0
            "B. In an abandoned building":
                return 0
            "C. In a cave lair":
                ch_v "No, the vampire thing came later."
                return 0
            "D. In a mall":
                return 1

    if QuizOrder[between_event_count] == 4:
        menu:
            ch_v "What sport did I do growing up?"
            "A. Baseball":
                $ JubesX.change_face("surprised")
                ch_v "Ok, maybe I sent some bad cues on this one?"
                $ JubesX.change_face("sly")
                return 0
            "B. Figure Skating":
                return 0
            "C. Gymnastics":
                ch_v "Why yes it was. . ."
                ch_v "I'm still quite flexible. . ."
                return 1
            "D. Shotput":
                ch_v ". . ."
                return 0


    "She asks you some other tricky questions, but you manage to get them right."
    return 1







label Emma_StripStudy_Intro:
    if Party[0] != EmmaX:
        $ Party.reverse()
    call shift_focus (Party[0])
    if not EmmaX.top and not EmmaX.legs:

        $ EmmaX.change_face("sly")
        ch_e "I was considering some way of. . . motivating you. . ."
        $ EmmaX.eyes = "down"
        ch_e "but but I suppose we're already past that. . ."
        $ EmmaX.eyes = "squint"
        ch_e "Do you have any ideas?"
        call Emma_SexMenu
    else:
        "[EmmaX.name] moves a bit closer to you. . ."
        ch_e "I was curious, [EmmaX.player_petname]. . ."
        ch_e "do you feel that a little \"motivation\" might help you to learn?"
        if "stripstudy" not in EmmaX.history:
            menu:
                extend ""
                "What sort of motivation?":
                    if "frisky" not in EmmaX.history:
                        $ EmmaX.change_face("sly")
                        $ Line = "ask"
                    else:
                        $ EmmaX.change_stat("obedience", 80, 3)
                        $ EmmaX.change_face("confused",1)
                        "She strokes at the edges of her clothes."
                        ch_e "You aren't going to make me say it, are you. . ."
                        menu:
                            extend ""
                            "Um. . . oh, OH! Yeah, sounds good. [[Strip tutoring]":
                                $ Line = "strip"
                            "Looks like I am. . .":
                                if approval_check(EmmaX, 500, "O"):
                                    $ EmmaX.change_stat("obedience", 80, 5)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ EmmaX.change_face("sly", 2)
                                    $ Line = "ask"
                                elif approval_check(EmmaX, 500, "LO"):
                                    $ EmmaX.change_face("confused", 2)
                                    $ EmmaX.change_stat("love", 70, -5)
                                    $ EmmaX.change_stat("obedience", 80, 5)
                                    ch_e "Very well. . ."
                                    $ Line = "ask"
                                else:
                                    $ EmmaX.change_stat("love", 200, -5)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ EmmaX.change_face("angry", 1)
                                    ch_e "Oh, never mind then."
                            ". . .":
                                if approval_check(EmmaX, 400, "O"):
                                    $ EmmaX.change_face("confused", 2)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ Line = "ask"
                                elif approval_check(EmmaX, 500, "LO"):
                                    $ EmmaX.change_face("confused", 1, Brows="angry")
                                    $ EmmaX.change_stat("obedience", 50, 5)
                                    $ EmmaX.change_stat("inhibition", 50, 5)
                                    $ Line = "ask"
                                else:
                                    $ EmmaX.change_stat("love", 200, -5)
                                    $ EmmaX.change_stat("inhibition", 50, -5)
                                    $ EmmaX.change_face("angry", 1)
                                    ch_e "Oh, never mind then."

                "I think it might." if "frisky" in EmmaX.history:
                    $ EmmaX.change_face("sly")
                    $ EmmaX.change_stat("love", 80, 5)
                    $ EmmaX.change_stat("obedience", 80, 3)
                    $ EmmaX.change_stat("inhibition", 50, 5)
                    ch_e "I was hoping you would. . ."
                    $ Line = "strip"
                "No, I've got this.":
                    $ EmmaX.change_face("confused", Eyes="side")
                    if "frisky" in EmmaX.history:
                        $ EmmaX.change_stat("love", 200, -10)
                        $ EmmaX.change_stat("obedience", 80, 5)
                        $ EmmaX.change_stat("inhibition", 50, -5)
                    else:
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("inhibition", 50, -5)
                    ch_e "Oh. . . Very well then."
                    $ EmmaX.change_face("confused")
            if Line == "ask":
                ch_e "Well, perhaps I could quiz you about mutant psychology. . ."
                $ EmmaX.eyes = "side"
                ch_e "and, perhaps, if you were to get a question right. . ."
                $ EmmaX.eyes = "squint"
                ch_e "I could. . ."
                menu:
                    extend ""
                    "Take off some clothes?":
                        $ EmmaX.change_stat("inhibition", 50, 5)
                        ch_e "Yes."
                        $ Line = "strip"
                    "Yes? . .":
                        if approval_check(EmmaX, 500, "O"):
                            $ EmmaX.change_face("confused", 2)
                            if "frisky" in EmmaX.history:
                                $ EmmaX.change_stat("love", 200, -5)
                                $ EmmaX.change_stat("obedience", 80, 10)
                            else:
                                $ EmmaX.change_stat("obedience", 80, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            $ Line = "ask"
                        elif approval_check(EmmaX, 500, "LO"):
                            $ EmmaX.change_face("confused", 1, Brows="angry")
                            if "frisky" in EmmaX.history:
                                $ EmmaX.change_stat("love", 200, -5)
                                $ EmmaX.change_stat("obedience", 80, 5)
                            else:
                                $ EmmaX.change_stat("obedience", 80, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            $ Line = "ask"
                    ". . .":
                        if approval_check(EmmaX, 500, "O"):
                            $ EmmaX.change_face("confused", 2)
                            if "frisky" in EmmaX.history:
                                $ EmmaX.change_stat("obedience", 50, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            else:
                                $ EmmaX.change_stat("obedience", 50, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            $ Line = "ask"
                        elif approval_check(EmmaX, 500, "LO"):
                            $ EmmaX.change_face("confused", 1, Brows="angry")
                            if "frisky" in EmmaX.history:
                                $ EmmaX.change_stat("love", 200, -5)
                                $ EmmaX.change_stat("obedience", 50, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            else:
                                $ EmmaX.change_stat("obedience", 50, 5)
                                $ EmmaX.change_stat("inhibition", 50, -5)
                            $ Line = "ask"
                if Line == "ask":
                    $ EmmaX.change_face("bemused", Eyes="side")
                    ch_e "Take off some clothes. . ."
                    $ Line = "strip"
                $ EmmaX.change_face("sly", Brows="confused")
                menu:
                    ch_e "Would that interest you?"
                    "Definitely!":
                        $ EmmaX.change_face("sly",Mouth="smile")
                        $ EmmaX.change_stat("love", 50, 5)
                        $ EmmaX.change_stat("love", 80, 5)
                        $ EmmaX.change_stat("inhibition", 50, 5)
                    "Yeah.":
                        $ EmmaX.change_face("sly")
                        $ EmmaX.change_stat("love", 80, 3)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                    "No thanks.":
                        if "frisky" in EmmaX.history:
                            $ EmmaX.change_stat("love", 200, -10)
                            $ EmmaX.change_stat("obedience", 80, 10)
                            $ EmmaX.change_stat("inhibition", 50, -5)
                        else:
                            $ EmmaX.change_stat("love", 200, -5)
                            $ EmmaX.change_stat("obedience", 80, 5)
                            $ EmmaX.change_stat("inhibition", 50, -5)
                        $ EmmaX.change_face("angry")
                        ch_e "Hrm."
                        $ Line = "no"

        if Line == "strip":
            $ EmmaX.change_face("sly", 0)
            if len(Party) >= 2:
                ch_e "And you, [Party[1].name]? Care to participate?"
                call Date_Sex_Break (EmmaX, Party[1])
                if _return == 4:

                    ch_e "Well I suppose we can. . . postone that."
                    return
                elif _return == 3:

                    ch_e "Well I suppose that answers that."
                    $ counter = 3
                elif _return == 2:

                    ch_e "I suppose you can just watch then. . ."
                    $ counter = 3
                elif _return == 1 and len(Party) >= 2:
                    if Party[1] == RogueX:
                        ch_r "I guess I could join in."
                    elif Party[1] == KittyX:
                        ch_k "It could be fun. . ."
                    elif Party[1] == LauraX:
                        ch_l "Yeah, ok. . ."
            return 1
        else:
            return 0
    return 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc