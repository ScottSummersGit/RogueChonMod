init python:

    def check_girl(Girl, local = False):
        global focused_Girl

        if Girl in all_Girls and (not local or bg_current == Check.location):
            return Girl
        elif bg_current == focused_Girl.location:
            return focused_Girl
        else:
            for Girl in all_Girls:
                if bg_current == Girl.location:
                    focused_Girl = Girl

                    return Girl

label check_favorite_actions(Girl = None):
    if Girl:
        $ temp_Girls = [Girl]
    else:
        $ temp_Girls = active_Girls[:]

    python:
        for G in temp_Girls:
            pussy_count = 0
            ass_count = 0
            fondle_count = 0

            handjob_count = G.action_counter["handjob"]
            footjob_count = G.action_counter["footjob"]
            titjob_count = G.action_counter["titjob"]
            blowjob_count = G.action_counter["blowjob"]

            for action in all_actions:
                if action in pussy_actions:
                    pussy_count += G.action_counter[action]

                if action in ass_actions:
                    ass_count += G.action_counter[action]

                if action in fondle_actions:
                    fondle_count += G.action_counter[action]

            if G.player_favorite_action and approval_check(character, 1500):
                if G.player_favorite_action == "handjob":
                    handjob_count += 20
                elif G.player_favorite_action == "footjob":
                    footjob_count += 20
                elif G.player_favorite_action == "titjob":
                    titjob_count += 20
                elif G.player_favorite_action == "blowjob":
                    blowjob_count += 20
                elif G.player_favorite_action == "sex":
                    pussy_count += 20
                elif G.player_favorite_action == "anal":
                    ass_count += 20
                else:
                    fondle_count += 20
            elif G.player_favorite_action and approval_check(character, 800):
                if G.player_favorite_action == "handjob":
                    handjob_count += 5
                elif G.player_favorite_action == "footjob":
                    footjob_count += 5
                elif G.player_favorite_action == "titjob":
                    titjob_count += 5
                elif G.player_favorite_action == "blowjob":
                    blowjob_count += 5
                elif G.player_favorite_action == "sex":
                    pussy_count += 5
                elif G.player_favorite_action == "anal":
                    ass_count += 5
                else:
                    fondle_count += 5

            total = ass_count + pussy_count + blowjob_count + titjob_count + handjob_count + footjob_count + fondle_count + G.action_counter["kiss"]

            if total <= 0:
                D20F = 999
            else:
                D20F = renpy.random.randint(1, total)

            if D20F <= ass_count:
                if G.action_counter["anal"] >= 5:
                    favorite_action = "anal"
                elif G.action_counter["eat_ass"] >= 5:
                    favorite_action = "eat_ass"
                else:
                    favorite_action = "finger_ass"
            elif D20F <= ass_count + pussy_count:
                if G.action_counter["sex"] >= 5:
                    favorite_action = "sex"
                elif G.action_counter["eat_pussy"] >= 5:
                    favorite_action = "eat_pussy"
                else:
                    favorite_action = "fondle_pussy"
            elif D20F <= ass_count + pussy_count + blowjob_count:
                favorite_action = "blowjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count:
                favorite_action = "titjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count:
                favorite_action = "footjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count:
                favorite_action = "handjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count + fondle_count:
                D20F = renpy.random.randint(1, 20)

                if D20F >= 15 and G.action_counter["hotdog"]:
                    favorite_action = "hotdog"
                elif D20F >= 10 and G.action_counter["suck_breasts"]:
                    favorite_action = "suck_breasts"
                elif D20F >= 5 and G.action_counter["fondle_breasts"]:
                    favorite_action = "fondle_breasts"
                else:
                    favorite_action = "fondle_thighs"
            else:
                favorite_action = "kiss"

            G.favorite_action = favorite_action

    return

