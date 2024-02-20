.. _manual:


.. raw:: html

    <br>


.. title:: Manual


.. raw:: html

    <center>

manual
######


.. raw:: html

    </center>
    <br>

**NAME**

 | ``KONING`` - Reconsider OTP-CR-117/19


**SYNOPSIS**

 ::

  koning <cmd> [key=val] 
  koning <cmd> [key==val]
  koning [-c] [-d] [-v]


**DESCRIPTION**


 ``KONING`` is a python3 IRC bot is intended to be programmable  in a
 static, only code, no popen, no user imports and no reading modules from
 a directory, way. It can show genocide and suicide stats of king netherlands
 his genocide into a IRC channel, display rss feeds and log simple text
 messages, source is `here <source.html>`_.



**INSTALL**

 with sudo::

  $ python3 -m pip install koning

 as user::

  $ pipx install koning

 or download the tar, see::

  https://pypi.org/project/koning


**USAGE**


 list of commands::

    $ koning cmd
    cmd,err,flt,sts,thr,upt

 start a console::

    $ koning -c
    >

 start additional modules::

    $ koning mod=<mod1,mod2> -c
    >

 list of modules::

    $ koning mod
    cmd,err,flt,fnd,irc,log,mdl,mod,
    req, rss,slg,sts,tdo,thr,upt,ver

 to start irc, add mod=irc when
 starting::

     $ koning mod=irc -c

 to start rss, also add mod=rss
 when starting::

     $ koning mod=irc,rss -c

 start as daemon::

    $ koning mod=irc,rss -d
    $ 


**CONFIGURATION**


 *irc*

 ::

    $ koning cfg server=<server>
    $ koning cfg channel=<channel>
    $ koning cfg nick=<nick>

 *sasl*

 ::

    $ koning pwd <nsvnick> <nspass>
    $ koning cfg password=<frompwd>

 *rss*

 ::

    $ koning rss <url>
    $ koning dpl <url> <item1,item2>
    $ koning rem <url>
    $ koning nme <url< <name>


**COMMANDS**


 ::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    mdl - genocide model
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    now - genocide stats
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    slg - slogan
    thr - show the running threads
    tpc - genocide stats into topic


**FILES**

 ::

    ~/.local/bin/koning
    ~/.local/pipx/venvs/koning/
    /usr/local/bin/koning
    /usr/local/share/doc/koning


**AUTHOR**


 ::
 
    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

 ::

    KONING is Public Domain.
