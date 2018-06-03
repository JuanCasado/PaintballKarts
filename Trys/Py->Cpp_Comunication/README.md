# py -> cpp

This comunication module alow the user tod pass data between two different process (not threads)
*_may be OS dependent*

1. The py process is launched
2. The cpp process is launched from the py one
3. The cpp stdin and stdout are bind to the py process by pipes so the cpp process became dependant from the py one to exists

-> By threading we can talk in a fast way to the cpp process in a bidirectional way

**_try on windows**