label who_likes_who(Check = 70, D20 = 0):
    $ D20 = renpy.random.randint(0, 1) if not D20 else D20

    $ teacher = 0

    if EmmaX.location == "bg_teacher":
        $ EmmaX.location = "bg_classroom"

        $ teacher = 1
    elif StormX.location == "bg_teacher":
        $ StormX.location = "bg_classroom"

        $ teacher = 2

    python:
        for GA in all_Girls:
            for GB in all_Girls:
                if GA != GB and GA.location == GB.location:
                    if GA.location == "bg_classroom":
                        GA.check_if_likes(GB, 700, 1, 1)
                    elif GA.location == "bg_dangerroom":
                        GA.check_if_likes(GB, 700, 1 + D20, 1)
                    elif GA.location == "bg_showerroom":
                        if GA == EmmaX:
                            GA.check_if_likes(GB, 900, 3, 1)
                        elif GB in [EmmaX, StormX] and GA != LauraX:
                            GA.check_if_likes(GB, 900, 3, 1)
                        else:
                            GA.check_if_likes(GB, 900, 2, 1)
                    else:
                        GA.check_if_likes(GB, Check, D20, 1)

                    if GA == EmmaX:
                        GA.check_if_likes(GB, 1000, int(GB.shame/4), 1)
                    elif GB in [EmmaX, StormX] and GA != LauraX:
                        GA.check_if_likes(GB, 1000, int(GB.shame/4), 1)
                    else:
                        GA.check_if_likes(GB, 1000, int(GB.shame/5), 1)

    if teacher == 2:
        $ StormX.location = "bg_teacher"
    elif teacher:
        $ EmmaX.location = "bg_teacher"

    return

label taboo_check(Character, location = None):
    if location in personal_rooms or location == "hold":
        $ Character.taboo = 0
    elif "locked" in Player.traits and location == bg_current:
        $ Character.taboo = 0
    elif location in ("bg_classroom", "bg_study"):
        if time_index >= 3:
            $ Character.taboo = 10
        elif time_index == 2 or weekday >= 5:
            $ Character.taboo = 30
        else:
            $ Character.taboo = 40
    elif location == "bg_dangerroom":
        if time_index >= 3:
            $ Character.taboo = 20
        else:
            $ Character.taboo = 40
    elif location == "bg_campus" or location == "bg_pool":
        if time_index >= 3:
            $ Character.taboo = 20
        else:
            $ Character.taboo = 40
    elif location == "bg_showerroom":
        $ Character.taboo = 20
    else:
        $ Character.taboo = 40

    if Character == Player:
        $ taboo = Character.taboo

        return

    if Character.taboo >= 20:
        return

    python:
        for G in all_Girls:
            if G != Character:
                if Character.location == G.location and Character.likes[G.tag] <= 700 and not (Character in Player.Harem and G in Player.Harem):
                    Character.taboo = 20

    $ taboo = Character.taboo if (Character.taboo > taboo and bg_current == Character.location) else taboo

    return

label are_girls_angry(Girls = 0):
    $ approval_bonus = 0

    python:
        for G in all_Girls:
            if G.location == bg_current and "_angry" in G.recent_history:
                if bg_current == G.home:
                    if G == RogueX:
                        renpy.say(ch_r, "You should get out, I'm fix'in ta throw down.")
                    elif G == KittyX:
                        renpy.say(ch_k, "You should get out of here, I can't even look at you right now.")
                    elif G == EmmaX:
                        renpy.say(ch_e, "You should leave, or do you want to test me?")
                    elif G == LauraX:
                        renpy.say(ch_l, "You should leave.")
                    elif G == JeanX:
                        renpy.say(ch_j, "Out, NOW!")
                    elif G == StormX:
                        renpy.say(ch_s, "Out!")
                    elif G == JubesX:
                        renpy.say(ch_v, "Get out!")

                    renpy.say(None, "You head back to your room.")

                    Party = []

                    renpy.pop_call()
                    renpy.jump(player_room_entry)
                else:
                    G.location = G.home

                if G in Party:
                    Party.remove(G)

                if Girls:
                    renpy.say(None, ". . . and so does [G.name].")
                else:
                    renpy.say(None, "[G.name] storms off.")

                    if G == StormX:
                        renpy.say(None, ". . . so to speak.")

                Girls += 1

                if G == RogueX:
                    renpy.hide(Rogue_sprite)
                elif G == KittyX:
                    renpy.hide(Kitty_sprite)
                elif G == EmmaX:
                    renpy.hide(Emma_Sprite)
                elif G == LauraX:
                    renpy.hide(Laura_Sprite)
                elif G == JeanX:
                    renpy.hide(Jean_Sprite)
                elif G == StormX:
                    renpy.hide(Storm_Sprite)
                elif G == JubesX:
                    renpy.hide(Jubes_Sprite)

                renpy.with_statement(easeoutleft)

    return

