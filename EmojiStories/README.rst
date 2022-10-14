The text used is this one :

    After winning a trip on the RMS Titanic during a dockside card game, American
    Jack Dawson spots the society girl Rose DeWitt Bukater who is on her way to
    Philadelphia to marry her rich snob fiancé Caledon Hockley. Rose feels
    helplessly trapped by her situation and makes her way to the aft deck and thinks
    of suicide until she is rescued by Jack. Cal is therefore obliged to invite
    Jack to dine at their first-class table where he suffers through the slights of
    his snobbish hosts. In return, he spirits Rose off to third-class for an evening
    of dancing, giving her the time of her life. Deciding to forsake her intended
    future all together, Rose asks Jack, who has made his living making sketches on
    the streets of Paris, to draw her in the nude wearing the invaluable blue diamond
    Cal has given her. Cal finds out and has Jack locked away. Soon afterwards, the
    ship hits an iceberg and Rose must find Jack while both must run from Cal even
    as the ship sinks deeper into the freezing water.


Here is the first output base done with Spacy's noun chunks.
It's nice, but I think a lot of the meaning gets lost
when only the noun chunks are kept, like all the verbs,
also the names like "Rose" are treated literally.

    a trip : 💑
    the RMS Titanic : 🌝
    a dockside card game : 🎴
    American Jack Dawson : 🏈
    the society girl : 👫
    Rose DeWitt Bukater : 🌹
    who : 👫
    her way : 👫
    Philadelphia : 🇸🇲
    her rich snob fiancé Caledon Hockley : 🙎‍♀️
    Rose : 🌹
    her situation : 🙋‍♀️
    her way : 👫
    the aft deck : 🤣
    suicide : 💣
    she : 👫
    Jack : 🎃
    Cal : 🔫
    Jack : 🎃
    their first-class table : 🕜
    he : 👫
    the slights : 😂
    his snobbish hosts : 👫
    return : 🤚
    he : 👫
    third-class : 🕜
    an evening : 🌉
    dancing : 🕺
    her : 🙋‍♀️
    the time : 🤚
    her life : 😂
    her intended future : 🤚
    Rose : 🌹
    Jack : 🎃
    who : 👫
    his living : 🤚
    sketches : ✏️
    the streets : 🤘
    Paris : 🗼
    her : 🙋‍♀️
    the nude : 👙
    the invaluable blue diamond Cal : 🔹
    her : 🙋‍♀️
    Cal : 🔫
    Jack : 🎃
    the ship : 🚢
    an iceberg : 🌥️
    Rose : 🌹
    Jack : 🎃
    Cal : 🔫
    the ship : 🚢
    the freezing water : 🌊

We can see that there is some wrong in that. For example, Iceberg
should output the ice symbol, not a cloud in front of the sun. Also,
Jack is 🎃 and Rose is 🌹. Maybe these can be masked, as for other proper
nouns, to prevent mistakes.
I tried on a sentence based level, but it's way worse :

    After winning a trip on the RMS Titanic during a dockside card game, American
    Jack Dawson spots the society girl Rose DeWitt Bukater who is on her way to
    Philadelphia to marry her rich snob fiancé Caledon Hockley. : 👫
    Rose feels helplessly trapped by her situation and makes her way to the aft
    deck and thinks of suicide until she is rescued by Jack. : 👫
    Cal is therefore obliged to invite Jack to dine at their first-class table
    where he suffers through the slights of his snobbish hosts. : 🤚
    In return, he spirits Rose off to third-class for an evening of dancing, giving
    her the time of her life. : 🤚
    Deciding to forsake her intended future all together, Rose asks Jack, who has
    made his living making sketches on the streets of Paris, to draw her in the
    nude wearing the invaluable blue diamond Cal has given her. : 🤚
    Cal finds out and has Jack locked away. : 🤚
    Soon afterwards, the ship hits an iceberg and Rose must find Jack while both
    must run from Cal even as the ship sinks deeper into the freezing water. : 🤚

It's way too long to get any meaningful elements out of it. I'm off to try to
find a decent way of chunking the text into sub-parts without losing too much
meaning in the operation. Let's start by the naive approach with a window

    After winning a trip on : 🤚
    the RMS Titanic during a : 🌛
    dockside card game, American : 🎴
    Jack Dawson spots the society : 👫🏿
    girl Rose DeWitt Bukater who : 👧
    is on her way to : 🤚
    Philadelphia to marry her rich : 👩🏿‍❤️‍👩🏿
    snob fiancé Caledon Hockley. : 🙎
    Rose feels helplessly trapped by : 😱
    her situation and makes her : 👫
    way to the aft deck : 🤣
    and thinks of suicide until : 🤚
    she is rescued by Jack : 👫
    . : 👨🏼‍❤️‍👨🏼
    Cal is therefore obliged to : 🙋
    invite Jack to dine at : 🌉
    their first-class table : 🕜
    where he suffers through the : 🤚
    slights of his snobbish hosts : 😂
    . : 👨🏼‍❤️‍👨🏼
    In return, he spirits : 👨🏿‍❤️‍👨🏿
    Rose off to third- : 🙃
    class for an evening of : 🛐
    dancing, giving her the : 👫
    time of her life. : 😂
    Deciding to forsake her intended : 🙋
    future all together, Rose : 👨🏻‍❤️‍👨🏻
    asks Jack, who has : 👨‍👨‍👧‍👦
    made his living making sketches : 🤚
    on the streets of Paris : 🤣
    , to draw her in : 🤚
    the nude wearing the invaluable : 👚
    blue diamond Cal has given : 🔹
    her. : 👫
    Cal finds out and has : 🤚
    Jack locked away. : 🔏
    Soon afterwards, the ship : 👨🏻‍❤️‍👨🏻
    hits an iceberg and Rose : 🌛
    must find Jack while both : 🈶
    must run from Cal even : 🏃
    as the ship sinks deeper : 🤚
    into the freezing water. : 🌊

I don't like it. I try chunking based on the verbs :

