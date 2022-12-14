The text used is this one :

    After winning a trip on the RMS Titanic during a dockside card game, American
    Jack Dawson spots the society girl Rose DeWitt Bukater who is on her way to
    Philadelphia to marry her rich snob fiancΓ© Caledon Hockley. Rose feels
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

    a trip : π
    the RMS Titanic : π
    a dockside card game : π΄
    American Jack Dawson : π
    the society girl : π«
    Rose DeWitt Bukater : πΉ
    who : π«
    her way : π«
    Philadelphia : πΈπ²
    her rich snob fiancΓ© Caledon Hockley : πββοΈ
    Rose : πΉ
    her situation : πββοΈ
    her way : π«
    the aft deck : π€£
    suicide : π£
    she : π«
    Jack : π
    Cal : π«
    Jack : π
    their first-class table : π
    he : π«
    the slights : π
    his snobbish hosts : π«
    return : π€
    he : π«
    third-class : π
    an evening : π
    dancing : πΊ
    her : πββοΈ
    the time : π€
    her life : π
    her intended future : π€
    Rose : πΉ
    Jack : π
    who : π«
    his living : π€
    sketches : βοΈ
    the streets : π€
    Paris : πΌ
    her : πββοΈ
    the nude : π
    the invaluable blue diamond Cal : πΉ
    her : πββοΈ
    Cal : π«
    Jack : π
    the ship : π’
    an iceberg : π₯οΈ
    Rose : πΉ
    Jack : π
    Cal : π«
    the ship : π’
    the freezing water : π

We can see that there is some wrong in that. For example, Iceberg
should output the ice symbol, not a cloud in front of the sun. Also,
Jack is π and Rose is πΉ. Maybe these can be masked, as for other proper
nouns, to prevent mistakes.
I tried on a sentence based level, but it's way worse :

    After winning a trip on the RMS Titanic during a dockside card game, American
    Jack Dawson spots the society girl Rose DeWitt Bukater who is on her way to
    Philadelphia to marry her rich snob fiancΓ© Caledon Hockley. : π«
    Rose feels helplessly trapped by her situation and makes her way to the aft
    deck and thinks of suicide until she is rescued by Jack. : π«
    Cal is therefore obliged to invite Jack to dine at their first-class table
    where he suffers through the slights of his snobbish hosts. : π€
    In return, he spirits Rose off to third-class for an evening of dancing, giving
    her the time of her life. : π€
    Deciding to forsake her intended future all together, Rose asks Jack, who has
    made his living making sketches on the streets of Paris, to draw her in the
    nude wearing the invaluable blue diamond Cal has given her. : π€
    Cal finds out and has Jack locked away. : π€
    Soon afterwards, the ship hits an iceberg and Rose must find Jack while both
    must run from Cal even as the ship sinks deeper into the freezing water. : π€

It's way too long to get any meaningful elements out of it. I'm off to try to
find a decent way of chunking the text into sub-parts without losing too much
meaning in the operation. Let's start by the naive approach with a window

    After winning a trip on : π€
    the RMS Titanic during a : π
    dockside card game, American : π΄
    Jack Dawson spots the society : π«πΏ
    girl Rose DeWitt Bukater who : π§
    is on her way to : π€
    Philadelphia to marry her rich : π©πΏββ€οΈβπ©πΏ
    snob fiancΓ© Caledon Hockley. : π
    Rose feels helplessly trapped by : π±
    her situation and makes her : π«
    way to the aft deck : π€£
    and thinks of suicide until : π€
    she is rescued by Jack : π«
    . : π¨πΌββ€οΈβπ¨πΌ
    Cal is therefore obliged to : π
    invite Jack to dine at : π
    their first-class table : π
    where he suffers through the : π€
    slights of his snobbish hosts : π
    . : π¨πΌββ€οΈβπ¨πΌ
    In return, he spirits : π¨πΏββ€οΈβπ¨πΏ
    Rose off to third- : π
    class for an evening of : π
    dancing, giving her the : π«
    time of her life. : π
    Deciding to forsake her intended : π
    future all together, Rose : π¨π»ββ€οΈβπ¨π»
    asks Jack, who has : π¨βπ¨βπ§βπ¦
    made his living making sketches : π€
    on the streets of Paris : π€£
    , to draw her in : π€
    the nude wearing the invaluable : π
    blue diamond Cal has given : πΉ
    her. : π«
    Cal finds out and has : π€
    Jack locked away. : π
    Soon afterwards, the ship : π¨π»ββ€οΈβπ¨π»
    hits an iceberg and Rose : π
    must find Jack while both : πΆ
    must run from Cal even : π
    as the ship sinks deeper : π€
    into the freezing water. : π

I don't like it. I try chunking based on the verbs :

