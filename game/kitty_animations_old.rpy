

image Kitty_Squint:
    "images/KittySprite/Kitty_sprite_eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittySprite/Kitty_sprite_eyes_Squint.png"
    .25
    repeat


image Kitty_Drip_Mask:

    contains:
        "images/KittySprite/Kitty_sprite_WetMask.png"
        offset (-225,-560)

image Kitty_Drip_MaskP:

    contains:
        "images/KittySprite/Kitty_sprite_WetMaskP.png"
        offset (-225,-560)




















image Kitty_SexSprite:
    LiveComposite(
        (1120,840),
        (0,0), ConditionSwitch(

                "not Player.Sprite", "Kitty_Sex_Body_animation0",
                "Player.Cock == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Body_animation3",
                        "action_speed >= 2", "Kitty_Sex_Body_animation2",
                        "action_speed", "Kitty_Sex_Body_animation1",
                        "True", "Kitty_Sex_Body_animation0",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Body_animation3",
                        "action_speed >= 2", "Kitty_Sex_Body_animation2",
                        "action_speed", "Kitty_Sex_Body_animation1",
                        "True", "Kitty_Sex_Body_animation0",
                        ),
                "Player.Cock == 'footjob'", ConditionSwitch(

                        "action_speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "action_speed", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Kitty_Hotdog_Body_animation2",
                "True", "Kitty_Sex_Body_animation0",
                ),
        (0,0), ConditionSwitch(
                "not Player.Sprite", "Kitty_Sex_Legs_animation0",
                "Player.Cock == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Legs_animation3",
                        "action_speed >= 2", "Kitty_Sex_Legs_animation2",
                        "action_speed", "Kitty_Sex_Legs_animation1",
                        "True", "Kitty_Sex_Legs_animation0",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Legs_animation3",
                        "action_speed >= 2", "Kitty_Sex_Legs_animation2",
                        "action_speed", "Kitty_Sex_Legs_animation1",
                        "True", "Kitty_Sex_Legs_animation0",
                        ),
                "Player.Cock == 'footjob'", ConditionSwitch(

                        "action_speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "action_speed", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Kitty_Hotdog_Legs_animation2",
                "True", "Kitty_Sex_Legs_animation0",
                ),
        )
    align (0.6,0.0)
    pos (650,230)
    zoom 0.7

image Kitty_Sex_Body_animation0:
    contains:
        "Kitty_Sex_Body"
    pos (650,230)

image Kitty_Sex_Legs_animation0:
    contains:
        "Kitty_Sex_Legs"
    pos (650,230)

image Kitty_Sex_Body = LiveComposite(

        (1120,840),
        (260,-350), "Kitty_HairBack_Sex",

        (0,0), ConditionSwitch(

            "KittyX.outfit['front_inner_accessory'] == '_barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",
            "KittyX.outfit['front_inner_accessory'] == '_ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",
            "True", "images/KittySex/Kitty_Sex_Body.png",
            ),
        (260,-350), "Kitty_Head_Sex",

        (0,0), ConditionSwitch(

            "KittyX.outfit['neck'] == '_gold_necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "KittyX.outfit['neck'] == '_star_necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "KittyX.outfit['neck'] == '_flower_necklace'", "images/KittySex/Kitty_Sex_Neck_Flower.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['bottom'] == '_dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Waist.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.outfit['bra']", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.outfit['bra'] == '_dress'", "images/KittySex/Kitty_Sex_Under_Dress.png",
                    "KittyX.outfit['bra'] == '_cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
                    "KittyX.outfit['bra'] == '_sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
                    "KittyX.outfit['bra'] == '_bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
                    "KittyX.outfit['bra'] == '_bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini.png",
                    "KittyX.outfit['bra'] == '_lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
                    "True", Null(),
                    ),
            "KittyX.outfit['top']", ConditionSwitch(

                    "KittyX.outfit['bra'] == '_dress'", "images/KittySex/Kitty_Sex_Under_Dress_UpS.png",
                    "KittyX.outfit['bra'] == '_cami'", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png",
                    "KittyX.outfit['bra'] == '_bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.outfit['bra'] == '_sports_bra' and KittyX.outfit['top'] == '_red_shirt'", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png",
                    "KittyX.outfit['bra'] == '_sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.outfit['bra'] == '_dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
                    "KittyX.outfit['bra'] == '_cami'", "images/KittySex/Kitty_Sex_Under_Cami_Up.png",
                    "KittyX.outfit['bra'] == '_sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "KittyX.outfit['bra'] == '_bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
                    "KittyX.outfit['bra'] == '_bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.outfit['bra'] == '_lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittySex/Kitty_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.outfit['top']", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.outfit['top'] == '_jacket'", "images/KittySex/Kitty_Sex_Over_Jacket.png",
                    "KittyX.outfit['top'] == '_pink_top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",
                    "KittyX.outfit['top'] == '_red_shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",
                    "KittyX.outfit['top'] == '_towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.outfit['top'] == '_jacket'", "images/KittySex/Kitty_Sex_Over_Jacket_Up.png",
                    "KittyX.outfit['top'] == '_pink_top' and KittyX.outfit['bra'] == '_sports_bra'", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png",
                    "KittyX.outfit['top'] == '_pink_top'", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png",
                    "KittyX.outfit['top'] == '_red_shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png",

                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.outfit['bra'] or not KittyX.outfit['top'] or not KittyX.top_pulled_up", Null(),

            "KittyX.outfit['bra'] == '_dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
            "KittyX.outfit['bra'] == '_bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
            "KittyX.outfit['bra'] == '_lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "KittyX.spunk['belly']", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "KittyX.spunk['breasts']", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'suck_breasts' or offhand_action == 'suck_breasts'", "Kitty_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Kitty_Sex_Fondle_Breasts",
            "True", Null()
            ),
        )

image Kitty_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.6
    offset (450,210)

image Kitty_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.1
    offset (320,-180)

image Kitty_Head_Sex:

    "Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

image Kitty_HairBack_Sex:

    "Kitty_HairBack"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10