label check_who_is_present(hold = True):
    while len(Party) > 2:
        $ Party.remove(Party[2])

    $ Present = Party[:] if Party else []

    $ temp_Girls = all_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    python:
        for G in temp_Girls:
            if G not in Present and G.location == bg_current:
                Present.append(G)

    while len(Present) > 2:
        call remove_girl(Present[2], hold = hold)

    if Present and focused_Girl not in Present:
        $ renpy.random.shuffle(Present)

        call shift_focus(Present[0])

    python:
        for G in Present:
            if G in Nearby:
                Nearby.remove(G)

            G.location = bg_current

    return

label check_addiction:
    $ temp_Girls = active_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    if JubesX in temp_Girls and JubesX.addiction >= 40 and JubesX.resistance:
        $ temp_Girls.remove(JubesX)

        if "sunshine" not in JubesX.history or "addiction" in JubesX.daily_history:
            pass
        elif bg_current == JubesX.home or bg_current == "bg_player":
            if not JubesX.resistance:
                call addiction_event(JubesX)
            else:
                call addiction_fix(JubesX)
        else:
            if "asked_to_meet" in JubesX.daily_history:
                pass
            elif "asked_to_meet" in JubesX.daily_history and JubesX.addiction >= 60:
                "[JubesX.name] texts you. . ."

                JubesX.voice "I know I asked to meet you in your room earlier, but I really need a fix."

                $ Player.add_word(1,"asked_for_fix",0,0,0)
                $ JubesX.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                call return_to_room

                return
            else:
                "[JubesX.name] texts and asks if you could get her a fix later."

                $ JubesX.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                call return_to_room

                return

    python:
        for G in temp_Girls:
            if "locked" in Player.traits and G.location != bg_current:
                pass
            elif "asked_for_fix" in Player.daily_history and "asked_to_meet" not in G.daily_history:
                pass
            elif G.event_happened[3]:
                pass
            elif "_angry" not in G.recent_history and "addiction" not in G.daily_history and G.remaining_actions >= 1:
                if (G.addiction >= 60 or (G.addiction >= 40 and G == JubesX)) and G.resistance:
                    if bg_current == G.home or bg_current == "bg_player":
                        renpy.call("addiction_fix", G)
                    else:
                        if "asked_to_meet" in G.recent_history:
                            pass
                        elif "asked_to_meet" in G.daily_history and G.addiction >= 80:
                            renpy.say(None, "[G.name] texts you. . .")
                            renpy.say(G.voice, "I know I asked to meet you in your room earlier, but I'm serious, this is important.")

                            Player.add_word(1,"asked_for_fix",0,0,0)

                            G.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                            renpy.call("return_to_room")
                            renpy.return_statement()
                        else:
                            "[G.name] texts and asks if you could meet her in your room later."

                            G.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                            renpy.call("return_to_room")
                            renpy.return_statement()
                elif G.resistance:
                    pass
                elif G == JubesX and G.addiction < 50:
                    pass
                elif (G.addiction >= 35 and not G.event_happened[1]) or (G.addiction >= 60 and G.event_happened[1] <= 2) or G.addiction >= 90:
                    if bg_current == G.home or bg_current == "bg_player":
                        renpy.call("addiction_event", G)
                    else:
                        if "asked_to_meet" in G.recent_history:
                            pass
                        elif "asked_to_meet" in G.daily_history and G.addiction >= 80:
                            renpy.say(None, "[G.name] texts you. . .")
                            renpy.say(G.voice, "I know I asked to meet you in your room earlier, but I'm serious, this is important.")

                            Player.add_word(1,"asked_for_fix",0,0,0)

                            G.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                            renpy.call("return_to_room")
                            renpy.return_statement()
                        else:
                            renpy.say(None, "[G.name] texts and asks if you could meet her in your room later.")

                            G.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                            renpy.call("return_to_room")
                            renpy.return_statement()

    return

label dildo_check(Girl):
    if "_dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "_dildo" in Girl.inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."

        return False

    return True

label vibrator_check(Girl):
    if "_vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "_vibrator" in Girl.inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return False

    return True