image Kitty_Sex_Legs:
    LiveComposite(

        (1120,840),
        (0,0), ConditionSwitch(
            "KittyX.outfit['bottom'] == '_dress' and KittyX.upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png",
            "KittyX.outfit['bottom'] == '_dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png",
            "KittyX.outfit['bottom'] == '_blue_skirt'", "images/KittySex/Kitty_Sex_Skirt_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittySex/Kitty_Sex_Legs.png",
        (0,0), ConditionSwitch(
            "KittyX.wet", "images/KittySex/Kitty_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Kitty_Sex_Anus",

        (0,0), "Kitty_Sex_Pussy",

        (0,0), ConditionSwitch(
            "KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['underwear'] == '_green_panties' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png",
            "KittyX.outfit['underwear'] == '_green_panties'", "images/KittySex/Kitty_Sex_Panties_Green.png",
            "KittyX.outfit['underwear'] == '_lace_panties' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png",
            "KittyX.outfit['underwear'] == '_lace_panties'", "images/KittySex/Kitty_Sex_Panties_Lace.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms'", "images/KittySex/Kitty_Sex_Panties_Bikini.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_StockingGarter_Legs.png",
            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittySex/Kitty_Sex_Hose_Garter_Legs.png",
            "KittyX.outfit['hose'] == '_stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_Legs.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_pantyhose'", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Legs.png",

            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            "KittyX.outfit['bottom'] == '_dress' and KittyX.upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png",
            "KittyX.outfit['bottom'] == '_dress'", "images/KittySex/Kitty_Sex_Legs_Dress.png",
            "KittyX.outfit['bottom'] == '_blue_skirt'", "images/KittySex/Kitty_Sex_Skirt.png",
            "KittyX.upskirt", Null(),
            "KittyX.outfit['bottom'] == '_capris' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png",
            "KittyX.outfit['bottom'] == '_capris'", "images/KittySex/Kitty_Sex_Pants_Blue.png",
            "KittyX.outfit['bottom'] == '_black_jeans' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png",
            "KittyX.outfit['bottom'] == '_black_jeans'", "images/KittySex/Kitty_Sex_Pants_Black.png",
            "KittyX.outfit['bottom'] == '_shorts' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Shorts_Wet.png",
            "KittyX.outfit['bottom'] == '_shorts'", "images/KittySex/Kitty_Sex_Shorts.png",
            "KittyX.outfit['bottom'] == '_yoga_pants' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png",
            "KittyX.outfit['bottom'] == '_yoga_pants'", "images/KittySex/Kitty_Sex_Pants_Yoga.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "KittyX.outfit['top'] == '_towel' and not KittyX.top_pulled_up", "images/KittySex/Kitty_Sex_Towel_Legs.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            "KittyX.spunk['belly']", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "action_speed >= 2", "Kitty_Hotdog_Zero_animation2",
            "action_speed", "Kitty_Hotdog_Zero_animation1",
            "True", "Kitty_Hotdog_Zero_animation0",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'eat_pussy'", "Kitty_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Kitty_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'footjob'", Null(),
            "action_speed >= 2", "Kitty_Footcock_Zero_animation2",
            "action_speed", "Kitty_Footcock_Zero_animation1",
            "True", "Kitty_Footcock_animation0",
            ),











        (0,0), ConditionSwitch(
            "not action_speed", "Kitty_Sex_Feet",
            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "True", "Kitty_Sex_Feet",
            ),
        )

image Kitty_Sex_Feet = LiveComposite(

        (1120,840),
        (0,0), "images/KittySex/Kitty_Sex_Feet.png",
        (0,0), ConditionSwitch(
            "KittyX.wet", "images/KittySex/Kitty_Sex_Water_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.outfit['bottom'] and not KittyX.upskirt and KittyX.outfit['bottom'] != '_blue_skirt' and KittyX.outfit['bottom'] != '_shorts'",ConditionSwitch(

                    "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.outfit['hose'] == '_stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.outfit['hose'] == '_knee_stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
                    "KittyX.outfit['hose'] == '_pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png",
                    "True", Null(),
                    ),



            "KittyX.outfit['hose'] == '_stockings' or KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",
            "KittyX.outfit['hose'] == '_knee_stockings'", "images/KittySex/Kitty_Sex_Hose_Kneesocks_Feet.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",

            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            "KittyX.upskirt", Null(),
            "KittyX.outfit['bottom'] == '_dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Feet.png",
            "KittyX.outfit['bottom'] == '_capris'", "images/KittySex/Kitty_Sex_Feet_Blue.png",
            "KittyX.outfit['bottom'] == '_black_jeans'", "images/KittySex/Kitty_Sex_Feet_Black.png",
            "KittyX.outfit['bottom'] == '_yoga_pants'", "images/KittySex/Kitty_Sex_Feet_Yoga.png",
            "True", Null(),
            ),
        )

image Kitty_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (530,510)

image Kitty_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.7
    offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image TestingSolid:

    contains:
        Solid("#75d7ec", xysize=(1500,1500))
        alpha 0.2


image Kitty_Pussy_Fucking0:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_animation0", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking1:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_animation1", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking2:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_animation2", "Kitty_Pussy_Fucking_Mask")
image Kitty_Pussy_Fucking3:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_animation3", "Kitty_Pussy_Fucking_Mask")

image Kitty_Pussy_Fucking_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Pussy_Mask.png"

image Kitty_Pussy_Open_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Pussy_Mask.png"
        yoffset 3















image Kitty_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Kitty_Sex_Pussy:

    contains:

        ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                "primary_action == 'eat_pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )
    contains:

        ConditionSwitch(
                "not KittyX.grool", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:

        ConditionSwitch(
                "KittyX.outfit['front_inner_accessory'] != '_ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                )
    contains:

        ConditionSwitch(
                "KittyX.outfit['front_inner_accessory'] != '_barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                "primary_action == 'eat_pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:

        ConditionSwitch(
                "KittyX.spunk[pussy]", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
                "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png",
                "True", Null(),
                ),
    contains:

        ConditionSwitch(
                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 3", AlphaMask("Kitty_Sex_Zero_animation3", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", AlphaMask("Kitty_Sex_Zero_animation2", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed", AlphaMask("Kitty_Sex_Zero_animation1", "Kitty_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Kitty_Sex_Zero_animation0", "Kitty_Pussy_Open_Mask"),
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "not KittyX.spunk['pussy'] or not Player.Sprite or Player.Cock != 'in' or not action_speed", Null(),
                "action_speed <= 1", "Kitty_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )






image Kitty_Sex_Zero_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (498,530)
        zoom 1.4

image Kitty_Sex_Zero_animation1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (498,525)
        zoom 1.4
        block:
            ease 1 pos (498,510)
            pause 1
            ease 3 pos (498,525)
            repeat

image Kitty_Sex_Zero_animation2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,490)
        zoom 1.4
        block:
            ease 1 pos (500,380)
            pause 1
            ease 3 pos (500,490)
            repeat

image Kitty_Sex_Zero_animation3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,490)
        zoom 1.4
        block:
            ease .25 pos (500,380)
            pause .25
            ease 1.5 pos (500,490)
            repeat



image Kitty_Sex_Legs_animation1:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .25
            easein 1 pos (0,-5)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_Sex_Legs_animation2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .5
            easein .5 pos (0,-15)
            ease .25 pos (0,-10)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_Sex_Legs_animation3:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .15
            easein .15 pos (0,-20)
            ease .10 pos (0,-15)
            pause .20
            ease 1.4 pos (0,0)
            repeat



image Kitty_Sex_Body_animation1:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-5)
            pause 1.25
            ease 2.5 pos (0,0)
            repeat

image Kitty_Sex_Body_animation2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .6
            easein .4 pos (0,-10)
            ease .25 pos (0,-5)
            pause 1
            ease 2.75 pos (0,10)
            repeat

image Kitty_Sex_Body_animation3:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .17
            easein .13 pos (0,-20)
            ease .10 pos (0,-15)
            pause .20
            ease 1.4 pos (0,10)
            repeat








image Kitty_Sex_Anus:
    contains:

        ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed", "Kitty_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Kitty_Sex_Anal_Tip",
            "KittyX.used_to_anal", "images/KittySex/Kitty_Sex_Hole_Loose.png",
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png",
            )
    contains:

        ConditionSwitch(
                "not KittyX.spunk['anus']", Null(),
                "Player.Sprite and Player.Cock != 'anal' and action_speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:

        ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "action_speed >= 3",  AlphaMask("Kitty_Anal_Zero_animation3", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed >= 2", AlphaMask("Kitty_Anal_Zero_animation2", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed", AlphaMask("Kitty_Anal_Zero_animation1", "Kitty_Sex_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_animation0", "Kitty_Sex_Anal_Fucking_Mask"),
            )
    contains:

        ConditionSwitch(
                "not KittyX.spunk['anus'] or not Player.Sprite or Player.Cock != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )


image Kitty_Sex_Anal_Fucking0:

    contains:

        "Kitty_Sex_Anal_Tip"
    contains:

        AlphaMask("Kitty_Anal_Zero_animation0", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking1:

    contains:

        "Kitty_Anal_Heading"
    contains:


        AlphaMask("Kitty_Anal_Zero_animation1", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking2:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_animation2", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking3:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_animation3", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"

image Kitty_Sex_Anal_Open_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"
        yoffset 3

image Kitty_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease .75 xzoom 1.0
        pause 1.75
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Kitty_Sex_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6




image Kitty_Anal_Zero_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,600)
        zoom 1.4

image Kitty_Anal_Zero_animation1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,600)
        zoom 1.4
        block:
            ease 1 pos (500,570)
            pause 1
            ease 3 pos (500,600)
            repeat

image Kitty_Anal_Zero_animation2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,570)
        zoom 1.4
        block:
            ease 1 pos (500,450)
            pause 1
            ease 3 pos (500,570)
            repeat

image Kitty_Anal_Zero_animation3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,570)
        zoom 1.4
        block:
            ease .25 pos (500,450)
            pause .25
            ease 1.5 pos (500,570)
            repeat



image Kitty_Hotdog_Zero_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (498,570)
        zoom 1.4

image Kitty_Hotdog_Zero_animation1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (498,500)
        zoom 1.4
        block:
            ease 1 pos (498,560)
            pause .5
            ease 1.5 pos (498,500)
            repeat

image Kitty_Hotdog_Zero_animation2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (500,510)
        zoom 1.4
        block:
            ease .5 pos (500,400)
            pause .5
            ease 1 pos (500,510)
            repeat

image Kitty_Hotdog_Body_animation2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .30
            ease .50 pos (0,-10)
            pause .20
            ease 1 pos (0,0)
            repeat

image Kitty_Hotdog_Legs_animation2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .20
            ease .50 pos (0,-10)
            pause .20
            ease 1.1 pos (0,0)
            repeat





image Kitty_Footcock:
    contains:
        subpixel True
        "Blowcock"
        alpha 0.8
        zoom 0.7
        anchor (0.5,0.5)
        offset (465,70)
        pos (0,0)
    pos (750,230)

image Kitty_Footcock_animation0:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
    pos (750,230)

image Kitty_Footcock_Zero_animation1:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause .5
            easein .75 ypos 360
            ease .25 ypos 355
            pause 1
            ease 2.50 ypos 270
            repeat
    pos (750,230)

image Kitty_Footcock_Zero_animation2:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause .2
            easein .4 ypos 360
            ease .2 ypos 355
            pause .2
            ease 1.00 ypos 270
            repeat
    pos (750,230)

transform Kitty_Footcock_Zero_animation1A():
    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset 60
        ease .25 yoffset 55
        pause 1
        ease 1.50 yoffset -30
        repeat

transform Kitty_Footcock_Zero_animation2A():
    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset 60
        ease .2 yoffset 55
        pause .2
        ease 1.00 yoffset -30
        pause .2
        easein .4 yoffset 60
        ease .2 yoffset 55
        pause .2
        ease 1.00 yoffset -30
        repeat

transform Kitty_Footcock_animation0A():
    subpixel True
    offset (0,-5)
    block:

        pause .5
        ease 1 yoffset 0
        pause 1
        ease 1.50 yoffset -5
        repeat

image Kitty_Sex_Legs_FootAnim1:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-65)
            ease .25 pos (0,-60)
            pause 1
            ease 2.50 pos (0,25)
            repeat
    pos (750,230)

image Kitty_Sex_Legs_FootAnim2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause .2
            easein .4 pos (0,-65)
            ease .2 pos (0,-60)
            pause .2
            ease 1.0 pos (0,25)
            repeat
    pos (750,230)

image Kitty_Sex_Legs_FootAnimStatic:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
    pos (750,230)

transform Kitty_Sex_Legs_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset -65
        ease .25 yoffset -60
        pause 1
        ease 1.50 yoffset 25
        repeat

transform Kitty_Sex_Legs_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset -65
        ease .2 yoffset -60
        pause .2
        ease 1.0 yoffset 25
        pause .2
        easein .4 yoffset -65
        ease .2 yoffset -60
        pause .2
        ease 1.0 yoffset 25
        repeat

transform Kitty_Sex_Legs_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause .5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





image Kitty_Sex_Body_FootAnim1:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-25)
            ease .25 pos (0,-15)
            pause 1
            ease 2.50 pos (0,15)
            repeat
    pos (750,230)

image Kitty_Sex_Body_FootAnim2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause .2
            easein .4 pos (0,-25)
            ease .2 pos (0,-15)
            pause .2
            ease 1.0 pos (0,15)
            repeat
    pos (750,230)

image Kitty_Sex_Body_FootAnimStatic:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
    pos (750,230)

transform Kitty_Sex_Body_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset -25
        ease .25 yoffset -15
        pause 1
        ease 1.50 yoffset 15
        repeat

transform Kitty_Sex_Body_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset -25
        ease .2 yoffset -15
        pause .2
        ease 1.0 yoffset 15
        pause .2
        easein .4 yoffset -25
        ease .2 yoffset -15
        pause .2
        ease 1.0 yoffset 15
        repeat

transform Kitty_Sex_Body_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause .5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





label Kitty_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action





    $ Player.Sprite = 1
    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Cock = "in"
        if offhand_action in ("fondle pussy","dildo pussy","lick pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.Cock = "anal"
        if offhand_action in ("insert ass","dildo anal","lick ass"):
            $ offhand_action = 0
    elif Line == "hotdog":
        $ Player.Cock = "out"
    elif Line == "footjob":
        $ show_feet = 1
        $ Player.Cock = "footjob"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    else:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        $ action_speed = 0
    $ primary_action = Line

    if KittyX.pose == "doggy":
        call Kitty_Doggy_Launch (Line)
        return
    if renpy.showing("Kitty_SexSprite"):
        return
    $ action_speed = 0
    call hide_girl(KittyX, hide_sprite = True)
    show Kitty_SexSprite zorder 150



    with dissolve
    return

label Kitty_Sex_Reset:
    if renpy.showing("Kitty_Doggy_Animation"):
        call Kitty_Doggy_Reset
        return
    if not renpy.showing("Kitty_SexSprite"):
        return
    $ KittyX.arm_pose = 2
    hide Kitty_SexSprite
    call hide_girl(KittyX)

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Kitty_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Kitty_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "action_speed", "Kitty_Doggy_Anal_Head_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "True", "Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Kitty_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "action_speed", "Kitty_Doggy_Anal_Head_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "True", "Kitty_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.Cock == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Kitty_Doggy_Feet2",
                    "action_speed", "Kitty_Doggy_Feet1",
                    "True", "Kitty_Doggy_Feet0",
                    ),
            "not Player.Sprite and show_feet", "Kitty_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Kitty_Doggy_Body:
    LiveComposite(

        (420,750),

        (0,105), "Kitty_Doggy_Head",


        (0,0), "images/KittyDoggy/Kitty_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not KittyX.outfit['bra']", Null(),
            "KittyX.top_pulled_up", ConditionSwitch(
                    "KittyX.outfit['top'] and KittyX.outfit['top'] != '_towel' and KittyX.outfit['top'] != '_jacket'", Null(),
                    "KittyX.outfit['bra'] == '_dress' and KittyX.outfit['top'] and KittyX.outfit['top'] != '_towel'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_UpC.png",
                    "KittyX.outfit['bra'] == '_dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_Up.png",
                    "KittyX.outfit['bra'] == '_cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami_Up.png",
                    "KittyX.outfit['bra'] == '_lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
                    "KittyX.outfit['bra'] == '_sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports_Up.png",
                    "KittyX.outfit['bra'] == '_bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
                    ),
            "KittyX.outfit['bra'] == '_dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress.png",
            "KittyX.outfit['bra'] == '_cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami.png",
            "KittyX.outfit['bra'] == '_lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
            "KittyX.outfit['bra'] == '_sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports.png",
            "KittyX.outfit['bra'] == '_bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Body_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.outfit['top']", Null(),
            "KittyX.outfit['top'] == '_jacket'", "images/KittyDoggy/Kitty_Doggy_Over_Jacket.png",
            "KittyX.outfit['top'] == '_red_shirt'", "images/KittyDoggy/Kitty_Doggy_Over_Red.png",
            "KittyX.outfit['top'] == '_pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink.png",
            "KittyX.outfit['top'] == '_towel' and not KittyX.top_pulled_up", "images/KittyDoggy/Kitty_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.spunk[back]", "images/KittyDoggy/Kitty_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Kitty_Doggy_GropeBreast",
            "True", Null()
            ),


        )


    offset (-30,0)



image Kitty_Doggy_Head:
    LiveComposite(

        (420,750),


        (0,0), ConditionSwitch(


            "KittyX.blushing", "images/KittyDoggy/Kitty_Doggy_Head_Blush.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.mouth == '_normal'", "images/KittyDoggy/Kitty_Doggy_mouth_Normal.png",
            "KittyX.mouth == '_lipbite'", "images/KittyDoggy/Kitty_Doggy_mouth_Smile.png",
            "KittyX.mouth == '_sucking'", "images/KittyDoggy/Kitty_Doggy_mouth_Tongue.png",
            "KittyX.mouth == '_kiss'", "images/KittyDoggy/Kitty_Doggy_mouth_Kiss.png",
            "KittyX.mouth == '_sad'", "images/KittyDoggy/Kitty_Doggy_mouth_Sad.png",
            "KittyX.mouth == '_smile'", "images/KittyDoggy/Kitty_Doggy_mouth_Smile.png",
            "KittyX.mouth == '_grimace'", "images/KittyDoggy/Kitty_Doggy_mouth_Smile.png",
            "KittyX.mouth == '_surprised'", "images/KittyDoggy/Kitty_Doggy_mouth_Kiss.png",
            "KittyX.mouth == '_tongue'", "images/KittyDoggy/Kitty_Doggy_mouth_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_mouth_Normal.png",
            ),





        (0,0), ConditionSwitch(

            "not KittyX.spunk['mouth']", Null(),


            "KittyX.mouth == '_lipbite'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == '_smile'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == '_grimace'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == '_sucking'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",


            "KittyX.mouth == '_tongue'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "KittyX.brows == '_angry'", "images/KittyDoggy/Kitty_Doggy_brows_Angry.png",
            "KittyX.brows == '_sad'", "images/KittyDoggy/Kitty_Doggy_brows_Sad.png",
            "KittyX.brows == '_surprised'", "images/KittyDoggy/Kitty_Doggy_brows_Surprised.png",

            "True", "images/KittyDoggy/Kitty_Doggy_brows_Normal.png",
            ),
        (0,0), "Kitty Doggy Blink",





        (0,0), ConditionSwitch(

            "KittyX.spunk['face']", "images/KittyDoggy/Kitty_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.outfit['hair'] == '_wet'", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png",
            "KittyX.outfit['hair'] == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Long.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.spunk['hair']", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 0.8
































image Kitty Doggy Blink:

    ConditionSwitch(
        "KittyX.eyes == '_sexy'", "images/KittyDoggy/Kitty_Doggy_eyes_Sexy.png",
        "KittyX.eyes == '_side'", "images/KittyDoggy/Kitty_Doggy_eyes_Side.png",

        "KittyX.eyes == '_closed'", "images/KittyDoggy/Kitty_Doggy_eyes_Closed.png",

        "KittyX.eyes == '_down'", "images/KittyDoggy/Kitty_Doggy_eyes_Down.png",
        "KittyX.eyes == '_stunned'", "images/KittyDoggy/Kitty_Doggy_eyes_Stunned.png",

        "KittyX.eyes == '_squint'", "images/KittyDoggy/Kitty_Doggy_eyes_Sexy.png",
        "True", "images/KittyDoggy/Kitty_Doggy_eyes_Normal.png",
        ),






    3

    "images/KittyDoggy/Kitty_Doggy_eyes_Closed.png"
    .25
    repeat

image Kitty_Doggy_Ass:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not KittyX.upskirt", Null(),
            "KittyX.outfit['bottom'] == '_dress'", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png",
            "KittyX.outfit['bottom'] == '_shorts' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png",
            "KittyX.outfit['bottom'] == '_shorts'", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png",
            "KittyX.outfit['bottom'] == '_yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.outfit['bottom'] and KittyX.outfit['bottom'] != '_blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.outfit['underwear'] == '_green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png",
            "KittyX.outfit['underwear'] == '_green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms' and KittyX.grool","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms'","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png",
            "KittyX.outfit['underwear'] == '_lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittyDoggy/Kitty_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "KittyX.wet", "images/KittyDoggy/Kitty_Doggy_Ass_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['hose'] == '_stockings'", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "(KittyX.outfit['bottom'] and KittyX.outfit['bottom'] != '_blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.outfit['hose'] == '_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.outfit['bottom'] and KittyX.outfit['bottom'] != '_blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.outfit['underwear'] == '_green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png",
            "KittyX.outfit['underwear'] == '_green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png",
            "KittyX.outfit['underwear'] == '_lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.outfit['hose'] and KittyX.outfit['hose'] != '_garterbelt'", Null(),
            "KittyX.outfit['bottom'] == '_capris' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png",
            "KittyX.outfit['bottom'] == '_black_jeans' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png",
            "KittyX.outfit['bottom'] == '_yoga_pants' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",
            "KittyX.outfit['bottom'] == '_shorts' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Pussy_Fucking3",
                    "action_speed > 1", "Kitty_Pussy_Fucking2",
                    "action_speed", "Kitty_Pussy_Heading",
                    "True", "Kitty_Pussy_animation0",
                    ),
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pussy_Open.png",
            "KittyX.outfit['bottom'] and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "KittyX.outfit['underwear'] and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Kitty_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Kitty_Pussy_Fucking2",
            "True", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            ),

        (0,0), ConditionSwitch(

            "KittyX.spunk[pussy] and Player.Cock == 'in'",Null(),
            "KittyX.spunk[pussy] ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "KittyX.grool and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "KittyX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "(KittyX.outfit['bottom'] and KittyX.outfit['bottom'] != '_blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            "KittyX.outfit['underwear']", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "KittyX.outfit['hose'] == '_pantyhose' and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_OpenC.png",
            "KittyX.outfit['hose'] == '_pantyhose'", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "KittyX.outfit['front_inner_accessory'] == '_barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.outfit['front_inner_accessory'] == '_ring' and KittyX.outfit['underwear'] and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.outfit['front_inner_accessory'] == '_ring' and KittyX.outfit['hose'] == '_pantyhose' and not (KittyX.outfit['underwear'] and KittyX.underwear_pulled_down)", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.outfit['front_inner_accessory'] == '_ring' and KittyX.outfit['bottom'] and KittyX.outfit['bottom'] != '_blue_skirt' and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.outfit['front_inner_accessory'] == '_ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Anal_Fucking2",
                    "action_speed > 1", "Kitty_Anal_Fucking",
                    "action_speed", "Kitty_Anal_Heading",
                    "True", "Kitty_Anal",
                    ),


            "KittyX.outfit['bottom'] and not KittyX.upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "KittyX.outfit['underwear'] and not KittyX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Kitty_Anal_Fingering",
            "primary_action == 'dildo anal'", "Kitty_Anal_Fucking",
            "KittyX.used_to_anal", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),









        (0,0), ConditionSwitch(

            "KittyX.underwear_pulled_down or not KittyX.outfit['underwear']", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),


            "KittyX.outfit['underwear'] == '_green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_GreenW.png",
            "KittyX.outfit['underwear'] == '_green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            "KittyX.outfit['underwear'] == '_lace_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Lace.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_BikiniW.png",
            "KittyX.outfit['underwear'] == '_bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "(KittyX.outfit['bottom'] or KittyX.outfit['bottom'] == '_blue_skirt') or not KittyX.upskirt", Null(),
            "KittyX.outfit['hose'] == '_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['bottom'] == '_dress'", ConditionSwitch(
                    "KittyX.upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png",
                    ),
            "KittyX.outfit['bottom'] == '_blue_skirt'", ConditionSwitch(
                    "KittyX.upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png",
                    ),

            "KittyX.upskirt", Null(),
            "KittyX.outfit['bottom'] == '_capris'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png",
                    ),
            "KittyX.outfit['bottom'] == '_black_jeans'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png",
                    ),
            "KittyX.outfit['bottom'] == '_yoga_pants'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png",
                    ),
            "KittyX.outfit['bottom'] == '_shorts'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png",
                    ),





            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['bottom'] == '_blue_skirt' and KittyX.upskirt", Null(),
            "KittyX.outfit['bottom'] == '_dress' and KittyX.upskirt", Null(),
            "KittyX.outfit['top'] == '_pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink_Tail.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['bottom'] == '_dress' and KittyX.upskirt", Null(),
            "KittyX.outfit['top'] == '_towel' and KittyX.top_pulled_up", Null(),
            "KittyX.outfit['top'] == '_towel' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Towel_Up.png",
            "KittyX.outfit['top'] == '_towel'", "images/KittyDoggy/Kitty_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.spunk[back]", "images/KittyDoggy/Kitty_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'eat_pussy'", "Rogue_Doggy_Lick_Pussy",
            "primary_action == 'eat_ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),

            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),


            "action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Kitty_Doggy_Feet:
    contains:
        AlphaMask("Kitty_Doggy_Shins", "images/KittyDoggy/Kitty_Doggy_Feet_Mask.png")