init python:

    def approval_check(Chr = 0, T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0, Alt=[[],0]):
        if Chr not in all_Girls:
            return False

        while Alt[0]:

            if Chr in Alt[0]:
                T = Alt[1] if Alt[1] else T
            Alt[0].remove(Alt[0][0])

        L = Chr.love
        O = Chr.obedience
        I = Chr.inhibition
        Localtaboo = Chr.taboo
        Loc = Chr.location if not Loc else Loc

        if Chr == JeanX and (O <= 800 or JeanX.taboo):

            I = (I - JeanX.IX)

        if Loc == bg_current and C:

            if Chr == LauraX:
                if "mandrill" in Player.traits:
                    if L <= 400:
                        L += 600
                    else:
                        L = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
                elif "purple" in Player.traits:
                    if O <= 400:
                        O += 600
                    else:
                        O = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
                elif "corruption" in Player.traits:
                    if I <= 400:
                        I += 600
                    else:
                        I = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
            else:
                if "mandrill" in Player.traits:
                    if L <= 500:
                        L += 500
                    else:
                        L = 1000
                elif "purple" in Player.traits:
                    if O <= 500:
                        O += 500
                    else:
                        O = 1000
                elif "corruption" in Player.traits:
                    if I <= 500:
                        I += 500
                    else:
                        I = 1000

        if Type == "LOI":
            Localtaboo = Localtaboo*10
            Localapproval_bonus = approval_bonus*10

        elif Type == "LO":


            I = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "OI":
            L = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "LI":
            O = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6

        elif Type == "L":
            O = 0
            I = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "O":
            L = 0
            I = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "I":
            O = 0
            L = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3

        else:
            Localtaboo = Localtaboo*10
            Localapproval_bonus = approval_bonus*10

        TabM = 0 if TabM <= 0 else TabM

        if Check:

            Check = (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo))
            return Check

        if (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= (T + (2*Spread)):

            return 3
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= (T + Spread):

            return 2
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= T:

            return True
        else:
            return False




    def Room_Full(Here = [],temp_Girls=[]):


        global Party
        Here = []
        while len(Party) > 2:


            Party.remove(Party[2])




        temp_Girls = all_Girls[:]
        while temp_Girls:
            if temp_Girls[0].location == bg_current and temp_Girls[0] not in Party:
                Here.append(temp_Girls[0])
            temp_Girls.remove(temp_Girls[0])
        if len(Party) + len(Here) >= 2:
            return True
        else:
            return False



    def AloneCheck(Girl=0,temp_Girls=[]):


        temp_Girls = all_Girls[:]
        if Girl and Girl in all_Girls:
            temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                return False
            temp_Girls.remove(temp_Girls[0])
        return True





label CheatCheck(temp_Girls=[], temp_Girls2=[]):







    $ temp_Girls = all_Girls[:]
    $ renpy.random.shuffle(temp_Girls)
    while temp_Girls:
        if "locked" in Player.traits and temp_Girls[0].location != bg_current:

            pass
        else:
            $ temp_Girls2 = all_Girls[:]
            while temp_Girls2:
                if "meet girl" in Player.daily_history:

                    return
                elif temp_Girls[0] in Player.Harem:

                    if "saw with " + temp_Girls2[0].tag in temp_Girls[0].traits:

                        if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:

                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag,0,0,1)
                        elif temp_Girls[0] in Player.Harem and temp_Girls2[0].tag + "Yes" in Player.traits:
                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag,0,0,1)
                        elif bg_current == "bg_player" or bg_current == temp_Girls[0].home:
                            call Cheated (temp_Girls[0], temp_Girls2[0])
                            $ renpy.pop_call()
                            return
                $ temp_Girls2.remove(temp_Girls2[0])
        $ temp_Girls.remove(temp_Girls[0])
    return

label ShareCheck(temp_Girls=[], temp_Girls2=[]):





    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(StormX)
    while temp_Girls:
        if temp_Girls[0] in Player.Harem:

            $ temp_Girls2 = all_Girls[:]
            $ temp_Girls2.remove(StormX)
            while temp_Girls2:
                if "ask " + temp_Girls2[0].tag in temp_Girls[0].traits:

                    if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:

                        $ temp_Girls[0].drain_word("ask "+temp_Girls2[0].tag,0,0,1)
                    else:
                        call Share (temp_Girls[0], temp_Girls2[0])
                        $ renpy.pop_call()
                        return
                $ temp_Girls2.remove(temp_Girls2[0])
        $ temp_Girls.remove(temp_Girls[0])
    return