image Kitty_Doggy_Shins:



    contains:

        ConditionSwitch(
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hole.png",
            "KittyX.outfit['hose'] and KittyX.outfit['hose'] != '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet_Legs.png"
            )
    contains:

        ConditionSwitch(
            "KittyX.outfit['bottom'] == '_capris'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Blue.png",
            "KittyX.outfit['bottom'] == '_black_jeans'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Black.png",
            "KittyX.outfit['bottom'] == '_yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Yoga.png",
            "True", Null(),
            )
    contains:



        ConditionSwitch(
            "not Player.Sprite or Player.Cock == 'footjob'", ConditionSwitch(
                    "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_HoleF.png",
                    "KittyX.outfit['hose'] and KittyX.outfit['hose'] != '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_HoseF.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_FeetF.png"
                    ),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_Hole.png",
            "KittyX.outfit['hose'] and KittyX.outfit['hose'] != '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet.png"
            )












image Kitty_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Kitty_Hotdog_animation0:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Kitty_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Kitty_Doggy_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Kitty_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Kitty_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Kitty_Pussy_Mask:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_Pussy_Mask_animation0:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat


































image Kitty_Pussy_animation0:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_animation0", "Kitty_Pussy_Mask_animation0")
    contains:


        AlphaMask("Kitty_PussyHole_animation0", "Kitty_Pussy_Hole_Mask_animation0")

image Kitty_Pussy_Hole_Mask_animation0:

    contains:

        AlphaMask("images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_PussyHole_animation0:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Heading:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Heading", "Kitty_Pussy_Mask")
    contains:


        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")


image Kitty_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_Pussy_Heading_Flap:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Fingering:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_doggy_pussy_mask")
    contains:



        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")



image Kitty_Pussy_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),



image Kitty_Pussy_Fucking3:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Kitty_Anal:

    contains:

        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)

image Kitty_Anal_Fingering:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Kitty_Anal_Heading:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Zero_Kitty_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Kitty_Doggy_Anal_Heading_Mask")

image Zero_Kitty_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Kitty_Doggy_Anal_Heading_Mask:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat

image Kitty_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Kitty_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Kitty_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Kitty_Anal_Fucking:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            pause .25
            ease .25 zoom 1
            pause .75
            ease 1 zoom .95
            pause .25
            repeat
    contains:
        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Kitty_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Kitty_Doggy_Anal_FullMask:
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
    contains:



        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        pause .4
        block:
            ease .2 ypos -10
            pause .3
            ease 2 ypos 0
            repeat

image Kitty_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Kitty_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Kitty_Anal_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            pause .1
            ease .1 zoom 1
            pause .3
            ease .3 zoom .95
            pause .1
            repeat
    contains:






        ConditionSwitch(

            "KittyX.outfit['hose'] == '_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.outfit['hose'] == '_stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.outfit['underwear'] and KittyX.underwear_pulled_down", Null(),
            "KittyX.outfit['hose'] == '_ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Kitty_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause .15
            ease .1 ypos -20
            pause .1
            easein .5 ypos 0
            pause .05
            repeat

image Kitty_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Kitty_Doggy_Feet0:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            subpixel True
            pause .5
            ease 2 ypos 0
            pause .5
            ease 2 ypos -20
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            subpixel True
            pause .5
            ease 2 ypos 0
            pause .5
            ease 2 ypos -20
            repeat

image Kitty_Doggy_Feet1:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .4
            ease 1.7 ypos 540
            ease .9 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Kitty_Doggy_Feet2:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .07
            ease .6 ypos 540
            ease .28 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat




label Kitty_Doggy_Launch(Line=primary_action):
    if renpy.showing("Kitty_Doggy_Animation"):
        return
    $ action_speed = 0
    call hide_girl(KittyX, hide_sprite = True)
    show Kitty_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Kitty_Doggy_Reset:
    if not renpy.showing("Kitty_Doggy_Animation"):
        return

    $ KittyX.arm_pose = 2
    $ KittyX.SpriteVer = 0
    hide Kitty_Doggy_Animation
    call hide_girl(KittyX)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return













image Kitty_BJ_Animation:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_0()),
            "action_speed == 1", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_1()),
            "action_speed == 2", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),
            "action_speed == 3", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_3()),
            "action_speed == 4", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_4()),
            "action_speed == 5", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),
            "action_speed == 6", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Head", Kitty_BJ_Head_0()),
            "action_speed == 1", At("Kitty_BJ_Head", Kitty_BJ_Head_1()),
            "action_speed == 2", At("Kitty_BJ_Head", Kitty_BJ_Head_2()),
            "action_speed == 3", At("Kitty_BJ_Head", Kitty_BJ_Head_3()),
            "action_speed == 4", At("Kitty_BJ_Head", Kitty_BJ_Head_4()),
            "action_speed == 5", At("Kitty_BJ_Head", Kitty_BJ_Head_5()),
            "action_speed == 6", At("Kitty_BJ_Head", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Blowcock", Kitty_BJ_Cock_0()),
            "action_speed == 1", At("Blowcock", Kitty_BJ_Cock_1()),
            "action_speed >= 2", At("Blowcock", Kitty_BJ_Cock_2()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_mouthSuckingMask"), Kitty_BJ_Head_3()),
            "action_speed == 4", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_mouthSuckingMask"), Kitty_BJ_Head_4()),
            "action_speed == 6", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_mouthSuckingMask"), Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_2()),
            "action_speed == 5", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or not KittyX.spunk['mouth']", Null(),
            "action_speed == 3", At("KittySuckingSpunk", Kitty_BJ_Head_3()),
            "action_speed == 4", At("KittySuckingSpunk", Kitty_BJ_Head_4()),
            "action_speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed == 2 and KittyX.spunk[mouth]", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_2()),
            "action_speed == 5 and KittyX.spunk[mouth]", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Kitty_BJ_HairBack:

    ConditionSwitch(
            "KittyX.wet and KittyX.outfit['hair'] == '_evo'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "KittyX.outfit['hair'] == 'long'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50







image Kitty_BJ_Backdrop:

    LiveComposite(
        (858,928),
        (-375,250), ConditionSwitch(

            "'blanket' in KittyX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.outfit['top'] == '_red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),
        (0,0),"images/KittyBJFace/Kitty_BJ_Body.png",

        (0,0), ConditionSwitch(

            "KittyX.outfit['neck'] == '_gold_necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.outfit['neck'] == '_star_necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.outfit['front_inner_accessory']", Null(),
            "KittyX.outfit['front_inner_accessory'] == '_ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",
            ),
        (0,0), ConditionSwitch(

            "not KittyX.wet", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),

        (0,0), ConditionSwitch(

            "not KittyX.outfit['bra']", Null(),
            "KittyX.outfit['bra'] == '_lace_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "KittyX.outfit['bra'] == '_sports_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "KittyX.outfit['bra'] == '_bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "KittyX.outfit['bra'] == '_cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.outfit['top']", Null(),
            "KittyX.outfit['top'] == '_pink_top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "KittyX.outfit['top'] == '_red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "KittyX.outfit['top'] == '_towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.spunk['breasts']", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),
        )
    zoom 1.5
    offset (-300,-200)

image Kitty_BJ_Head:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.outfit['hair'] == '_wet'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "action_speed <= 2 or action_speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "KittyX.wet", ConditionSwitch(

                            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png",
                            ),
                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
                    ),

            "KittyX.wet", ConditionSwitch(

                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png",
                    ),
            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(

            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_mouth_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png",
                    "action_speed == 6", "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png",
                    "True", "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_mouth_Tongue.png",
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_mouth_Kiss.png",
            "KittyX.mouth == '_normal'", "images/KittyBJFace/Kitty_BJ_mouth_Smile.png",
            "KittyX.mouth == '_lipbite'", "images/KittyBJFace/Kitty_BJ_mouth_Lipbite.png",
            "KittyX.mouth == '_sucking'", "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png",
            "KittyX.mouth == '_kiss'", "images/KittyBJFace/Kitty_BJ_mouth_Kiss.png",
            "KittyX.mouth == '_sad'", "images/KittyBJFace/Kitty_BJ_mouth_Sad.png",
            "KittyX.mouth == '_smile'", "images/KittyBJFace/Kitty_BJ_mouth_Smile.png",
            "KittyX.mouth == '_grimace'", "images/KittyBJFace/Kitty_BJ_mouth_Smile.png",
            "KittyX.mouth == '_surprised'", "images/KittyBJFace/Kitty_BJ_mouth_Surprised.png",
            "KittyX.mouth == '_tongue'", "images/KittyBJFace/Kitty_BJ_mouth_Tongue.png",
            "True", "images/KittyBJFace/Kitty_BJ_mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Kitty_BJ_Animation')", Null(),
            "action_speed == 2", At("Kitty_BJ_mouthHeading", Kitty_BJ_mouthAnim()),
            "action_speed == 5", At("Kitty_BJ_mouthHeading", Kitty_BJ_mouthAnimC()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.spunk['mouth']", Null(),
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    ),
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == '_normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == '_lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.mouth == '_kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == '_sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == '_smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == '_surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.mouth == '_tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.mouth == '_sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.brows == '_normal'", "images/KittyBJFace/Kitty_BJ_brows_Normal.png",
            "KittyX.brows == '_angry'", "images/KittyBJFace/Kitty_BJ_brows_Angry.png",
            "KittyX.brows == '_sad'", "images/KittyBJFace/Kitty_BJ_brows_Sad.png",
            "KittyX.brows == '_surprised'", "images/KittyBJFace/Kitty_BJ_brows_Surprised.png",
            "KittyX.brows == '_confused'", "images/KittyBJFace/Kitty_BJ_brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",

        (0,0), ConditionSwitch(

            "KittyX.spunk['face']", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.wet or KittyX.outfit['hair'] == '_wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "KittyX.outfit['hair'] == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "KittyX.outfit['hair'] == '_evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.wet", Null(),
            "action_speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.spunk['hair']", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:

    ConditionSwitch(
            "KittyX.eyes == '_normal'", "images/KittyBJFace/Kitty_BJ_eyes_Normal.png",
            "KittyX.eyes == '_sexy'", "images/KittyBJFace/Kitty_BJ_eyes_Sexy.png",
            "KittyX.eyes == '_closed'", "images/KittyBJFace/Kitty_BJ_eyes_Closed.png",
            "KittyX.eyes == '_surprised'", "images/KittyBJFace/Kitty_BJ_eyes_Surprised.png",
            "KittyX.eyes == '_side'", "images/KittyBJFace/Kitty_BJ_eyes_Side.png",
            "KittyX.eyes == '_stunned'", "images/KittyBJFace/Kitty_BJ_eyes_Surprised.png",
            "KittyX.eyes == '_down'", "images/KittyBJFace/Kitty_BJ_eyes_Down.png",
            "KittyX.eyes == '_manic'", "images/KittyBJFace/Kitty_BJ_eyes_Surprised.png",
            "KittyX.eyes == '_squint'", "images/KittyBJFace/Kitty_BJ_eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittyBJFace/Kitty_BJ_eyes_Closed.png"
    .25
    repeat

image Kitty_BJ_mouthHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Kitty_BJ_mouthSuckingMask:

    contains:
        "images/KittyBJFace/Kitty_BJ_mouth_SuckingMask.png"
        zoom 1.4
    contains:
        ConditionSwitch(
            "not KittyX.spunk['mouth']", Null(),
            "Speed != 2 and action_speed != 5", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            )
        zoom 1.4

image Kitty_BJ_MaskHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_mouth_SuckingMask.png"
        offset (-380,-595)

image Kitty_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Kitty_BJ_MaskHeading", Kitty_BJ_mouthAnim()),
            "action_speed == 5", At("Kitty_BJ_MaskHeading", Kitty_BJ_mouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Kitty_BJ_MaskHeadingSpunk:

    At("KittySuckingSpunk", Kitty_BJ_mouthAnim())
    zoom 1.8

image KittySuckingSpunk:
    contains:
        "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png"
        zoom 1.4
        anchor (0.5, 0.5)

transform Kitty_BJ_mouthAnim():

    subpixel True
    zoom 0.7
    block:
        pause .40
        easeout .40 zoom 0.69
        linear .10 zoom 0.7
        easein .45 zoom 0.65
        pause .15

        easeout .25 zoom 0.7
        linear .10 zoom 0.69
        easein .30 zoom 0.7
        pause .35

        repeat
transform Kitty_BJ_mouthAnimC():

    subpixel True
    zoom 0.7
    block:
        pause .20
        ease .50 zoom 0.65
        pause .60
        ease .30 zoom 0.7
        pause .10
        ease .30 zoom 0.65
        pause .20
        ease .30 zoom 0.7
        repeat

image Blanket:
    contains:
        "images/KittyBJFace/Kitty_BJFace_Blanket.png"
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image Blanket = LiveComposite(
    (858,928),
    (0, 0), "images/KittyBJFace/Kitty_BJFace_Blanket.png"
    )


transform Kitty_BJ_Cock_0():

    anchor (.5,.5)
    rotate -10
transform Kitty_BJ_Cock_1():

    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat
transform Kitty_BJ_Cock_2():

    anchor (.5,.5)
    rotate 0





transform Kitty_BJ_Head_0():

    subpixel True
    ease 1.5 offset (0,0)
transform Kitty_BJ_Body_0():

    subpixel True
    ease 1.5 offset (0,0)


transform Kitty_BJ_Head_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat
transform Kitty_BJ_Body_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat

transform Kitty_BJ_Head_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 35
        ease 1.5 offset (0,-40)
        repeat
transform Kitty_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Kitty_BJ_Head_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat
transform Kitty_BJ_Body_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Kitty_BJ_Head_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Kitty_BJ_Body_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Kitty_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Kitty_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Kitty_BJ_Head_6():

    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Kitty_BJ_Body_6():

    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat






label Kitty_BJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_BJ_Animation"):
        return

    call hide_girl(KittyX)
    if Line == "L" or Line == "cum":
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."
        if not KittyX.action_counter["blowjob"]:
            "[KittyX.name] hesitantly kneels down and touches her mouth to your cock."
        else:
            "[KittyX.name] kneels down and begins to suck on your cock."

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 0
    show Kitty_BJ_Animation zorder 150:
        pos (645,510)
    return

label Kitty_BJ_Reset:
    if not renpy.showing("Kitty_BJ_Animation"):
        return
    call hide_girl(KittyX)
    $ action_speed = 0

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)

    return









image Kitty_TJ_Animation:

    contains:
        ConditionSwitch(

            "Player.Sprite", ConditionSwitch(

                    "action_speed == 1", "Kitty_TJ_Body_1",
                    "action_speed == 2", "Kitty_TJ_Body_2",
                    "action_speed == 3", "Kitty_TJ_Body_3",
                    "action_speed >= 5", "Kitty_TJ_Body_5",
                    "True",       "Kitty_TJ_Body_0",
                    ),
            "True","Kitty_TJ_Body_0",
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)


image Kitty_TJ_Torso:

    contains:

        "images/KittyBJFace/Kitty_TJ_Body.png"












































image Kitty_TJ_Arms:

    contains:

        "images/KittyBJFace/Kitty_TJ_Arms.png"

image Kitty_TJ_Tits:

    contains:


        ConditionSwitch(
            "Player.Sprite and action_speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png",
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )






















































image Kitty_Mega_Mask:

    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha .5





image Kitty_TJ_Body_0:

    contains:

        "Kitty_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        ConditionSwitch(
                    "Player.Sprite", "Blowcock",
                    "True", Null(),
                    )
        subpixel True
        pos (640,150)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_1:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.9 ypos -40
            ease 1 ypos 60
            pause .1
            repeat

image Kitty_TJ_Body_1:

    contains:

        "Kitty_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 3 ypos 210
            ease 1 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.8 ypos 280
            ease 1 ypos 330
            pause .2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.85 ypos 280
            ease 1 ypos 330
            pause .15
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.9 ypos 210
            ease 1 ypos 260
            pause .1
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.9 ypos 280
            ease 1 ypos 330
            pause .1
            repeat
    contains:

        ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_1"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease 2.8 ypos 490
            ease .8 ypos 500
            pause .4
            repeat



image Kitty_TJ_Mask_2:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease .71 ypos -15
            ease .27 ypos 60
            pause .02
            repeat

image Kitty_TJ_Body_2:

    contains:

        "Kitty_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease .7 ypos 215
            ease .25 ypos 260
            pause .05
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease .65 ypos 285
            ease .25 ypos 330
            pause .1
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease .68 ypos 285
            ease .25 ypos 330
            pause .07
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease .71 ypos 290
            ease .27 ypos 330
            pause .02
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease .68 ypos 215
            ease .25 ypos 260
            pause .07
            repeat
    contains:

        ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_2"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease .72 ypos 490
            ease .27 ypos 500
            pause .01
            repeat



image Kitty_TJ_Mask_3:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 90
            ease .6 ypos 140
            pause .2
            repeat

image Kitty_TJ_Body_3:

    contains:

        "Kitty_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        parallel:
            block:

                ease 2 pos (500,290)
                ease .6 pos (500,315)
                pause .4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease .8 pos (520,320)
                ease 2.2 pos (510,290)
                ease .8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease .6 pos (500,315)
                pause .4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease .8 pos (475,320)
                ease 2.2 pos (490,290)
                ease .8 pos (475,320)
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease .6 ypos 360
            pause .2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease .6 ypos 360
            pause .2
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease .6 ypos 360
            pause .2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,310)
        subpixel True
        rotate 0
        parallel:
            block:

                ease 2 pos (500,290)
                ease .6 pos (500,315)
                pause .4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease .8 pos (520,320)
                ease 2.2 pos (510,290)
                ease .8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease .6 pos (500,315)
                pause .4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease .8 pos (475,320)
                ease 2.2 pos (490,290)
                ease .8 pos (475,320)
            repeat
        parallel:
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease .8 rotate 10
                ease 2.2 rotate 0
                ease .8 rotate 5
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease .8 rotate -10
                ease 2.2 rotate 0
                ease .8 rotate -5
            repeat
    contains:

        ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_3"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_5:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 120
            ease 1.6 ypos 140
            pause .2
            repeat

image Kitty_TJ_Body_5:

    contains:

        "Kitty_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause .4
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause .2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause .2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,307)
        subpixel True
        rotate 0
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause .4
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause .2
            repeat
    contains:













        ConditionSwitch(

                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_5"),

                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4





























label Kitty_TJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call hide_girl(KittyX)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50
    if Line == "L" and taboo:
        if len(Present) >= 2:
            if Present[0] != KittyX:
                "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != KittyX:
                "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[KittyX.name] casually glances around to see if anyone can see her."
    if KittyX.outfit['bra'] and KittyX.outfit['top']:
        "She throws off her [KittyX.outfit['top']] and her [KittyX.outfit['bra']]."
    elif KittyX.outfit['top']:
        "She throws off her [KittyX.outfit['top']], baring her breasts underneath."
    elif KittyX.outfit['bra']:
        "She tugs off her [KittyX.outfit['bra']] and throws it aside."
    $ KittyX.outfit['top'] = 0
    $ KittyX.outfit['bra'] = 0
    $ KittyX.arm_pose = 0
    call Kitty_First_Topless
    if Line == "L":
        if not KittyX.action_counter["titjob"]:
            "She hesitantly presses your cock against her chest."
        else:
            "She squeezes her breasts around your cock."


    show blackscreen onlayer black with dissolve
    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Kitty_TJ_Animation zorder 150
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Kitty_TJ_Reset:
    if not renpy.showing("Kitty_TJ_Animation"):
        return
    call hide_girl(KittyX)
    $ Player.Sprite = 0

    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        zoom 2 xpos 550 yoffset 50
    show Kitty_sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos KittyX.sprite_location yoffset 0
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos KittyX.sprite_location

    return






















image Kitty_Hand_Under:
    "images/KittySprite/handkitty2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Kitty_Hand_Over:
    "images/KittySprite/handkitty1.png"
    anchor (0.5,0.5)
    pos (0,0)


















transform Kitty_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5
    pause 0.25
    ease 1.0 ypos -100 rotate -5
    pause 0.1
    repeat

transform Kitty_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Kitty_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_Hand_Under"),
            "action_speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_Hand_Over"),
            "action_speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Kitty_HJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call hide_girl(KittyX)
    if Line == "L":
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
    else:
        show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
        with dissolve

    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause .5
    show Kitty_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (100,250)
    return

label Kitty_HJ_Reset:
    if not renpy.showing("Kitty_HJ_Animation"):
        return
    $ action_speed = 0
    hide Kitty_HJ_Animation with easeoutbottom
    call hide_girl(KittyX)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return


label Kitty_Kissing_Launch(T=primary_action, Set=1):
    call hide_girl(KittyX)
    $ primary_action = T
    $ KittyX.pose = "kiss" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location)
    show Kitty_sprite at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Kitty_Kissing_Smooch:
    $ KittyX.change_face("kiss")
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos KittyX.sprite_location zoom 1
    $ KittyX.change_face("_sexy")
    return

label Kitty_Breasts_Launch(T=primary_action, Set=1):
    call hide_girl(KittyX)
    $ primary_action = T
    $ KittyX.pose = "breasts" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Middle_Launch(T=primary_action, Set=1):
    call hide_girl(KittyX)
    $ primary_action = T
    $ KittyX.pose = "mid" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Kitty_Pussy_Launch(T=primary_action, Set=1):
    call hide_girl(KittyX)
    $ primary_action = T
    $ KittyX.pose = "pussy" if Set else KittyX.pose
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Pos_Reset(T=0, Set=0):
    if KittyX.location != bg_current:
        return
    call hide_girl(KittyX)
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Kitty_sprite zorder KittyX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (KittyX.sprite_location,50)
    $ KittyX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Kitty_ThreewayBreasts_Launch:
    show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
    $ KittyX.arm_pose = 1
    return













image GropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (95,370)
            pause .5
            ease 1.5 rotate 30 pos (115,400)
            repeat

image LickLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,380)
            pause .5
            ease 1.5 rotate 30 pos (200,410)
            repeat

image GropeThigh_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 720
            repeat
        parallel:
            pause .5
            ease 1 rotate 110 xpos 180
            ease 1 rotate 100 xpos 200
            repeat

image GropePussy_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (210,625)
                ease .75 rotate 170 pos (210,640)
            choice:
                ease .5 rotate 190 pos (210,625)
                pause .25
                ease 1 rotate 170 pos (210,640)
            repeat

image FingerPussy_Kitty:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (230,695)
                pause .5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease .5 rotate 40 pos (230,695)
                pause .5
                ease 1.75 rotate 50 pos (220,730)
            choice:
                ease 2 rotate 40 pos (230,695)
                pause .5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
            repeat

image Lickpussy_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (220,660)
            linear .5 rotate -60 pos (210,670)
            easein 1 rotate 10 pos (240,680)
            repeat

image VibratorRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
            repeat

image VibratorLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
            repeat

image VibratorPussy_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
            repeat

image VibratorAnal_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat

image VibratorPussyInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (110,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (215,640)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (215,640)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:


                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
            choice:
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_Kitty:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice:
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc